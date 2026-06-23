import { useState } from "react";

function Chat() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    try {
      const res = await fetch(
        "https://customer-care-ai-agent.onrender.com/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: message,
          }),
        }
      );

      const data = await res.json();

      setResponse(data.response);
    } catch (error) {
      console.error(error);
      setResponse("Error connecting to server");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Customer Chat</h1>

      <input
        type="text"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          width: "300px",
          padding: "10px",
          marginRight: "10px",
        }}
      />

      <button onClick={sendMessage}>
        Send
      </button>

      <h3>Response:</h3>
      <p>{response}</p>
    </div>
  );
}

export default Chat;