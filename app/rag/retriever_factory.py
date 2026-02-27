from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.loaders.pdf_loader import PDFLoader
from app.embeddings.embedding_factory import EmbeddingFactory
from app.vectorstore.vectorstore_repository import VectorStoreRepository


class RetrieverFactory:

    DOCS_PATH: Path = Path("documents")

    @classmethod
    def create(cls) -> BaseRetriever:

        documents: List[Document] = PDFLoader.load_documents(cls.DOCS_PATH)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks: List[Document] = splitter.split_documents(documents)

        embeddings = EmbeddingFactory.create()

        repository = VectorStoreRepository()

        vectorstore = repository.get_or_create(
            chunks,
            embeddings
        )

        return vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 6, "fetch_k": 4}
        )