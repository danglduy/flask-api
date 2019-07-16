import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass
