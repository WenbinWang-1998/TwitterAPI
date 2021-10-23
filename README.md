# EC601-Project
Including wenbin wang's EC601 Project
## ABSTRACT
Twitter API: I use this API to get the user's all tweets and get all replys/remove all replys. This function can help me filter the tweets. 
Because if I want to judge whether the person is happy or not, reading his/her replys to other people is useless, we should focus on his or her own tweets.
Thus I write this function. 

Google NLP: I use Google NLP to get text's overall sentiment and analyze all entities in this sentence and get their sentiment separately.


## Part 1: Twitter API
First of all, we have to get the permission of Twitter API by adding consumer key, access key, etc. Here's what we should use:

```
twitter_keys = {
        'consumer_key':        'Enter consumer key here',
        'consumer_secret':     'Enter consumer secret here',
        'access_token_key':    'Enter access token key here',
        'access_token_secret': 'Enter access token secret here'
    }
```
Using this as key to execute the Twitter API by using tweepy.OAuthHandler function:
```
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
```
Secondly, I use package tweepy's api.user_timeline to get 200 of statuses sent from the user. Then I put them all into the "myTwitterApi.json" to get the result. 
Here's the code:
```
    tweets = api.user_timeline(screen_name=id, count=200)

    file=open('myTwitterApi','w')
    #Put all tweets into a json file
    for tweet in tweets:
        string=json.dumps(tweet._json)
        obj=json.loads(string)
        json.dump(obj, file, indent=4, sort_keys=True)
    file.close()
```
Using my twitter as an example, if I update a tweet which the content is Hello World! Noticing the text part in the json file. Here's the result :
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/GlanceTwitterContent.PNG)
**Picture 1**

![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/HelloWorld.PNG)
**Picture 2**

Thirdly, **it's the most important part**. Because I want to get the users' emotion, so I have to remove all the tweets which are replys to other people. I need to
find the tweets from themselves instead. Here's an example: A friend of mine is so happy. So, I reply to him with positive words. But I am sad and I use some negative words in my own tweets. Something like this:

### Only Tweets:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/OnlyTweets.PNG)
### Tweets and Reply:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/TweetsAndReply.PNG)


