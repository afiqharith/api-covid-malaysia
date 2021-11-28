from flask import Flask

class MOH_WebAPI:
    def __init__(self) -> None:
        self.run_app = self.init()

    def init(self) -> Flask:
        app = Flask(__name__)
        app.config["SECRET_KEY"] = "MYAPI123"

        from .views import views
        app.register_blueprint(views, url_prefix="/")

        from .api_epidemic import api_epidemic
        app.register_blueprint(api_epidemic, url_prefix="/epidemic")

        from .api_vaccination import api_vaccination
        app.register_blueprint(api_vaccination, url_prefix="/vaccine")

        from .api_category import api_category
        app.register_blueprint(api_category, url_prefix="/category")

        return app