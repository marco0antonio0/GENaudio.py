from flasgger import Swagger

def init_swagger(app):
    """Inicializa o Swagger apenas no ambiente de desenvolvimento."""
    from config.settings import FLASK_ENV

    if FLASK_ENV == "development":
        swagger_config = {
            "headers": [],
            "specs": [
                {
                    "endpoint": "apispec",
                    "route": "/apispec.json",
                    "rule_filter": lambda rule: True,
                    "model_filter": lambda tag: True,
                }
            ],
            "static_url_path": "/flasgger_static",
            "swagger_ui": True,
            "specs_route": "/docs/"
        }
        Swagger(app, config=swagger_config)
