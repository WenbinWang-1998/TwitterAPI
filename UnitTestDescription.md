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





