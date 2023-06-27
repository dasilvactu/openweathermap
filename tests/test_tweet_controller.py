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
            client.publish_tweet(text='teste 2')
        except Exception as e:
            self.fail(f"Error: {str(e)}")
if __name__ == '__main__':
    unittest.main()