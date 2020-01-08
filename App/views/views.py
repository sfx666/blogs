from flask import Blueprint

bbs = Blueprint('categroy', __name__, url_prefix='/')

@bbs.route('/')
def index():
    return "这是首页"

