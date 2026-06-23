import { useEffect, useState } from "react";

function Admin() {
  const [stats, setStats] = useState(null);
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/admin/stats")
      .then((res) => res.json())
      .then((data) => setStats(data));

    fetch("http://127.0.0.1:8000/admin/tickets")
      .then((res) => res.json())
      .then((data) => setTickets(data));
  }, []);

  if (!stats) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <h2 className="text-2xl focsnt-bold">Loading Dashboard...</h2>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-4xl font-bold mb-8">
        Admin Dashboard
      </h1>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold">
            Total Orders
          </h2>
          <p className="text-3xl mt-2">
            {stats.total_orders}
          </p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold">
            Total Tickets
          </h2>
          <p className="text-3xl mt-2">
            {stats.total_tickets}
          </p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold">
            Open Tickets
          </h2>
          <p className="text-3xl mt-2">
            {stats.open_tickets}
          </p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold">
            Escalated Tickets
          </h2>
          <p className="text-3xl mt-2">
            {stats.escalated_tickets}
          </p>
        </div>

      </div>

      {/* Tickets Table */}
      <div className="bg-white mt-8 p-6 rounded-lg shadow">

        <h2 className="text-2xl font-bold mb-4">
          Recent Tickets
        </h2>

        <table className="w-full border-collapse border border-gray-300">

          <thead>
            <tr className="bg-gray-100">
              <th className="border p-2">ID</th>
              <th className="border p-2">Message</th>
              <th className="border p-2">Priority</th>
              <th className="border p-2">Status</th>
            </tr>
          </thead>

          <tbody>
            {tickets.map((ticket) => (
              <tr key={ticket.id}>
                <td className="border p-2">
                  {ticket.id}
                </td>

                <td className="border p-2">
                  {ticket.message}
                </td>

                <td className="border p-2">
                  {ticket.priority}
                </td>

                <td className="border p-2">
                  {ticket.status}
                </td>
              </tr>
            ))}
          </tbody>

        </table>

      </div>
    </div>
  );
}

export default Admin;