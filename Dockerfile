# Usa a imagem oficial do Python
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o container
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 para acesso à API
EXPOSE 5000

# Define a variável de ambiente para desativar o buffer de saída
ENV PYTHONUNBUFFERED=1

# Comando para rodar a aplicação
CMD ["python", "main.py"]
