from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.rag_service import RAGService

router = APIRouter()
rag = RAGService.create()


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Endpoint FastAPI para chat com histórico Redis.
    """
    response = rag.ask(request.session_id, request.message)

    return ChatResponse(answer=response)