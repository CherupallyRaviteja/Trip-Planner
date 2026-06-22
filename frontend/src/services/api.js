const API_URL = "http://127.0.0.1:8000";

export async function sendMessage(
  message,
  userId
) {

  const response = await fetch(
    `${API_URL}/chat`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },

      body: JSON.stringify({
        message,
        user_id: userId
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to get response"
    );
  }

  return await response.json();
}