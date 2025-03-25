"""
This module initializes and runs the ChatBotApp.

The ChatBotApp is trained with paired data from a file and the English corpus.
It then starts an interactive chat session with the user.
"""

# import os
# import json
from taxmitra.config import SelectedConfig as conf
from taxmitra.bot_app import ChatBotApp

if __name__ == "__main__":
    try:
        # Initialize chatbot application with the selected configuration
        bot_app = ChatBotApp(
            name = conf.BOT_NAME,
            training_file = conf.TRAINING_FILE,
            db_uri = conf.DATABASE_URI,
        )

        # Example training data
        # bot_app.train_with_list([
        #     "Hi",
        #     "Welcome, friend 🤗",
        # ])
        # bot_app.train_with_list([
        #     "Are you a plant?",
        #     "No, I'm the pot below the plant!",
        # ])

        # Train the chatbot with data from a file
        bot_app.train_with_paired_datafile()

        # Train the chatbot with data from a JSON file
        # with open(TRAINING_FILE, mode="r", encoding="utf-8") as file:
        #     training_data = json.load(file)
        #     for pair in training_data:
        #         bot_app.train_with_list(pair)

        # For more information about available corpora, visit:
        # https://github.com/gunthercox/chatterbot-corpus/blob/master/readme.md
        bot_app.train_with_corpus('chatterbot.corpus.english')
        # Start the chat session to interact with the chatbot
        bot_app.start_chat()
    except (FileNotFoundError, ImportError) as e:
        print(f"An error occurred while running the ChatBotApp: {e}")
        print(conf.DATABASE_URI)