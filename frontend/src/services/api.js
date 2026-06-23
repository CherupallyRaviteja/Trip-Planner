const API_URL = "https://trip-planner-chatbot.onrender.com";

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

  if (!response.ok) {
    throw new Error("Failed to get response");
  }

  return await response.json();
}
