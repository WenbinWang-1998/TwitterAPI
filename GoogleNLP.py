#reference:https://drive.google.com/file/d/1dNahyZnwgqwUUdbV5I0u68b8pQADBiWi/view

import os
import tweepy
import json
from google.cloud import language


def entities_sentiment(doc):
    client = language.LanguageServiceClient()
    document = language.Document(content=doc, type_=language.Document.Type.PLAIN_TEXT)
    response = client.analyze_entity_sentiment(document=document,encoding_type='UTF32')
    res=client.analyze_sentiment(document=document,encoding_type='UTF32',)
    sentiment = res.document_sentiment
    fin = dict(
        sentence=doc,
        overallscore=f"{sentiment.score:.1%}",
        overallmagnitude=f"{sentiment.magnitude:.1%}",
    )
    print("overall sentiment: ")
    for key, value in fin.items():
        print(f"{key:15}: {value}")
    for entity in response.entities:
        print("-------------------------------------")
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            score=entity.sentiment.score,
            magnitude=entity.sentiment.magnitude
        )
        for key, value in results.items():
            print(f"{key:15}:  {value}")

def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")


if __name__ == '__main__':

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\EC601_Project1\ec601-project2-nlp-b125dc28fe61.json"
    entities_sentiment("I am so happy!")
