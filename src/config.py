import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """Base configuration for the application."""
    BOT_NAME = os.getenv('BOT_NAME', 'TaxMitra')
    DATABASE_URI = os.getenv('DATABASE_URL')
    TRAINING_FILE = os.getenv('TRAINING_FILE')
    
class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URL', Config.DATABASE_URI)
    TRAINING_FILE = os.getenv('DEV_TRAINING_FILE', Config.TRAINING_FILE)
    
class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    DATABASE_URI = os.getenv('TEST_DATABASE_URL', Config.DATABASE_URI)
    TRAINING_FILE = os.getenv('TEST_TRAINING_FILE', Config.TRAINING_FILE)

class ProductionConfig(Config):
    """Configuration for production environment."""
    DEBUG = False
    DATABASE_URI = os.getenv('DATABASE_URL', Config.DATABASE_URI)
    TRAINING_FILE = os.getenv('TRAINING_FILE', Config.TRAINING_FILE)

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
