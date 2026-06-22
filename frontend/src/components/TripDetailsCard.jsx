function TripDetailsCard({ trip }) {
  if (!trip) return null;
  return (
    <div className="bg-white rounded-xl shadow p-5">

      <h2 className="text-xl font-bold mb-4">
        📍 Trip Summary
      </h2>

      <div className="grid grid-cols-2 gap-4">

        <div>
          <p className="text-gray-500">
            Destination
          </p>
          <p className="font-semibold">
            {trip.destination}
          </p>
        </div>

        <div>
          <p className="text-gray-500">
            Duration
          </p>
          <p className="font-semibold">
            {trip.duration_days} Days
          </p>
        </div>

        <div>
          <p className="text-gray-500">
            Budget
          </p>
          <p className="font-semibold">
            ₹{trip.budget}
          </p>
        </div>

        <div>
          <p className="text-gray-500">
            Companions
          </p>
          <p className="font-semibold">
            {trip.companions}
          </p>
        </div>

      </div>

    </div>
  );
}

export default TripDetailsCard;