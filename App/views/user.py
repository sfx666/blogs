from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user/')

@user.route('/register/')
def register():
    return "注册"

@user.route('/login/')
def login():
    return "登录"

