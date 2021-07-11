from app.db import db, ma 
from app.config import  DevelopmentConfig 
from flask import Flask
from app.store.views import home, dashboard
from flask_sqlalchemy import SQLAlchemy

ACTIVE_ENDPOINTS = [('/',home), ('/dashboard', dashboard) ]

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
   

    with app.app_context():
        db.create_all()

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    return app


if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run(debug=True)





