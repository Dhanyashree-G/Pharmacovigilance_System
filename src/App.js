import { BrowserRouter, Routes, Route } from "react-router-dom";
import FollowUp from "./FollowUp";
import Dashboard from "./Dashboard";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/f/:token" element={<FollowUp />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}
