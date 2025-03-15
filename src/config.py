"""
This module provides configuration classes for different environments 
(development, testing, and production)
and loads environment variables from a .env file using the `dotenv` package.

Classes:
    Config: Base configuration class with default settings.
    DevelopmentConfig: Configuration class for the development environment.
    TestingConfig: Configuration class for the testing environment.
    ProductionConfig: Configuration class for the production environment.

Attributes:
    config_by_name (dict): A dictionary mapping environment names ('dev', 'test', 'prod') 
                           to their respective configuration classes.
    ENV (str): The current environment mode, defaulting to 'prod' if not set 
               in environment variables.
    SelectedConfig (Config): The configuration class selected based on the current environment mode.
"""

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """Base configuration for the application."""
    BOT_NAME = os.getenv('BOT_NAME', 'TaxMitra')
    DATABASE_URI = os.getenv('DATABASE_URL')
    TRAINING_FILE = os.getenv('TRAINING_FILE')

    def get_bot_name(self):
        """Return the bot name."""
        return self.BOT_NAME

    def get_database_uri(self):
        """Return the database URI."""
        return self.DATABASE_URI

class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URL', Config.DATABASE_URI)
    TRAINING_FILE = os.getenv('DEV_TRAINING_FILE', Config.TRAINING_FILE)

    def get_bot_name(self):
        return super().get_bot_name() + " Dev"

    def get_database_uri(self):
        return super().get_database_uri()

class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    DATABASE_URI = os.getenv('TEST_DATABASE_URL', Config.DATABASE_URI)
    TRAINING_FILE = os.getenv('TEST_TRAINING_FILE', Config.TRAINING_FILE)

    def get_bot_name(self):
        return super().get_bot_name() + " Test"

    def get_database_uri(self):
        return super().get_database_uri()

class ProductionConfig(Config):
    """Configuration for production environment."""
    DEBUG = False
    DATABASE_URI = os.getenv('DATABASE_URL', Config.DATABASE_URI)
    TRAINING_FILE = os.getenv('TRAINING_FILE', Config.TRAINING_FILE)

    def get_bot_name(self):
        return super().get_bot_name() + " Prod"

    def get_database_uri(self):
        return super().get_database_uri()

# Dictionary to map environment names to their respective configurations
config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}

# Get the environment mode (default: 'prod')
ENV = os.getenv("ENV", "prod")
# Select the appropriate configuration based on the environment mode
SelectedConfig = config_by_name[ENV]
