from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from langchain_community.vectorstores import FAISS


class VectorStoreRepository:

    STORAGE_PATH: Path = Path("storage/vectorstore")
    INDEX_FILE: Path = STORAGE_PATH / "index.faiss"

    def create(
        self,
        documents: List[Document],
        embeddings: Embeddings
    ) -> VectorStore:

        vectorstore = FAISS.from_documents(documents, embeddings)

        self.STORAGE_PATH.mkdir(parents=True, exist_ok=True)
        vectorstore.save_local(str(self.STORAGE_PATH))

        return vectorstore

    def load(
        self,
        embeddings: Embeddings
    ) -> VectorStore:

        return FAISS.load_local(
            str(self.STORAGE_PATH),
            embeddings,
            allow_dangerous_deserialization=True
        )

    def exists(self) -> bool:
        return self.INDEX_FILE.exists()

    def get_or_create(
        self,
        documents: List[Document],
        embeddings: Embeddings
    ) -> VectorStore:

        if self.exists():
            return self.load(embeddings)

        return self.create(documents, embeddings)