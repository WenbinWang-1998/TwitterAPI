#reference1 : https://cloud.google.com/natural-language/docs/quickstart-client-libraries
#reference2 : https://cloud.google.com/natural-language/docs/analyzing-entity-sentiment
#reference3 : https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
import os
import tweepy
import json
from google.cloud import language


twitter_keys = {
        'consumer_key':        '',
        'consumer_secret':     '',
        'access_token_key':    '',
        'access_token_secret': ''
    }



def get_all_tweets_and_reply(id):

    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
    #Get 200 tweets
    tweets = api.user_timeline(screen_name=id, count=1)

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

    #Get tweets which are not reply's text
    string = ""
    file=open('OwnText','w')
    for tweet in tweets:
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id is None:
                replies=json.dumps(tweet._json)
                obj=json.loads(replies)
                json.dump(obj["text"],file,indent=4,sort_keys=True)
                string = string + json.dumps(obj["text"])
                file.write('\n')
    file.close()
    return string

#Get the entities' sentiment
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

#Analyze one sentence's sentiment
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

    twitter_keys['consumer_key'] = input("Please Enter the Consumer Key: ")
    twitter_keys['consumer_secret'] = input("Please Enter the Consumer Secret: ")
    twitter_keys['access_token_key'] = input("Please Enter the Token Key: ")
    twitter_keys['access_token_secret'] = input("Please Enter the Token Secret: ")
    id = input('Please Enter the UserId: ')
    credential_path = input("Google_Application_Crendentials: ")

    # You can use my Twitter as an example
    # get_all_tweets_and_reply("@wwenbinbu")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
    entities_sentiment(get_all_tweets_and_reply(id) )
    entities_sentiment(get_all_tweets_and_reply('@wwenbinbu') )
