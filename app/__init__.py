from config import  DevelopmentConfig 
from flask import Flask
from store.views import home
from flask_sqlalchemy import SQLAlchemy

ACTIVE_ENDPOINTS = [('/',home) ]






if __name__ == "__main__":
    
    app = Flask(__name__)
    app.jinja_env.trim_blocks = True
    app.config.from_object(DevelopmentConfig)
    for url,  blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    db = SQLAlchemy(app)
    app.run(debug=True)