# main.py
from config import config
from searchtweet import searchtweet


# setting
conf = config.Config()
st = searchtweet.SearchTweet(
    consumer_key=conf.get("CONSUMER_KEY"),
    consumer_secret=conf.get("CONSUMER_SECRET"),
    access_token=conf.get("ACCESS_TOKEN"),
    access_token_secret=conf.get("ACCESS_TOKEN_SECRET")
)

# get
tweet_list = st.get_home_timeline()
# tweet_list = st.get_user_timeline("TwitterDev")

# output
for tweet in tweet_list:
    print(tweet.user_name + "(@" + tweet.user_account + ")\n" + tweet.text)
    print("==========================================================================================")
