# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import re
import string
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


def save_bar_graph(input_csv,filename):
    """
    given a csv file of annotation result, create a bar graph and output
    the image to the provided file
    """
    df_result = pd.read_csv(input_csv)
    chart = alt.Chart(df_result,title="Main Category Distribution").mark_bar().encode(
            x = alt.X('most_common', axis = alt.Axis(labels = False, title = 'Categories')),
            y = alt.Y('count()', axis = alt.Axis(title = 'Counts')),
            color=alt.Color('most_common', legend=alt.Legend(title = 'Categories',orient="left"))
            ).properties(width = 400, height = 200)
    chart.save(filename) #can save as .json or .html


def preprocess(text):
    """
    Returns stemmed text with digits, punctuation, and
    unnecessary whitespace removed.
    """
    pun = string.punctuation+ "…"
    dig = string.digits
    table_pun = str.maketrans(pun, len(pun) * " ")
    table_dig = str.maketrans(dig, len(dig) * " ")
    processed = text.lower().translate(table_pun).translate(table_dig).strip().split()
    return processed


def save_word_cloud(input_category):
    """
    With a given category ('Appetizer and side dish', 'Dessert', 'Main course'), 
    provide the corresponding wordcloud using all the ingredients in that category
    """
    filtered_res = df_result[["Input.ingredients", "Input.preparation", "Input.description","Input.document_url", 'most_common']]
    df = filtered_res[filtered_res.most_common == input_category]
    words = []
    ingredients = df['Input.ingredients'].to_list()
    stopwords_set = stopwords.words("english") + ['tablespoon','cup','teaspoon','tablespoons','teaspoons','cups','oz','chopped','sliced','salt','pepper','oil','cloves']
    for text in ingredients:
        words.extend(preprocess(text))
    text = " ".join([word for word in words])
    wordcloud = WordCloud(stopwords=stopwords_set, background_color="white").generate(text)
    filename = input_category + '.png'
    wordcloud.to_file(filename)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


