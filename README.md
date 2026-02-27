# Production RAG Architecture - Atendimento Cliente

Este projeto é uma implementação de um **sistema de atendimento automatizado** utilizando **RAG (Retrieval-Augmented Generation)** com armazenamento de histórico em **Redis** e integração com **LLM (Groq Llama 3.3)**.  

O exemplo aqui considera um **LLM especializado em atendimento de clientes de um banco**, capaz de responder dúvidas sobre contas, transações e serviços financeiros.  

---

## Tecnologias Utilizadas

- **Backend**
  - Python 3.13
  - FastAPI (API REST)
  - LangChain / RAG para integração com LLM
  - Redis (armazenamento de histórico)
  - Pydantic (validação de dados)
  
- **Infraestrutura**
  - Docker / Docker Compose (para Redis)
  - `.env` para variáveis de ambiente

---

## Estrutura do Projeto
├── app/
│   ├── api/         # Controllers / rotas da API
│   ├── chat/        # ChatService para gerenciamento de histórico e interação com RAG
│   ├── core/        # Configurações, cliente Redis, variáveis de ambiente
│   ├── embeddings/  # Funções para criação e persistência de embeddings
│   ├── vectorstore/ # Armazenamento, indexação e consulta de embeddings
│   ├── llm/         # Factory para criação do LLM
│   ├── loaders/     # Loaders de documentos (PDF, texto, etc.) para indexação
│   ├── rag/         # RAGBuilder, Retriever e serviços de integração
|   ├── utils/       # Utilitários gerais (funções de logging, parsing, helpers)
│   └── main.py      # Entry point da API FastAPI
│
├── documents/       # PDFs ou documentos usados pelo RAG
├── storage/         # Persistência de dados, arquivos processados, backups do vectorstore
├── .env             # Variáveis de ambiente (não commitar)
└── requirements.txt # Dependências Python


## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

- Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
HISTORY_TTL=86400
GROQ_API_KEY=<sua_chave_aqui>

## Variáveis de Ambiente
Backend (FastAPI + Redis)

- Instale dependências:
`pip install -r requirements.txt`
Ou
`uv sync`

- Inicie o Redis (local ou via Docker Compose):
`docker-compose up -d`

- Execute a API FastAPI:
`python -m app.main`
Ou
`uv run -m app.main`
