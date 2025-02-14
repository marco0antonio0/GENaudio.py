# GENaudio.py 🎙️

GENaudio é uma API Flask que gera áudios a partir de textos utilizando **Edge-TTS** (Text-to-Speech da Microsoft).  
A API suporta diferentes vozes, velocidades e permite escolher entre **reprodução direta no navegador ou download do arquivo de áudio**.  

## 🚀 **Recursos**
✅ Geração de áudios usando Edge-TTS  
✅ Suporte a múltiplas vozes e velocidades  
✅ Escolha entre **reprodução no navegador** ou **download do áudio**  
✅ API documentada com **Swagger**  
✅ Configuração baseada em **variáveis de ambiente** (`.env`)  
✅ Docker e **Docker Compose** para fácil implantação  
✅ Código organizado em **Camadas (repositories-service-controller-config)** para melhor manutenção  

---

## 📌 **Estrutura do Projeto**
```
GENaudio/
├── main.py
├── controllers/
│   ├── __init__.py
│   ├── audio_controller.py
├── services/
│   ├── __init__.py
│   ├── audio_service.py
├── repositories/
│   ├── __init__.py
│   ├── audio_repository.py
├── modules/
│   ├── __init__.py
│   ├── swagger.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│── .env
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── README.md
```

---

## 📌 **Passo a Passo para Inicializar o Projeto**

### 🔹 **1️⃣ Clonar o Repositório**
```bash
git clone https://github.com/seu-usuario/genaudio.git
cd genaudio
```

### 🔹 **2️⃣ Criar e Ativar o Ambiente Virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 🔹 **3️⃣ Instalar as Dependências**
```bash
pip install -r requirements.txt
```

### 🔹 **4️⃣ Configurar as Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto e adicione:
```ini
FLASK_ENV=development
```

📌 **Opções para `FLASK_ENV`**:  
- `development` → Ativa o **Swagger UI**  
- `production` → **Desativa o Swagger** para uso em produção  

### 🔹 **5️⃣ Executar a API**
```bash
python app/main.py
```

### 🔹 **6️⃣ Acessar o Swagger**
Se o ambiente estiver como `development`, acesse:
```
http://localhost:5000/docs/
```

---

## 📌 **Uso da API**
### **1️⃣ Gerar um áudio (POST)**
- **Endpoint:** `/gerar-audio`
- **Exemplo de JSON para requisição:**
```json
{
  "texto": "Olá, este é um teste de áudio.",
  "voz": "antonio",
  "velocidade": "+10%",
  "modo": "play"
}
```
📌 **Opções de `modo`**  
- `"play"` → Reproduzir no navegador  
- `"download"` → Baixar o arquivo  

### **2️⃣ Listar vozes disponíveis (GET)**
- **Endpoint:** `/vozes-disponiveis`

**Resposta JSON:**
```json
{
  "vozes": {
    "antonio": "pt-BR-AntonioNeural",
    "francisca": "pt-BR-FranciscaNeural",
    "daniel": "pt-BR-DanielNeural",
    "maria": "pt-BR-MariaNeural"
  }
}
```

### **3️⃣ Listar velocidades disponíveis (GET)**
- **Endpoint:** `/velocidades-disponiveis`

**Resposta JSON:**
```json
{
  "velocidades": ["-50%", "-25%", "-10%", "0%", "+10%", "+25%", "+50%"]
}
```

---

## 📌 **Modo Docker (Opcional)**
Se quiser rodar a API dentro de um container Docker:  
```bash
docker-compose up --build -d
```

Para parar o container:
```bash
docker-compose down
```

---

## 📌 **Tecnologias Utilizadas**
- 🐍 **Python 3.10**  
- 🌐 **Flask**  
- 🎙️ **Edge-TTS (Text-to-Speech da Microsoft)**  
- 📄 **Swagger (Flasgger)**  
- 🐳 **Docker + Docker Compose**  
- 🔧 **Dotenv para variáveis de ambiente**  

---

## 📌 **Licença**
Este projeto é de código aberto e pode ser utilizado livremente.  

---

## 📌 **Autor**
👨‍💻 **Seu Nome**  
🔗 [LinkedIn](https://www.linkedin.com/in/seu-usuario/)  
🔗 [GitHub](https://github.com/seu-usuario/)  
