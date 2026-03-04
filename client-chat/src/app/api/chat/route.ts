import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { message, session_id } = await req.json();

    if (!message) {
      return NextResponse.json(
        { error: "Mensagem é obrigatória" },
        { status: 400 }
      );
    }

    const res = await fetch(`${process.env.RAG_API_BASE_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
        session_id: session_id ?? "web-session-default",
      }),
    });

    if (!res.ok) {
      const errorText = await res.text();
      console.error("Erro backend:", errorText);
      return NextResponse.json(
        { error: "Erro no backend RAG" },
        { status: 500 }
      );
    }

    const data = await res.json();

    // 👇 Adapter aqui
    return NextResponse.json({
      reply: data.answer ?? "Sem resposta",
    });

  } catch (error) {
    console.error("Erro interno:", error);
    return NextResponse.json(
      { error: "Erro interno no servidor" },
      { status: 500 }
    );
  }
}