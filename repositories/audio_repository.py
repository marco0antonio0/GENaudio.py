import edge_tts
import asyncio
import io
import os
import uuid

async def gerar_audio(texto: str, voz: str, velocidade: str):
    """Função assíncrona para gerar áudio e armazenar em memória."""

    # Substituições de pausas para Edge TTS (simulando com pontuação e espaços)
    pausas = {
        "<pausa-curta/>": "..., ",  # Pequena pausa usando reticências e espaço
        "<pausa-media/>": "... ... ",  # Pausa média com mais espaços
        "<pausa-longa/>": "... ... ... "  # Pausa longa com mais pontos
    }

    # Substituir todas as tags personalizadas pelo texto simulando pausas naturais
    for tag, pausa_texto in pausas.items():
        texto = texto.replace(tag, pausa_texto)

    # Criar o nome do arquivo temporário
    temp_filename = f"/tmp/audio_{uuid.uuid4().hex}.mp3"

    # Gerar áudio sem SSML, apenas com texto puro
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
