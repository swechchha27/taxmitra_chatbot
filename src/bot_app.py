#!/usr/bin/env python3
"""
Indian Income Tax Consultant Chatbot using Chatterbot.

This script creates a simple domain-specific chatbot named 'TaxMitra'
that provides basic income tax guidance to Indian citizens.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


class ChatBotApp:
    """
    A chatbot that provides basic guidance on Indian income tax matters.
    """
    def __init__(self, 
                 name="TaxMitra", 
                 training_file="../data/training_data.txt", 
                 db_uri="sqlite:///./storage/tax_db.sqlite3"):
        """
        Initialize the chatbot with a name and training data.

        :param name: The name of the chatbot (default: 'TaxMitra')
        :param training_file: The path to the file containing training data
                              (default: '../data/training_data.txt')
        :param db_uri: The URI of the database to store chatbot data
                       (default: 'sqlite:///./storage/tax_db.sqlite3')
        """
        self.name = name
        self.training_file = training_file
        self.database_uri = db_uri
        self.bot = ChatBot(
            name=name,
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri=db_uri
        )
        # Create a ListTrainer instance for the chatbot
        self.list_trainer = ListTrainer(self.bot)
        self.corpus_trainer = ChatterBotCorpusTrainer(self.bot)

    def train_with_corpus(self, corpus_name):
        """
        Train the chatbot with the specified corpus.
        
        :param corpus_name: The name of the corpus to train the chatbot with.
                            The available corpora are listed at:
                            https://chatterbot.readthedocs.io/en/stable/training.html
        """
        self.corpus_trainer.train(corpus_name)             

    def train_with_list(self, conversation_list):
        """
        Train the chatbot with a list of conversation pairs.
        
        :param conversation_list: A list of tuples where each tuple contains
                                  a question and its corresponding answer.
        """
        self.list_trainer.train(conversation_list)

    def train_with_file(self, file_path=None):
        """
        Train the chatbot with conversation data from a file.
        
        :param file_path: The path to the file containing conversation data.
                          The file should contain one statement per line.
        """
        if file_path is None:
            file_path = self.training_file
        with open(file_path, mode="r", encoding="utf-8") as file:
            conversation = file.read().split('\n')
            self.list_trainer.train(conversation)

    def train_with_paired_datafile(self, file_path=None):
        """
        Train the chatbot with custom paired conversation data from a file.
        
        :param file_path: The path to the file containing conversation data.
                          The file should contain one conversation pair per line,
                          separated by a tab character.
        """
        if file_path is None:
            file_path = self.training_file
        with open(file_path, encoding="utf-8", mode="r") as file:
            conversation = []
            for line in file.readlines():
                pair = line.strip().split('\t')
                if len(pair) == 2:
                    conversation.append(pair)
            for pair in conversation:
                self.list_trainer.train(pair)

    def start_chat(self):
        """
        Start an interactive chat session with the user.
        """
        exit_conditions = (":q", "quit", "exit")
        name = input("Enter your name: ")
        while True:
            try:
                query = input(f"> {name}: ")
                if query.lower() in exit_conditions:
                    print(f"{self.name}🧑🏻‍💻: Goodbye! Have a great day! 🌞")
                    break
                print(f"{self.name}🧑🏻‍💻: {self.bot.get_response(query)}")
            except (KeyboardInterrupt, EOFError, SystemExit):
                print(f"\n{self.name}🧑🏻‍💻: Goodbye! Have a great day! 🌞")
                break
