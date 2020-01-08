from App.admin.category import categroy


def register_blueprint(app):
    app.register_blueprint(categroy)