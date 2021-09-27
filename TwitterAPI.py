#reference:https://drive.google.com/file/d/1dNahyZnwgqwUUdbV5I0u68b8pQADBiWi/view

import tweepy
import json


twitter_keys = {
        'consumer_key':        'Enter consumer key here',
        'consumer_secret':     'Enter consumer secret here',
        'access_token_key':    'Enter access token key here',
        'access_token_secret': 'Enter access token secret here'
    }

def get_all_tweets_and_reply(id):
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)

    #Get 200 tweets
    tweets = api.user_timeline(screen_name="@elonmusk", count=200)

    file=open('myTwitterApi','w')
    #Put all tweets into a json file
    for tweet in tweets:
        string=json.dumps(tweet._json)
        obj=json.loads(string)
        json.dump(obj, file, indent=4, sort_keys=True)
    file.close()

    #Get tweets which are reply
    file=open('Replies','w')
    for tweet in tweets:
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            # print('dfafsa',tweet.in_reply_to_status_id_str)
            # if (tweet.in_reply_to_status_id_str=='1442142917464780803'):
            if tweet.in_reply_to_status_id is None:
                replies=json.dumps(tweet._json)
                obj=json.loads(replies)
                json.dump(obj,file,indent=4,sort_keys=True)
    file.close()




if __name__ == '__main__':
    #pass the username to the function, get all his/her tweets and get the replies tweets, say @elonmusk
    get_all_tweets_and_reply("@elonmusk")

