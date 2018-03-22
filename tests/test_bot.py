import unittest
from unittest.mock import patch

import tweepy

from bot import extract_tags, initialize_api, write_data


class TestBot(unittest.TestCase):
    """ Tests for the Bot """

    def test_tags_extracts_appropriately(self):
        entry = 'dev center , developers,nigeria'
        tag_list = ['#dev', '#center', '#developers', '#nigeria']
        tags = extract_tags(entry)
        self.assertListEqual(tags, tag_list)

    def test_tweepy_api_initialises(self):
        api = initialize_api()
        self.assertTrue(api)
        self.assertIs(type(api), tweepy.API)
