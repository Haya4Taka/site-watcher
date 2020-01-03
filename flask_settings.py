class Config(object):
    """Base configuration."""

class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False

class DevConfig(Config):
    ENV = 'development'
    # コードに変更を加えると自動でサーバーを再起動させる
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'db_name': 'site-watcher_development'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    ENV = 'test'
    TESTING = True
    DEBUG = True