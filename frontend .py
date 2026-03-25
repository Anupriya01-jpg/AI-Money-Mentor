import React from "react";
import Dashboard from "./components/Dashboard";
import ChatUI from "./components/ChatUI";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>💰 AI Money Mentor</h1>
      <Dashboard />
      <ChatUI />
    </div>
  );
}

export default App;
