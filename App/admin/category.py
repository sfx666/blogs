# 版块管理
from flask import Blueprint

categroy = Blueprint('categroy', __name__, url_prefix='/admin/')

@categroy.route('/categroy/')
def index():
    return "模块管理"

