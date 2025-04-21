import requests

from bs4 import BeautifulSoup

import pandas as pd

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer

import lxml

import html5lib


import csv




url = "https://www.digitaltrends.com/gaming/its-beginning-to-feel-like-gaming-isnt-for-everyone/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


body = doc.article

script = body.text

article = ['article']
with open('script.csv', 'w') as f:

    writer = csv.writer(f)
    
    writer.writerow(article)

    writer.writerows(script)


dfs = pd.read_csv('script.csv')

# create preprocess_text function
def preprocess_text(text):

    # Tokenize the text

    tokens = word_tokenize(text.lower())




    # Remove stop words

    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]




    # Lemmatize the tokens

    lemmatizer = WordNetLemmatizer()

    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]




    # Join the tokens back into a string

    processed_text = ' '.join(lemmatized_tokens)

    return processed_text

# apply the function df

dfs = dfs.apply(preprocess_text)





print(dfs)
