import os
from flask import Flask
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from api.v1 import api_v1_bp

def not_found(e):
    return '', 404

def create_app(environment_config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False # Make url without trailing slash work.
    app.config.from_object(environment_config)
    app.register_error_handler(404, not_found)
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    # TODO: Add config for database
    # from Model import db
    # db.init_app(app)

    return app


if __name__ == "__main__":
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    configs = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
    }
    app = create_app(configs.get(FLASK_ENV))
    app.run()
