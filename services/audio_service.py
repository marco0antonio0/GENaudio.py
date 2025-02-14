import os
import uuid
import asyncio
from repositories.audio_repository import gerar_audio
from config.settings import AUDIO_DIR, VOICES, VELOCIDADES

import asyncio
from repositories.audio_repository import gerar_audio
from config.settings import VOICES, VELOCIDADES

def processar_audio(texto: str, voz_key: str, velocidade: str):
    """Processa o áudio e retorna os bytes do arquivo gerado."""
    if voz_key not in VOICES:
        raise ValueError(f"Voz inválida! Escolha entre: {', '.join(VOICES.keys())}")

    if velocidade not in VELOCIDADES:
        raise ValueError(f"Velocidade inválida! Escolha entre: {', '.join(VELOCIDADES)}")

    voz = VOICES[voz_key]

    # Executar a geração do áudio de forma assíncrona
    audio_bytes = asyncio.run(gerar_audio(texto, voz, velocidade))

    return audio_bytes



def listar_vozes():
    """Retorna todas as vozes disponíveis."""
    return VOICES


def listar_velocidades():
    """Retorna todas as velocidades disponíveis."""
    return VELOCIDADES
