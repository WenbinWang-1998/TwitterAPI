import TwitterAPI as TAPI
from pytest import approx

def test_userid():
    TAPI.get_all_tweets_and_reply("Please Enter the id you want to test")
    assert TAPI.errorTypeAccepter == 'Unauthorized' or 'BadRequest' or 'NotFound'


if __name__ == 'UnitTest':

    test_userid()
