import { useState } from "react";
import { sendMessage } from "./services/api";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  Plane,
  MapPinned,
  Wallet,
  Compass,
} from "lucide-react";

function App() {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Welcome to TripPlanner! Ask me about destinations, itineraries, budgets, and attractions.",
    },
  ]);

  const handleSendMessage = async (text = message) => {
    if (!text.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const data = await sendMessage(text);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: data.reply,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Unable to connect to TripPlanner.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const examples = [
    "Plan a 3-day Goa trip",
    "Best places near Hyderabad",
    "Budget for Kerala trip",
    "Places to visit in monsoon",
  ];

  return (
    <div className="min-h-screen bg-linear-to-b from-sky-50 via-white to-slate-100 flex flex-col">
      {/* Header */}
      <header className="bg-white border-b shadow-sm">
        <div className="max-w-6xl mx-auto px-4 py-5">
          <h1 className="text-4xl font-bold">Trip Planner</h1>
          <p className="text-slate-600 mt-1">
                AI-powered travel planner for personalized itineraries, budgets, and destination recommendations.
          </p>
        </div>
      </header>

      {/* Main */}
      <main className="flex-1 max-w-6xl w-full mx-auto px-6 py-6">

  {/* Hero */}
  <div className="relative h-70 rounded-3xl overflow-hidden shadow-xl mb-8">
    <img
      src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
      alt="Travel"
      className="w-full h-full object-cover"
    />

    <div className="absolute inset-0 bg-black/50 flex items-center">
      <div className="px-10 text-white">
        <h1 className="text-6xl font-bold">
          Discover Your Next Adventure
        </h1>

        <p className="mt-4 text-xl max-w-2xl">
          Plan trips, estimate budgets, create itineraries & explore destinations with AI.
        </p>
      </div>
    </div>
  </div>

  {/* Feature Cards */}
  <div className="grid md:grid-cols-4 gap-5 mb-8">

    <div className="bg-white rounded-3xl p-6 shadow-lg">
      <Plane size={32} />
      <h3 className="font-bold mt-3">Trip Planning</h3>
      <p className="text-gray-500 text-sm mt-2">
        Generate complete travel plans.
      </p>
    </div>

    <div className="bg-white rounded-3xl p-6 shadow-lg">
      <MapPinned size={32} />
      <h3 className="font-bold mt-3">Destinations</h3>
      <p className="text-gray-500 text-sm mt-2">
        Discover amazing places.
      </p>
    </div>

    <div className="bg-white rounded-3xl p-6 shadow-lg">
      <Wallet size={32} />
      <h3 className="font-bold mt-3">Budget Estimator</h3>
      <p className="text-gray-500 text-sm mt-2">
        Calculate travel costs.
      </p>
    </div>

    <div className="bg-white rounded-3xl p-6 shadow-lg">
      <Compass size={32} />
      <h3 className="font-bold mt-3">Itineraries</h3>
      <p className="text-gray-500 text-sm mt-2">
        Day-by-day schedules.
      </p>
    </div>

  </div>

  {/* Example Questions */}
  <div className="bg-white rounded-3xl p-5 shadow-lg mb-6">

    <h2 className="font-bold text-xl mb-3">
      Example Questions
    </h2>

    <div className="flex flex-wrap gap-3">
      {examples.map((item) => (
        <button
          key={item}
          onClick={() => handleSendMessage(item)}
          className="px-4 py-2 rounded-full bg-sky-100 hover:bg-sky-200"
        >
          {item}
        </button>
      ))}
    </div>

  </div>

  {/* Chat Box */}
  <div className="bg-white rounded-3xl shadow-2xl p-6">

    <h2 className="font-bold text-xl mb-4">
      AI Travel Assistant
    </h2>

    <div className="h-100 overflow-y-auto space-y-4">

      {messages.map((msg, index) => (
        <div
          key={index}
          className={`flex ${
            msg.sender === "user"
              ? "justify-end"
              : "justify-start"
          }`}
        >
          <div
  className={`max-w-[75%] rounded-2xl px-4 py-3 ${
    msg.sender === "user"
      ? "bg-blue-600 text-white"
      : "bg-white border border-slate-200 shadow-sm"
  }`}
>
  {msg.sender === "bot" ? (
  <div className="prose prose-slate max-w-none">
    <ReactMarkdown
      remarkPlugins={[remarkGfm]}
      components={{
        h1: ({ children }) => (
          <h1 className="text-3xl font-bold mb-4">
            {children}
          </h1>
        ),
        h2: ({ children }) => (
          <h2 className="text-2xl font-semibold mb-3">
            {children}
          </h2>
        ),
        h3: ({ children }) => (
          <h3 className="text-xl font-semibold mb-2">
            {children}
          </h3>
        ),
        p: ({ children }) => (
          <p className="mb-4 leading-7">
            {children}
          </p>
        ),
        ul: ({ children }) => (
          <ul className="list-disc pl-5 mb-4">
            {children}
          </ul>
        ),
        ol: ({ children }) => (
          <ol className="list-decimal pl-5 mb-4">
            {children}
          </ol>
        ),
      }}
    >
      {msg.text}
    </ReactMarkdown>
  </div>
) : (
  msg.text
)}
</div>
        </div>
      ))}

      {loading && (
        <div className="text-slate-500">
          Planning your trip...
        </div>
      )}

    </div>

    <div className="mt-5 flex gap-3">

      <input
        type="text"
        value={message}
        placeholder="Ask about travel..."
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) =>
          e.key === "Enter" && handleSendMessage()
        }
        className="flex-1 border rounded-xl px-4 py-3"
      />

      <button
        onClick={() => handleSendMessage()}
        className="bg-blue-600 text-white px-6 rounded-xl"
      >
        Send
      </button>

    </div>

  </div>

</main>
      {/* Footer */}
      <footer className="text-center py-4 text-slate-500">
        Built by Raviteja | Built for GENAI Internship
      </footer>
    </div>
  );
}

export default App;