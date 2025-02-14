from flask import Blueprint, request, jsonify, send_file
from flasgger import swag_from
from services.audio_service import processar_audio
from config.settings import VOICES, VELOCIDADES

audio_bp = Blueprint("audio", __name__)

@audio_bp.route("/gerar-audio", methods=["POST"])
@swag_from({
    "tags": ["Áudio"],
    "summary": "Gera um áudio a partir de um texto e retorna para reprodução ou download",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "texto": {"type": "string", "example": "Olá! Este é um teste de áudio."},
                    "voz": {"type": "string", "enum": list(VOICES.keys()), "example": "antonio"},
                    "velocidade": {"type": "string", "enum": VELOCIDADES, "example": "+10%"},
                    "modo": {"type": "string", "enum": ["play", "download"], "example": "play"}
                },
                "required": ["texto"]
            }
        }
    ]
})
def gerar_audio():
    """Endpoint para gerar áudio e retornar para reprodução ou download."""
    data = request.json
    texto = data.get("texto")
    voz_key = data.get("voz", "antonio").lower()
    velocidade = data.get("velocidade", "0%")
    modo = data.get("modo", "play").lower()

    if not texto:
        return jsonify({"erro": "O campo 'texto' é obrigatório!"}), 400

    try:
        filename, modo = processar_audio(texto, voz_key, velocidade, modo)
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    return send_file(filename, mimetype="audio/mpeg") if modo == "play" else send_file(filename, as_attachment=True)
