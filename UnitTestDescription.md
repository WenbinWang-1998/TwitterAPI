# TwitterAPI UnitTest
I use the code listed below to find the error name. I used variable errorTypeAccepter as a record to record the ErrorName. 
'''
    except Exception as e:
        err = type(e).__name__
        errorTypeAccepter = err
        print("ErrorName: " + err)
'''

Until now, I found three ways to make the TwitterAPI's input invalid.
First of all, if at least one variables in consumer_key, consumer_secret, access_token_key, access_token_secret are not exist, it will lead to Unauthorized Error.
Secondly, if at least one of the variables are null, it will lead to BadRequest Error.
Thirdly, if the id you input does not exist, that will lead to NotFound Error.
