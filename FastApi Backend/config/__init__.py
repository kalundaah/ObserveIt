import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_dev_key")
    SEND_FILE_MAX_AGE_DEFAULT = 300
    TIMEOUT = 90

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    FLASK_DEBUG = True
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    DEVELOPMENT = False
    FLASK_DEBUG = False
    TESTING = False
    DEBUG = False