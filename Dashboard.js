import React, { useState } from "react";

function Dashboard() {
  const [result, setResult] = useState(null);

  const calculateSIP = async () => {
    const res = await fetch("http://127.0.0.1:8000/sip?amount=5000&rate=12&years=10");
    const data = await res.json();
    setResult(data.future_value);
  };

  return (
    <div>
      <h2>SIP Calculator</h2>
      <button onClick={calculateSIP}>Calculate</button>
      {result && <p>Future Value: ₹{result}</p>}
    </div>
  );
}

export default Dashboard;
