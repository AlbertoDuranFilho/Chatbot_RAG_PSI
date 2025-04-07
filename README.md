# 🤖 Chatbot RAG para Psicólogos

Assistente virtual via WhatsApp, integrado à API Evolution, com capacidade de:
- Realizar atendimentos iniciais automatizados
- Agendar consultas psicológicas
- Aplicar uma anamnese personalizada
- Gerar resumos e análises com GPT via RAG (Retrieval-Augmented Generation)
- Armazenar e organizar dados em painel web para os psicólogos

---

## 🚀 Tecnologias utilizadas

-  Python
-  React
-  OpenAI GPT (via API)
-  LangChain
-  ChromaDB ou Weaviate (banco vetorial)
-  Redis (memória conversacional)
-  PostgreSQL (armazenamento persistente)
-  Docker 
-  API Evolution (integração WhatsApp)
-  Django ou FastAPI (backend e painel web)

---

## 📂 Estrutura do Projeto
```
chatbot-rag/ 
├── app/ 
│ ├── main.py # Ponto de entrada 
│ ├── handlers/ # Lida com mensagens do WhatsApp 
│ ├── services/ # Lógica de agendamento, anamnese, etc. 
│ ├── rag/ # Configuração do LLM e banco vetorial 
│ ├── memory/ # Integração com Redis 
│ ├── db/ # Conexão e modelos com PostgreSQL 
│ ├── utils/ # Funções auxiliares 
│ └── config/ # Variáveis de ambiente e setup 
├── docs/ # Diagramas, fluxos, exemplos 
│ ├── anamnese.json 
│ └── fluxograma.png 
├── .env.example # Exemplo de variáveis para configurar 
├── requirements.txt 
├── docker-compose.yml 
├── todo.md # Planejamento semanal com checklist 
└── README.md
```

## 🧪 Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/seunome/chatbot-rag.git
cd chatbot-rag
```

2. Configure o .env:
```bash
cp .env.example .env # Edite com suas chaves da API Evolution e OpenAI
```

3. Instale as dependências (se não estiver usando Docker):
```bash
pip install -r requirements.txt
```

4. Inicie os serviços com Docker:
```bash
docker-compose up
```

## 🧠 Anamnese

O fluxo da anamnese segue uma lista de perguntas definidas em [docs/anamnese.json](docs/anamnese.json). As respostas são armazenadas no PostgreSQL, associadas ao número do usuário.

## 📊 Painel Web (em desenvolvimento)
O painel permitirá que psicólogos acessem:

- Histórico de pacientes

- Respostas da anamnese

- Agendamentos pendentes

## 📅 Cronograma e progresso

Você pode acompanhar o progresso semanal no arquivo [todo.md](./todo.md) do projeto.

## 📸 Exemplos e fluxogramas
Veja o fluxo da conversa no WhatsApp no diretório [/docs](./docs/).

## 📄 Licença
Este projeto é livre para fins de estudo e pesquisa.
Consulte o autor antes de utilizá-lo comercialmente.

## ✍️ Autor
Alberto Janeiro Duran Filho
Desenvolvedor Python com foco em IA aplicada à saúde e educação.
[LinkedIn](https://www.linkedin.com/in/alberto-janeiro) | [GitHub](https://github.com/AlbertoDuranFilho)

