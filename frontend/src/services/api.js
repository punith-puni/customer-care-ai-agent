const API_URL = "http://127.0.0.1:8000";
const [loading, setLoading] = useState(false);
export async function sendMessage(message) {
  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });

  return response.json();
}