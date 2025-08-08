
# settings.py - Configuration management for NewsBot 2.0

# General Settings
PROJECT_NAME = "NewsBot Intelligence System 2.0"
VERSION = "1.0"
AUTHOR = "Kaden Glover"
GROUP_NAME = "KGMY"

# Data Paths
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
MODEL_PATH = "data/models/"
RESULTS_PATH = "data/results/"

# NLP Configuration
LANGUAGE_MODEL = "en_core_web_sm"
NUM_TOPICS = 10
SUMMARY_LENGTH = 3

# Translation Settings
DEFAULT_SOURCE_LANG = "auto"
DEFAULT_TARGET_LANG = "en"

# API Configs (to be overridden by actual api_keys.py file if available)
NEWS_API_KEY = "your_news_api_key_here"
# Configuration settings for NewsBot 2.0
