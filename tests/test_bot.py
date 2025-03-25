"""
Unit tests for the ChatBotApp class.

This module contains unit tests for the ChatBotApp class, which is responsible for
handling chatbot interactions. The tests are designed to ensure that the chatbot
responds correctly to various inputs and that the training data is loaded and used
properly.

Classes:
    TestChatBotApp: A unittest.TestCase subclass that contains tests for the ChatBotApp class.
"""

import unittest
import os
# import json
from taxmitra.bot_app import ChatBotApp
from taxmitra.config import SelectedConfig as conf


class TestChatBotApp(unittest.TestCase):
    """
    A unittest.TestCase subclass that contains tests for the ChatBotApp class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Class method that initializes the ChatBotApp instance and trains it with
        the provided training data and corpus.
        """
        cls.bot_app = ChatBotApp('TestBot', conf.TRAINING_FILE, conf.DATABASE_URI)
        # Train the chatbot with data from training file
        cls.bot_app.train_with_paired_datafile()
        # Train the chatbot based on the English corpus
        cls.bot_app.train_with_corpus('chatterbot.corpus.english')

    @classmethod
    def tearDownClass(cls):
        """
        Class method that cleans up resources, such as deleting the test database.
        """
        # Clean up code, e.g., delete the test database
        if os.path.exists(conf.DATABASE_URI):
            os.remove(conf.DATABASE_URI)

    def test_response(self):
        """
        Test method that checks if the bot gives a valid response to a tax-related query.
        """
        response = self.bot_app.bot.get_response("What is income tax?")
        self.assertIsNotNone(response)
        self.assertIn("tax", response.text.lower().split())

    def test_greeting(self):
        """
        Test method that checks if the bot responds correctly to a greeting.
        """
        response = self.bot_app.bot.get_response("Hello")
        self.assertIsNotNone(response)
        self.assertTrue("hello" in response.text.lower() or "hi" in response.text.lower())

    # def test_farewell(self):
    #     """
    #     Test method that checks if the bot responds correctly to a farewell.
    #     """
    #     response = self.bot_app.bot.get_response("Goodbye")
    #     self.assertIsNotNone(response)
    #     self.assertIn("goodbye", response.text.lower())

if __name__ == '__main__':
    unittest.main()
