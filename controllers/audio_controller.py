from flask import Blueprint, request, jsonify, send_file
from flasgger import swag_from
from services.audio_service import processar_audio, listar_vozes, listar_velocidades
from config.settings import VOICES, VELOCIDADES

audio_bp = Blueprint("audio", __name__)

@audio_bp.route("/gerar-audio", methods=["POST"])
@swag_from({
    "tags": ["Áudio"],
    "summary": "Gera um áudio a partir de um texto e retorna para reprodução ou download",
    "description": "Este endpoint gera um áudio a partir do texto informado, podendo incluir pausas customizadas.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "texto": {
                        "type": "string",
                        "example": "Olá! Este é um teste <pausa-curta/> de áudio. Agora uma pausa maior <pausa-media/> e uma bem longa <pausa-longa/> antes do fim.",
                        "description": (
                            "Texto que será convertido em áudio. Você pode incluir pausas personalizadas no texto:\n"
                            "- `<pausa-curta/>`: Pequena pausa (~0,5s)\n"
                            "- `<pausa-media/>`: Pausa média (~1s)\n"
                            "- `<pausa-longa/>`: Pausa longa (~2s)\n"
                        )
                    },
                    "voz": {
                        "type": "string",
                        "enum": list(VOICES.keys()),
                        "example": "antonio"
                    },
                    "velocidade": {
                        "type": "string",
                        "enum": VELOCIDADES,
                        "example": "+10%"
                    },
                    "modo": {
                        "type": "string",
                        "enum": ["play", "download"],
                        "example": "download"
                    }
                },
                "required": ["texto"]
            }
        }
    ],
    "responses": {
        200: {
            "description": "Áudio gerado com sucesso.",
            "content": {
                "audio/mpeg": {
                    "schema": {
                        "type": "string",
                        "format": "binary"
                    }
                }
            }
        },
        400: {
            "description": "Erro na requisição (ex: campo obrigatório ausente)."
        }
    }
})
def gerar_audio():
    """Endpoint para gerar áudio sem persistência e retornar para reprodução ou download."""
    data = request.json
    texto = data.get("texto")
    voz_key = data.get("voz", "antonio").lower()
    velocidade = data.get("velocidade", "0%")
    modo = data.get("modo", "donwload").lower()

    if not texto:
        return jsonify({"erro": "O campo 'texto' é obrigatório!"}), 400

    try:
        audio_bytes = processar_audio(texto, voz_key, velocidade)
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    return send_file(audio_bytes, mimetype="audio/mpeg") if modo == "play" else send_file(audio_bytes, as_attachment=True, download_name="audio.mp3")


@audio_bp.route("/listar-vozes", methods=["GET"])
@swag_from({
    "tags": ["Áudio"],
    "summary": "Lista todas as vozes disponíveis",
    "description": "Retorna uma lista das vozes disponíveis para geração de áudio.",
    "responses": {
        200: {
            "description": "Lista de vozes disponíveis",
            "schema": {
                "type": "object",
                "properties": {
                    "vozes": {"type": "object"}
                }
            }
        }
    }
})
def get_vozes():
    """Endpoint para listar todas as vozes disponíveis."""
    return jsonify({"vozes": listar_vozes()})


@audio_bp.route("/listar-velocidades", methods=["GET"])
@swag_from({
    "tags": ["Áudio"],
    "summary": "Lista todas as velocidades disponíveis",
    "description": "Retorna uma lista das velocidades permitidas para ajuste da fala.",
    "responses": {
        200: {
            "description": "Lista de velocidades disponíveis",
            "schema": {
                "type": "object",
                "properties": {
                    "velocidades": {"type": "array", "items": {"type": "string"}}
                }
            }
        }
    }
})
def get_velocidades():
    """Endpoint para listar todas as velocidades disponíveis."""
    return jsonify({"velocidades": listar_velocidades()})
