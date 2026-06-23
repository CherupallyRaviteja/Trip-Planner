import TripDetailsCard from "./TripDetailsCard";
import WeatherCard from "./WeatherCard";
import BudgetCard from "./BudgetCard";
import ItineraryCard from "./ItineraryCard";

function ResponseRenderer({ data }) {
  if (!data) return null;
  if (data.message) {

  return (
      <div className="bg-yellow-50 border border-yellow-300 rounded-xl p-4">

        <p className="text-yellow-800">
          {data.message}
        </p>

      </div>
    );
  }
  return (
    <div className="space-y-6 mt-6">

      <TripDetailsCard
        trip={data.trip_details}
      />

      <WeatherCard
        weather={data.weather}
        advice={data.weather_advice}
      />

      <BudgetCard
        budget={data.budget_analysis}
        trip={data.trip_details}
      />

      <div className="space-y-8">
      {data.itinerary?.map((day) => (
        <ItineraryCard
          key={day.day}
          day={day}
        />
      ))}
    </div>

    </div>
  );
}

export default ResponseRenderer;