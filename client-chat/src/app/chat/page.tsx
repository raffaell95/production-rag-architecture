"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import axios from "axios";
import ChatMessage from "./ChatMessage";
import ChatInput from "@/app/components/ChatInput";


type Message = {
  id: string;
  from: "user" | "bot";
  text: string;
};

type ChatResponse = {
  reply: string;
};


export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  const containerRef = useRef<HTMLDivElement | null>(null);
  const sessionId = useRef<string>(crypto.randomUUID());

  /* Auto Scroll */
  useEffect(() => {
    containerRef.current?.scrollTo({
      top: containerRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages]);

  /* Send Message */
  const sendMessage = useCallback(async (text: string) => {
    if (!text.trim()) return;

    const userMessage: Message = {
      id: crypto.randomUUID(),
      from: "user",
      text,
    };

    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await axios.post<ChatResponse>("/api/chat", {
        message: text,
        session_id: sessionId.current,
      });

      const botMessage: Message = {
        id: crypto.randomUUID(),
        from: "bot",
        text: response.data.reply,
      };

      setMessages((prev) => [...prev, botMessage]);

    } catch (error) {
      console.error("Erro ao enviar:", error);

      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          from: "bot",
          text: "Erro ao processar mensagem.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }, []);

  return (
    <div className="flex flex-col h-screen bg-gray-50">
        <div className="h-16 border-b bg-white flex items-center px-6 shadow-sm">
            <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center text-bl font-bold">
                SB
                </div>
                <div>
                <p className="font-semibold text-blue-500">SafeBank Assistente</p>
                <p className="text-xs text-green-500">Online</p>
                </div>
            </div>
        </div>
      <div
        ref={containerRef}
        className="flex-1 overflow-y-auto p-4 space-y-3"
      >
        {messages.map((msg) => (
          <ChatMessage key={msg.id} msg={msg} />
        ))}
      </div>

      {loading && (
        <div className="flex items-center gap-2 px-4 pb-2">
            <div className="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center text-sm">
            SB
            </div>

            <div className="bg-white border px-4 py-2 rounded-2xl rounded-bl-none">
            <div className="flex gap-1">
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-150"></span>
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-300"></span>
            </div>
            </div>
        </div>
    )}

      <ChatInput disabled={loading} onSend={sendMessage} />
    </div>
  );
}