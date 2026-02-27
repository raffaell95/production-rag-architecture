from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader


class PDFLoader:

    @staticmethod
    def load_documents(path: str | Path):
        path = Path(path)

        documents = []

        if path.is_file():
            loader = PyMuPDFLoader(str(path))
            documents.extend(loader.load())

        elif path.is_dir():
            for pdf_file in path.glob("*.pdf"):
                loader = PyMuPDFLoader(str(pdf_file))
                documents.extend(loader.load())

        else:
            raise ValueError(f"Caminho inválido: {path}")

        return documents