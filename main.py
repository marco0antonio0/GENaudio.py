from flask import Flask
from flask_cors import CORS
from controllers.audio_controller import audio_bp
from modules.swagger import init_swagger
from config.settings import FLASK_ENV

app = Flask(__name__)
CORS(app)

# Inicializa o Swagger apenas em ambiente de desenvolvimento
init_swagger(app)

# Registra os blueprints (controllers)
app.register_blueprint(audio_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=(FLASK_ENV == "development"))
