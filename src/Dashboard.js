import axios from "axios";
import { useEffect, useState } from "react";

export default function Dashboard() {
  const [cases, setCases] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/dashboard", {
      headers: { Authorization: "Bearer TOKEN" }
    }).then(res => setCases(res.data));
  }, []);

  return (
    <table>
      <tr><th>Case</th><th>Risk</th><th>Status</th></tr>
      {cases.map(c =>
        <tr key={c.case_id}>
          <td>{c.case_id}</td>
          <td>{c.risk_level}</td>
          <td>{c.status}</td>
        </tr>
      )}
    </table>
  );
}
