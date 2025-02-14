import edge_tts
import asyncio

async def gerar_audio(texto: str, output_file: str, voz: str, velocidade: str):
    """Função assíncrona para gerar áudio usando Edge-TTS."""
    communicate = edge_tts.Communicate(texto, voice=voz, rate=velocidade)
    await communicate.save(output_file)
