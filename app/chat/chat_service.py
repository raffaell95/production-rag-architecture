from langchain_core.messages import AIMessage, HumanMessage
from typing import List
import json

from app.core.config import settings
from app.core.redis_client import redis_client

class ChatService:
    def __init__(self, rag_chain):
        self.rag_chain = rag_chain

    def _key(self, session_id: str) -> str:
        return f"chat_history:{session_id}"

    def _save_message(self, session_id: str, sender: str, content):
        if not isinstance(content, str):
            if hasattr(content, "content"):
                content = content.content
            else:
                content = str(content)

        msg = json.dumps({"sender": sender, "content": content})
        redis_client.rpush(self._key(session_id), msg)
        redis_client.expire(self._key(session_id), settings.HISTORY_TTL)

    def _get_history(self, session_id: str, limit: int = 10) -> List[dict]:
        messages = redis_client.lrange(self._key(session_id), 0, -1)
        history = [json.loads(m) for m in messages]
        return history[-limit:] if limit else history

    def ask(self, session_id: str, question: str):
        self._save_message(session_id, "human", question)

        history = self._get_history(session_id)

        chat_history = []
        for m in history:
            if m["sender"] == "human":
                chat_history.append(HumanMessage(content=m["content"]))
            else:
                chat_history.append(AIMessage(content=m["content"]))

        response = self.rag_chain.invoke({
            "input": question,
            "chat_history": chat_history
        })

        if isinstance(response, dict):
            answer_text = response.get("answer") or response.get("input") or str(response)
        else:
            answer_text = str(response)

        self._save_message(session_id, "ai", answer_text)

        return answer_text