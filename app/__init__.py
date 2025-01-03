import os
from flask import Flask, render_template
from flask_login import LoginManager
from config import DevelopmentConfig, ProductionConfig
from .models.user_models import User


def create_app():
    app = Flask(__name__)
    
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Register blueprints
    from app.views.main import main
    from app.views.admin import admin
    app.register_blueprint(main)
    app.register_blueprint(admin)

    # Error handler for 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # Error handler for 500 (optional)
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500
  
    return app
