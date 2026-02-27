from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingFactory:

    @staticmethod
    def create(model_name: str = "BAAI/bge-m3"):
        return HuggingFaceEmbeddings(model_name=model_name)