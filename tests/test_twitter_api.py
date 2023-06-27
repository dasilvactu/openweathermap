# -*- coding: utf-8 -*-
import unittest, os
import tweepy
from dotenv import load_dotenv

class ApiTwitterPostTweet((unittest.TestCase)):
    
    def setUp(self):
        load_dotenv()
        
    def test_if_credentials_are_not_valid(self):
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        with self.assertRaisesRegex(Exception, '401 Unauthorized'):
            client.get_compliance_jobs(type = 'MARCUSVINI87122')
    def test_if_post_tweet_success(self):
       
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        try:
            client.create_tweet(text='teste 2')
        except Exception as e:
            self.fail(f"Error: {str(e)}")

    def test_if_post_tweet_is_not_success(self):
       
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        with self.assertRaisesRegex(Exception, '403 Forbidden'):
            client.create_tweet(text='teste 2')

if __name__ == '__main__':
    unittest.main()