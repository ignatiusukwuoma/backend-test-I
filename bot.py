import os
import re
import tweepy
from dotenv import load_dotenv, find_dotenv
from sheet import SpreadSheet

load_dotenv(find_dotenv())

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


def initialize_api():
    """ Initializes the Tweepy API """

    if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        raise ValueError('Please provide all the required Twitter credentials')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


class TwitterlyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        """Called when a new status arrives"""

        screen_name = status.user.screen_name
        followers_count = status.user.followers_count

        twitter_bio = {'screen_name': screen_name, 'followers_count': followers_count}

        spreadsheet = SpreadSheet()
        sheet_name = os.getenv('SPREADSHEET_NAME')
        if not sheet_name:
            sheet_name = 'New spreadsheet'
        spreadsheet.write(sheet_name, twitter_bio)

        print('[x] Twitter Handle:', screen_name)
        print('[x] Number of Followers:', followers_count)
        print('=' * 80)


if __name__ == "__main__":
    user_entry = input("[+] Enter hashtag(s) to listen for, separated by space or comma: ")
    cleaned_entry = re.split('\W+', user_entry)
    hashtags = [f'#{entry}' for entry in cleaned_entry]

    if hashtags:
        api = initialize_api()
        myStreamListener = TwitterlyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        print(f'[-] Listening for tweets with hashtags {hashtags}')
        print('=' * 80)
        myStream.filter(track=hashtags)
