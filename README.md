# EC601-Project
Including wenbin wang's EC601 Project
## ABSTRACT
Twitter API: I use this API to get the user's all tweets and get all replys/remove all replys. This function can help me filter the tweets. 
Because if I want to judge whether the person is happy or not, reading his/her replys to other people is useless, we should focus on his or her own tweets.
Thus I write this function. 

Google NLP: I use Google NLP to get text's overall sentiment and analyze all entities in this sentence and get their sentiment separately.


### Part 1: Twitter API
First of all, I use package tweepy's api.user_timeline to get 200 of statuses sent from the user. Then I put them all into the "myTwitterApi.json" to get the result. 
Using my twitter as an example, if I update a tweet which the content is Hello World! Here's the result :
![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/GlanceTwitterContent.PNG)
                            **Picture 1**

![image](https://github.com/WenbinWang-1998/TwitterAPI/blob/main/Image/HelloWorld.PNG)
                            **Picture 2**
