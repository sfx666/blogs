class BaseConfig:
    Debug = False

    SECRET_KEY = 'dadlaidn-lija-134h-d153d-add153a-ds'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(BaseConfig):
    Debug = True

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/py07"

class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/py07"

Config = {
    'default': BaseConfig,
    'develop': DevelopConfig,
    'product': ProductConfig
}