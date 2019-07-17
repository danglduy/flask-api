import os

class Config(object):
    DB_HOST = os.getenv('FLASK_APP_DB_HOST', 'localhost')
    DB_PORT = os.getenv('FLASK_APP_DB_PORT', 3306)
    DB_NAME = os.getenv('FLASK_APP_DB_NAME', 'flask')
    DB_USERNAME = os.getenv('FLASK_APP_DB_USERNAME', 'root')
    DB_PASSWORD = os.getenv('FLASK_APP_DB_PASSWORD', '')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass
