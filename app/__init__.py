from db import db, ma 
from config import  DevelopmentConfig 
from flask import Flask
from store.views import home, dashboard
from flask_sqlalchemy import SQLAlchemy

ACTIVE_ENDPOINTS = [('/',home), ('/dashboard', dashboard) ]






if __name__ == "__main__":
    
    app = Flask(__name__)
    app.jinja_env.trim_blocks = True
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():   #el contexto es la DB, el serializable 
        db.create_all()

    for url,  blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    db = SQLAlchemy(app)
    app.run(debug=True)