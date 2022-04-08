from flask import Flask

class WebAPI:
    def __init__(self) -> None:
        self.run_app = self.init()

    def init(self) -> Flask:
        app = Flask(__name__, static_url_path="/public", static_folder="public")
        app.config["SECRET_KEY"] = "MYAPI123"

        from .views import views
        app.register_blueprint(views, url_prefix="/")

        from .controller import api_epidemic
        app.register_blueprint(api_epidemic, url_prefix="/epidemic")

        from .controller import api_vaccination
        app.register_blueprint(api_vaccination, url_prefix="/vaccination")

        from .controller import api_category
        app.register_blueprint(api_category, url_prefix="/category")

        return app