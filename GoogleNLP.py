#reference:https://drive.google.com/file/d/1dNahyZnwgqwUUdbV5I0u68b8pQADBiWi/view

import os
import tweepy
import json
from google.cloud import language

twitter_keys = {
        'consumer_key':        'g5KDHAfYfQVT7uONC3MpIJp3G',
        'consumer_secret':     '4td2zhOQmbKRKuqLaKKcixOVXY3Ps9tfKNJrH4y4DZxSCNgWVw',
        'access_token_key':    '1441140944279990275-8Et6DLwB8FAMqXcb5vFIqeHekaXKGw',
        'access_token_secret': 'gYMd0nwbMISfmAMq48TohUkZxjRnXR88m8du6ptBCE242'
    }




def get_all_tweets_and_reply(id):

    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)

    #新加代码
    # status = api.get_status(id, tweet_mode="extended")
    # print(status.text)

    #Get 200 tweets
    tweets = api.user_timeline(screen_name=id, count=200)

    file=open('myTwitterApi','w')
    #Put all tweets into a json file
    for tweet in tweets:
        string=json.dumps(tweet._json)
        obj=json.loads(string)
        json.dump(obj, file, indent=4, sort_keys=True)
    file.close()

    #Get tweets which are not reply
    file=open('NotReplies','w')
    for tweet in tweets:
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            # print('dfafsa',tweet.in_reply_to_status_id_str)
            # if (tweet.in_reply_to_status_id_str=='1442142917464780803'):
            if tweet.in_reply_to_status_id is None:
                replies=json.dumps(tweet._json)
                obj=json.loads(replies)
                json.dump(obj,file,indent=4,sort_keys=True)
    file.close()

    file=open('OwnText','w')
    for tweet in tweets:
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id is None:
                replies=json.dumps(tweet._json)
                obj=json.loads(replies)
                json.dump(obj["text"],file,indent=4,sort_keys=True)
                file.write('\n')

    file.close()

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
    #pass the username to the function, get all his/her tweets and get the replies
    # get_all_tweets_and_reply("@elonmusk")
    get_all_tweets_and_reply("@wwenbinbu")

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\EC601_Project1\ec601-project2-nlp-b125dc28fe61.json"
    # print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

    entities_sentiment("@parpitudelegend I am so glad you are so happy!")
