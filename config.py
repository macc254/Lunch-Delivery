import os
class Config:

    # simple mail transfer protocol server configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='Madetowin'
    #PHOTOS DESTINATION

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://francis:Master@localhost/lunchdelivery'


    Debug = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://francis:Master@localhost/lunch_test'



#configuration options
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
    '''
    General configuration parent class
    '''
    SECRET_KEY='Madetowin'

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2015@localhost/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Blog'
    SENDER_EMAIL = 'cherotichm23@gmail.com'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod 
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2015@localhost/blogs_test'
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2015@localhost/lunchdelivery'
    DEBUG = True


 
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig


}