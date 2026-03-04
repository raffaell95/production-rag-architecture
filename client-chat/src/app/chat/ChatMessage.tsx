type Props = {
  msg: {
    from: "user" | "bot";
    text: string;
  };
};

export default function ChatMessage({ msg }: Props) {
  const isUser = msg.from === "user";

  return (
    <div className={`flex items-end gap-2 ${isUser ? "justify-end" : "justify-start"}`}>
      
      {/* Avatar Bot */}
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center text-sm">
          SB
        </div>
      )}

      {/* Bubble */}
      <div
        className={`max-w-[70%] p-3 rounded-2xl text-sm ${
          isUser
            ? "bg-blue-600 text-white rounded-br-none"
            : "bg-white border text-gray-800 rounded-bl-none"
        }`}
      >
        {msg.text}
      </div>

      {/* Avatar User */}
      {isUser && (
        <div className="w-8 h-8 rounded-full bg-gray-400 text-white flex items-center justify-center text-sm">
          EU
        </div>
      )}
    </div>
  );
}