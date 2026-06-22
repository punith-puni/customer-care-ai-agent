import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Chat from "./pages/Chat";
import Admin from "./pages/Admin";

function App() {
  return (
    <BrowserRouter>
      <nav className="bg-blue-600 text-white p-4 flex gap-4">
        <Link to="/">Chat</Link>
        <Link to="/admin">Admin Dashboard</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Chat />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;