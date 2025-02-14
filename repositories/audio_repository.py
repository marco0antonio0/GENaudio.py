import edge_tts
import asyncio
import io
import os
import uuid

async def gerar_audio(texto: str, voz: str, velocidade: str):
    """Função assíncrona para gerar áudio e armazenar em memória."""
    temp_filename = f"/tmp/audio_{uuid.uuid4().hex}.mp3"

    # Gerar áudio e salvar temporariamente
    communicate = edge_tts.Communicate(texto, voice=voz, rate=velocidade)
    await communicate.save(temp_filename)

    # Ler o áudio gerado para a memória
    with open(temp_filename, "rb") as f:
        audio_bytes = io.BytesIO(f.read())

    # Remover o arquivo temporário
    os.remove(temp_filename)

    # Retornar o cursor para o início do buffer
    audio_bytes.seek(0)
    return audio_bytes
