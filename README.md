# EC601-Project
Including wenbin wang's EC601 Project
## ABSTRACT
Twitter API: I use this API to get the user's all tweets and get all replys/remove all replys. This function can help me filter the tweets. 
Because if I want to judge whether the person is happy or not, reading his/her replys to other people is useless, we should focus on his or her own tweets.
Thus I write this function. 

Google NLP: I use Google NLP to get text's overall sentiment and analyze all entities in this sentence and get their sentiment separately.


## Part 1: Twitter API
### 1. Preparation
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
### 2. Put all the tweets into a json file
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
### Object in json file:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/GlanceTwitterContent.PNG)

### Tweet content:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/HelloWorld.PNG)

### 3. Extract the tweets are not replys

**Thirdly, it's the most important part. Because I want to get the users' emotion, so I have to remove all the tweets which are replys to other people. I need to
find the tweets from themselves instead. Here's an example: A friend of mine is so happy. So, I reply to him with positive words. But I am sad and I use some negative words in my own tweets. Something like this:**

### Only Tweets:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/OnlyTweets.PNG)
### Tweets and Reply:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/TweetsAndReply.PNG)

Thus, I need to find a way to get all of the tweets which are not replys and put them into a json file. I used the in_reply_to_status_id_str, the description in Twitter Developer Platform is: "Nullable. If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s ID." I used this attribute to judge if this tweets is a reply or not and put it into the json file. 	
Here's my function:
```
    #Get tweets which are not reply
    file=open('NotReplies','w')
    for tweet in tweets:
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id is None:
                replies=json.dumps(tweet._json)
                obj=json.loads(replies)
                json.dump(obj,file,indent=4,sort_keys=True)
    file.close()
```

## Part 2: Google NLP

### 1. Preparation
First of all, I downloaded the Google Cloud SDK from official website and I used the PyCharm to set up a project in the same path as SDK.
Then I download the credential json file to computer and add code, the "Path" should be substituted by the json file's path in my computer:
```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Path"
```
### 2. Analyze the overall sentiment of one sentence
Secondly, I used the language package from Google Cloud to write a simple test to analyze whether the sentiment in a sentence is positive or negative. Using language.LanguageServiceClient(), language.Document() and client.analyze_sentiment() to get the sentiment and use the percentage format to show the result :
```
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
```
### Result format by using PyCharm:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/NLP_Sentiment.PNG)

### 3. Analyze the entities sentiment
Finally, I wrote an entities_sentiment function to get the overall sentiment of multiple sentences and get the emotion from different people. 
```
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
 ```
### Result format by using PyCharm:
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/OverallSentiment.PNG)

