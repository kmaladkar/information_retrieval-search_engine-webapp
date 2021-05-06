from fastapi import FastAPI, Request, Form
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse
from nltk.corpus import brown
from collections import defaultdict
import numpy as np
from InformationRetrival.search import OkapiBM25
from MachineLearning.linearSVC.linearSVC_inference import LinearClassifier
import pickle
import nltk
nltk.download("stopwords")
nltk.download("punkt")

app = FastAPI()

search_recipes = OkapiBM25(path="./data/mturks_results_cleaned.csv").build_searchDB()
linearSVC = LinearClassifier()

# Functions for generating HTML
def create_row(data):
    '''Given a pandas dataframe will create a new HTML row out of each row in the dataframe'''
    S = []
    i = 1
    for _, row in data.iterrows(): 
        if i % 2 == 0:
            S.append("<tr class='even'>")
        else:
            S.append("<tr class='odd'>")
        i += 1
        for col in data.columns:
            S.append("<td class='table_field'>" + str(row[col]) + "</td>")
        S.append("</tr>")
    return "".join(S)

def create_header(data):
    '''Given a pandas dataframe will create a HTML header row'''
    S = []
    S.append('<tr class=\'even\'>')
    for col in data.columns:
        S.append('<th>' + col.upper() + '</th>')
    S.append('</tr>')
    return "".join(S)

def put_in_table(data):
    '''Puts given dataframe into HTML table format'''
    return "<table>" + create_header(data) + create_row(data) + "</table>"


@app.get("/")
def start():
    return FileResponse("frontend.html")

@app.get("/{filename}")
def get_file(filename):
    return FileResponse(filename)

@app.get("/pos/")
def search(category, search):
    df = search_recipes.get_documents(search)
    if category == 'all':
        filtered_df = df
    elif category == 'dessert':
        filtered_df = df[df.Category == 'Dessert']
    elif category == 'appetizer_or_side_dish':
        filtered_df = df[df.Category == 'Appetizer or side dish']
    elif category == 'main_course':
        filtered_df = df[df.Category == 'Main course']
    elif category == 'drinks':
        filtered_df = df[df.Category == 'Drinks']
    elif category == 'others':
        filtered_df = df[df.Category == 'Other']
        
    return HTMLResponse(put_in_table(filtered_df))

@app.get("/classify/")
def classifier(category, search):
    prediction = linearSVC.predict(search)
    return HTMLResponse(f"Prediction: {prediction}")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9999, debug=True)
