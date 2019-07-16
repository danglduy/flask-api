import os
from flask import Flask
from flask_migrate import Migrate
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from api.v1 import api_v1_bp
from api.database import db, ma

def not_found(e):
    return '', 404

FLASK_ENV = os.getenv('FLASK_ENV', 'production')
configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

app = Flask(__name__)
app.url_map.strict_slashes = False # Make url without trailing slash work.
app.config.from_object(configs.get(FLASK_ENV))
db.init_app(app)
ma.init_app(app)

app.register_error_handler(404, not_found)
app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
