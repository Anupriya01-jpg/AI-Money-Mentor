import React, { useState } from "react";

function ChatUI() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://127.0.0.1:8000/advisor", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div>
      <h2>AI Advisor</h2>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask about investing..."
      />
      <button onClick={sendMessage}>Send</button>
      {response && <p><b>AI:</b> {response}</p>}
    </div>
  );
}

export default ChatUI;
