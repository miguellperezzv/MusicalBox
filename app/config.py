import os

UPLOAD_FOLDER = os.path.abspath("./uploads/")
DB_URI = "TBD"

class Config(object):
    DEBUG = True
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    # OJO: PARA CUANDO TRABAJE EN MEMORIA   SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:" 
    #SQLALCHEMY_DATABASE_URI = "sqlite:///musicalbox.sqlite3"
    SQLALCHEMY_DATABASE_URI = "sqlite:///musicalboxPRUEBA.sqlite3"
    #SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER

    

class ProductionConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY", 123456)
    SQLALCHEMY_DATABASE_URI = DB_URI

class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    FLASK_ENV='development'
    DEBUG=True
    SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'