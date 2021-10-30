#reference:https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet

import tweepy
import json


twitter_keys = {
        'consumer_key':        'Enter consumer key here',
        'consumer_secret':     'Enter consumer secret here',
        'access_token_key':    'Enter access token key here',
        'access_token_secret': 'Enter access token secret here'
    }

# Get top 200 tweets from the user and save them into myTwitterApi.json and save the non-reply tweets into NotReplies.json
errorTypeAccepter = ''
def get_all_tweets_and_reply(id):
    global errorTypeAccepter
    try:
        auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
        auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
        api = tweepy.API(auth)
        #Get 200 tweets
        tweets = api.user_timeline(screen_name=id, count=200)
    except Exception as e:
        err = type(e).__name__
        errorTypeAccepter = err
        print("ErrorName: " + err)

    else:   
        try:
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
        except Exception as e:
            err = type(e).__name__
            errorTypeAccepter = err
            print("ErrorName: " + err)


if __name__ == '__main__':
    #pass the username to the function, get all his/her tweets and get the replies
    # get_all_tweets_and_reply("@elonmusk")
    get_all_tweets_and_reply("@wwenbinbu")


