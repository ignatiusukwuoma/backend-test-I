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


def write_data(data):
    """
    Write data to Google Sheets
    :param data: obj. The data to be written to Google Sheets
    """

    spreadsheet = SpreadSheet()
    sheet_name = os.getenv('SPREADSHEET_NAME')
    if not sheet_name:
        sheet_name = 'New spreadsheet'
    spreadsheet.write(sheet_name, data)


def persist_bio(screen_name, followers_count):
    """
    Calls the function to write data to Spreadsheet
    only if the number of followers is between 1000 and 50000
    :param screen_name: str. Profile name of the user
    :param followers_count: int. Number of followers
    """
    if 1000 <= followers_count <= 50000:
        twitter_bio = {'screen_name': screen_name, 'followers_count': followers_count}
        write_data(twitter_bio)


def initialize_api():
    """
    Initializes the Tweepy API
    :return: class. tweepy.API
    """

    if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        raise ValueError('Please provide all the required Twitter credentials')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


def extract_tags(entry):
    """
    Extracts hashtags from user entry
    :param entry: str. User entry
    :return tags: list. Hashtags
    """
    cleaned_entry = re.split('\W+', entry)
    tags = [f'#{entry}' for entry in cleaned_entry]
    return tags


class TwitterlyStreamListener(tweepy.StreamListener):
    """ Twitter Stream listener """

    def on_status(self, status):
        """
        Called when a new status arrives
        :param status: A tweet that meets the condition
        that our stream is listening for.
        """

        screen_name = status.user.screen_name
        followers_count = status.user.followers_count
        persist_bio(screen_name, followers_count)

        print('[x] Twitter Handle:', screen_name)
        print('[x] Number of Followers:', followers_count)
        print('=' * 80)


if __name__ == "__main__":
    user_entry = input("[+] Enter hashtag(s) to listen for, separated by space or comma: ")
    hashtags = extract_tags(user_entry)
    if hashtags:
        api = initialize_api()
        myStreamListener = TwitterlyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        print(f'[-] Listening for tweets with hashtags {hashtags}')
        print('=' * 80)
        myStream.filter(track=hashtags)
