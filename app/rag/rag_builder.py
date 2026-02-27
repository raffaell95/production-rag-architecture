from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains.history_aware_retriever import create_history_aware_retriever
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


class RAGBuilder:

    @staticmethod
    def build(llm, retriever):

        reformulation_prompt = ChatPromptTemplate.from_messages([
            ("system", "Reformule a pergunta considerando o histórico."),
            MessagesPlaceholder("chat_history"),
            ("human", "Pergunta: {input}")
        ])

        history_retriever = create_history_aware_retriever(
            llm=llm,
            retriever=retriever,
            prompt=reformulation_prompt
        )

        qa_prompt = ChatPromptTemplate.from_messages([
            ("system",
             """Você é um assistente virtual.
             Use o contexto para responder.
             Se não souber, diga que não sabe.
             Responda em português."""
             ),
            MessagesPlaceholder("chat_history"),
            ("human", "Pergunta: {input}\n\nContexto: {context}")
        ])

        qa_chain = create_stuff_documents_chain(llm, qa_prompt)

        return create_retrieval_chain(history_retriever, qa_chain)