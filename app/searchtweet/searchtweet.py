# searchtweet.py
import json

from requests_oauthlib import OAuth1Session

from . import tweetdata

# const
TWITTER_API_URL_PREFIX = "https://api.twitter.com/1.1/"


# SearchTweet class
class SearchTweet:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self._twitter_oauth = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

    def _request(self, url, params, log=False):
        request = self._twitter_oauth.get(url, params=params)
        if log:
            print(request.url)

        if request.status_code != 200:
            print("Error : Http Status Code " + request.status_code)
            return None
        return json.loads(request.text)

    def get_home_timeline(self, count=50, exclude_replies=False):
        # url
        url = TWITTER_API_URL_PREFIX + "statuses/home_timeline.json"

        # params
        params = dict()
        params.setdefault("count", count)
        params.setdefault("exclude_replies", exclude_replies)

        # request
        timeline = self._request(url, params, log=True)
        if timeline is None:
            print("Error : Not get home timeline")
            return None

        # convert
        return [tweetdata.TweetData(user_name=tweet["user"]["name"],
                                    user_account=tweet["user"]["screen_name"],
                                    text=tweet["text"]) for tweet in timeline]

    def get_user_timeline(self, screen_name, count=50, exclude_replies=False, include_rts=True):
        # url
        url = TWITTER_API_URL_PREFIX + "statuses/user_timeline.json"

        # params
        params = dict()
        params.setdefault("screen_name", screen_name)
        params.setdefault("count", count)
        params.setdefault("exclude_replies", exclude_replies)
        params.setdefault("include_rts", include_rts)

        # request
        timeline = self._request(url, params, log=True)
        if timeline is None:
            print("Error : Not get user timeline")
            return None

        # convert
        return [tweetdata.TweetData(user_name=tweet["user"]["name"],
                                    user_account=tweet["user"]["screen_name"],
                                    text=tweet["text"]) for tweet in timeline]
