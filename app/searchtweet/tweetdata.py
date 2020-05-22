# tweetdata.py
from datetime import datetime


# TweetData class
class TweetData:

    def __init__(self, user_name="", user_account="", date="", text=""):
        self.user_name = user_name
        self.user_account = user_account
        # date_format "Thu Apr 06 15:28:43 +0000 2017"
        self.date = datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y") if date else None
        self.text = text

    def __repr__(self):
        return "TweetDate[" \
                + "user_name:" + self.user_name + ", " \
                + "user_account:" + self.user_account + ", " \
                + "date:" + (self.date.strftime("%Y-%m-%d %H:%M:%S") if self.date is not None else "None") + ", " \
                + "text:" + self.text \
                + "]"

    def __str__(self):
        return self.user_name \
                + "(@" + self.user_account + ")" \
                + (self.date.strftime("%Y-%m-%d %H:%M:%S") if self.date is not None else "") \
                + "\n" \
                + self.text
