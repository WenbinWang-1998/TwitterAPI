import os
import tweepy
import json

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token_key = os.getenv('ACCESS_TOKEN_KEY')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

errorTypeAccepter = ''
def get_tweets(id):
    global errorTypeAccepter
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=id, count=1)
    except Exception as e:
        err = type(e).__name__
        errorTypeAccepter = err

    else:
        try:
            file=open('myTwitterApi','w')
            for tweet in tweets:
                string=json.dumps(tweet._json)
                obj=json.loads(string)
                json.dump(obj, file, indent=4, sort_keys=True)
            file.close()
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
        except Exception as e:
            err = type(e).__name__
            errorTypeAccepter = err

def notFound_error(id):
    global errorTypeAccepter
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=id, count=200)

    except Exception as e:
        err = type(e).__name__
        errorTypeAccepter = err
        return errorTypeAccepter
    else:
        try:
            file=open('myTwitterApi','w')
            for tweet in tweets:
                string=json.dumps(tweet._json)
                obj=json.loads(string)
                json.dump(obj, file, indent=4, sort_keys=True)
            file.close()
            file=open('NotReplies','w')
            for tweet in tweets:
                if hasattr(tweet, 'in_reply_to_status_id_str'):
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
        except Exception as e:
            err = type(e).__name__
            errorTypeAccepter = err


if __name__ == '__main__':
    print(notFound_error('dfasdfadsfsdaf'))
