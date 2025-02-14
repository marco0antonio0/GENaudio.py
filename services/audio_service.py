import os
import uuid  # ✅ Adicionado para corrigir o erro
import asyncio
from repositories.audio_repository import gerar_audio
from config.settings import AUDIO_DIR, VOICES, VELOCIDADES

def processar_audio(texto: str, voz_key: str, velocidade: str, modo: str):
    """Processa o áudio e retorna o caminho do arquivo gerado."""
    if voz_key not in VOICES:
        raise ValueError(f"Voz inválida! Escolha entre: {', '.join(VOICES.keys())}")

    if velocidade not in VELOCIDADES:
        raise ValueError(f"Velocidade inválida! Escolha entre: {', '.join(VELOCIDADES)}")

    voz = VOICES[voz_key]
    filename = f"{AUDIO_DIR}/audio_{uuid.uuid4().hex}.mp3"  # ✅ Agora o UUID está definido corretamente

    # Executar a geração do áudio de forma assíncrona
    asyncio.run(gerar_audio(texto, filename, voz, velocidade))

    return filename, modo
