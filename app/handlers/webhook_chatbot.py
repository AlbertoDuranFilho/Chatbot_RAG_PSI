from fastapi import FastAPI, Request
# from llm import get_final_response
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "página inicial"}

# Endpoint para receber mensagens do Evolution
@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Mensagem recebida:", data) 
    user_message = data['data']['message']['conversation']
    print(user_message)
    user_number = data['data']['key']['remoteJid']
    print(user_number.split('@')[0])

    if data['data']['key']['fromMe'] == True:
        # Processar a intenção
        response = process_message(user_message)
        print(response)
        # Enviar resposta via API Evolution
        send_response(user_number.split('@')[0], response)
        return {"status": "success"}

def process_message(message):
    # Processamento básico
    if "consulta" in message:
        return "Gostaria de agendar uma consulta? Envie sua disponibilidade."
    elif "dúvida" in message:
        return "Por favor, envie sua pergunta e tentarei ajudar!"
    else:
        return "Não entendi. Poderia reformular sua mensagem?"

def send_response(number, message):
    evolution_api_url = os.getenv("EVOLUTION_API_URL")
    evolution_api_instance = os.getenv("EVOLUTION_API_INSTANCE")
    evolution_api_key = os.getenv("AUTHENTICATION_API_KEY")
    print(evolution_api_url)
    print(evolution_api_instance)
    print(evolution_api_key)

    route = f"{evolution_api_url}/message/sendText/{evolution_api_instance}"
    headers = {
        'Content-Type': 'application/json',
        'apikey': evolution_api_key
    }
    payload = {
        "number": number,
        "textMessage": {"text": message}
        
    }
    response = requests.post(route, json=payload, headers=headers)
    print(response)
    return response.json()