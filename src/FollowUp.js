import axios from "axios";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

export default function FollowUp() {
  const { token } = useParams();
  const [fields, setFields] = useState([]);
  const [answers, setAnswers] = useState({});

  useEffect(() => {
    axios.get(`http://localhost:8000/followup/${token}`)
      .then(res => setFields(res.data.fields));
  }, []);

  const submit = () => {
    axios.post(`http://localhost:8000/followup/${token}`, answers);
    alert("Submitted");
  };

  return (
    <div>
      {fields.map(f =>
        <input key={f} placeholder={f}
          onChange={e => setAnswers({...answers,[f]:e.target.value})}/>
      )}
      <button onClick={submit}>Submit</button>
    </div>
  );
}
