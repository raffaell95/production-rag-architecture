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
<img width="400" height="1536" alt="ChatGPT Image 27 de fev  de 2026, 01_20_54" src="https://github.com/user-attachments/assets/b6c2c0e1-97d4-4f62-9b52-5b2fd43875c3" />



## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

REDIS_HOST=localhost  
REDIS_PORT=6379  
REDIS_DB=0  
HISTORY_TTL=86400  
GROQ_API_KEY=<sua_chave_aqui>

## Como Rodar o Projeto
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




