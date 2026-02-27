from app.llm.llm_factory import LLMFactory
from app.rag.retriever_factory import RetrieverFactory
from app.rag.rag_builder import RAGBuilder
from app.chat.chat_service import ChatService

class RAGService:

    @staticmethod
    def create():
        llm = LLMFactory.create(
            provider="groq",
            model="llama-3.3-70b-versatile",
            temperature=0.7
        )

        retriever = RetrieverFactory.create()

        rag_chain = RAGBuilder.build(llm, retriever)

        return ChatService(rag_chain)