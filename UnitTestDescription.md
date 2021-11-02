# TwitterAPI UnitTest

## 1. Preparation
You need to use the code below to install the environment:
```
pip install nose
```

## 2. Unit Test 

I use the code listed below to find the error name. I used variable errorTypeAccepter as a record to record the ErrorName. 
```
    except Exception as e:
        err = type(e).__name__
        errorTypeAccepter = err
        print("ErrorName: " + err)
```

Until now, I found three ways to make the TwitterAPI's input invalid.  

First of all, if at least one variables in consumer_key, consumer_secret, access_token_key, access_token_secret are not exist, it will lead to Unauthorized Error.  

Secondly, if at least one of the variables are null, it will lead to BadRequest Error.  

Finally, if the id you input does not exist, that will lead to NotFound Error.  

Based on that, I used the try except statement in Python to catch the errorType and use a variable to save it.
When you use the Unit Test. You can pass the test if any of error is showed.

## 3. Actions

After that, I used Actions in Github and wrote main.yml to run the Unit test automatically when you push or pull request. Also, I used the secret key, so that you can run in the Github and don't need to run in your own laptop.





