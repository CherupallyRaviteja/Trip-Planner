function WeatherCard({weather,advice}) 
{
  if (!weather) return null;
  return (
    <div className="bg-white rounded-xl shadow p-5">

      <h2 className="text-xl font-bold mb-4">
        ☀ Weather
      </h2>

      <div className="grid grid-cols-4 gap-4">

        <div>
          <p>
            {weather?.temperature ?? "Unavailable"}
          </p>
        </div>

        <div>
          <p>{weather.condition || "Unavailable"}</p>
        </div>

        <div>
          <p>{weather.humidity}%</p>
        </div>

        <div>
          <p>{weather.wind_speed} m/s</p>
        </div>

      </div>

      <div className="mt-4 p-3 bg-blue-50 rounded">

        <p>{advice}</p>

      </div>

    </div>
  );
}

export default WeatherCard;