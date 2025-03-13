import unittest
import os
import json
from src.bot_app import ChatBotApp
from src.config import SelectedConfig as conf

class TestChatBotApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load the test training data before running tests"""
        cls.bot_app = ChatBotApp('TestBot', conf.TRAINING_FILE, conf.DATABASE_URI)
        # Train the chatbot with data from training file
        cls.bot_app.train_with_paired_datafile()
        # Train the chatbot based on the English corpus
        cls.bot_app.train_with_corpus('chatterbot.corpus.english')
    
    @classmethod
    def tearDownClass(cls):
        # Clean up code, e.g., delete the test database
        if os.path.exists(conf.DATABASE_URI):
            os.remove(conf.DATABASE_URI)

    def test_response(self):
        """Check if the bot gives a valid response"""
        response = self.bot_app.bot.get_response("What is income tax?")
        self.assertIsNotNone(response)
        self.assertIn("tax", response.text.lower().split())

    def test_greeting(self):
        response = self.bot_app.bot.get_response("Hello")
        self.assertIsNotNone(response)
        self.assertTrue("hello" in response.text.lower() or "hi" in response.text.lower())

    # def test_farewell(self):
    #     response = self.bot_app.bot.get_response("Goodbye")
    #     self.assertIsNotNone(response)
    #     self.assertIn("goodbye", response.text.lower())

if __name__ == '__main__':
    unittest.main()