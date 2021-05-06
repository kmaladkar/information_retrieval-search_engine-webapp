#search.py
import json
from nltk.stem import PorterStemmer 
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter, defaultdict
import numpy as np
import pandas as pd

class OkapiBM25:
    def __init__(self, path):
        self.path = path
        self.stemmer = PorterStemmer() 
        self.en_stopwords = set(stopwords.words("english"))
        self.data_pd = pd.read_csv(self.path)

    def preprocess(self, text):
        """
        Preprocess the text by stemmming and removing stop words and digits
        """
        words = word_tokenize(text.lower())
        words = [self.stemmer.stem(word) for word in words if not (not word.isalnum() and not word.isnumeric() and word not in self.en_stopwords)]
        return words

    def process_idf_avgLen(self):
        """
        Set up the self.avg_len to prepare for the OkapiBM25 scoring
        """
        def get_idf(qi):
            """
            Get idf score
            """
            num = N - doc_counter[qi] + 0.5
            den = doc_counter[qi] + 0.5
            total = num/den + 1
            return np.log(total)

        doc_counter = Counter()
        lengths = []
        for index, row in self.data_pd.iterrows():
            counter = defaultdict(int)
            text = " ".join([row['Input.document_url']] + [row['Input.ingredients']] + [row['Input.preparation']])
            words = self.preprocess(text)
            lengths.append(len(words))
            for word in words:
                counter[word] = 1
            doc_counter.update(counter)
        self.avg_len = sum(lengths)/len(lengths)
        N = len(self.data_pd)

        self.idf = defaultdict(float)
        for word in doc_counter:
            self.idf[word] = get_idf(word)
        return self

    def process_tf(self):
        """
        Get tf score
        """
        k_1 = 1.2
        b = 0.75
        self.tf = defaultdict(dict)
        for idx, row in self.data_pd.iterrows():
            text = " ".join([row['Input.document_url']] + [row['Input.ingredients']] + [row['Input.preparation']])
            words = self.preprocess(text)
            length = len(words)
            doc_dict = {}
            for w, c in Counter(words).items():
                den = c + k_1 * (1 - b + b * length/self.avg_len)
                doc_dict[w] = c/den
            self.tf[idx] = doc_dict
        return self
        
    def get_tfidf(self, qi, D):
        """
        Put the tf and idf scores together
        """
        return self.tf[D].get(qi, 0) * self.idf.get(qi, 0)

    def build_searchDB(self):
        """
        Prepare the OkapiBM25 search scores
        """
        self.process_idf_avgLen()
        self.process_tf()
        return self

    def get_documents(self, query, n_ids = 20):
        """
        Return a dataframe that contains the top 20 entries
        according to the OkapiBM25 results
        """
        scores = []
        for doc in range(len(self.data_pd)):
            vals = []
            for token in self.preprocess(query):
                vals.append(self.get_tfidf(token, doc))
            scores.append((sum(vals), doc))

        top_docInfo = sorted(scores, reverse=True)[:n_ids]
        ids = [x[1] for x in top_docInfo]
        df = self.data_pd.iloc[ids, :].reset_index()
        filtered_df = df[["most_common",
                          "Input.document_url",
                          "Input.description", 
                          "Input.preparation"]]
        filtered_df.columns = ['Category','Title','Ingredients','Preparation']
        return filtered_df      