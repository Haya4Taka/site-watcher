from flask import Flask
from flask_migrate import Migrate
from flask_settings import DevConfig
================ここをrestから独立させる========
from src.rest.property import property_module
from src.rest.user import user_module
=============================================
================ここをsqlalchemy()に変更=======
from src.domain.model import db
=============================================
================ここを読みこむ場所を他のファイルかもっと遅くする==
import src.domain.model
=============================================

modules = [
    property_module,
    user_module
]

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    for module in modules:
        app.register_blueprint(module)
    db.init_app(app)
    Migrate(app, db)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5001)
