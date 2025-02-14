import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Configurações gerais
FLASK_ENV = os.getenv("FLASK_ENV", "development")
AUDIO_DIR = "audios"

# Criar a pasta para armazenar os áudios, se não existir
os.makedirs(AUDIO_DIR, exist_ok=True)

# Configurações de vozes disponíveis
VOICES = {
    "antonio": "pt-BR-AntonioNeural",
    "francisca": "pt-BR-FranciscaNeural",
    "daniel": "pt-BR-DanielNeural",
    "maria": "pt-BR-MariaNeural"
}

# Velocidades permitidas
VELOCIDADES = ["-50%", "-25%", "-10%", "0%", "+10%", "+25%", "+50%"]
