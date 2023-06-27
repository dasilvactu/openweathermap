# -*- coding: utf-8 -*-
import unittest, os
from controllers.TweetController import TweetController
from dotenv import load_dotenv

class TweetControllerApi((unittest.TestCase)):
    def setUp(self):
        load_dotenv()
        
    def test_if_post_tweet_success(self):
        client = TweetController()
        try:
            client.publish_tweet(text='twwet novo')
        except Exception as e:
            self.fail(f"Error: {str(e)}")
    def test_if_post_tweet_is_not_success(self):
        client = TweetController()
        with self.assertRaisesRegex(Exception, '403 Forbidden'):
            client.publish_tweet(text='stringddddddd')
if __name__ == '__main__':
    unittest.main()