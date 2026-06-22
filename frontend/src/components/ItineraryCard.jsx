function ItineraryCard({ day }) {

  return (
    <div className="bg-white rounded-xl shadow p-5">

      <h2 className="text-xl font-bold mb-4">

        Day {day.day}

      </h2>

      {day.image && (
      <img src={day.image} alt={day.title} className="w-full h-64 object-cover rounded-xlmb-4"/>
      )}

      <h3 className="font-semibold text-lg mb-4">

        {day.title}

      </h3>

      {day.activities.map(
        (activity, index) => (
          <div
            key={index}
            className="border-l-4 border-blue-500 pl-4 mb-5"
          >

            <h4 className="font-semibold">

              {activity.name}

            </h4>

            <p className="mt-2">

              {activity.description}

            </p>

            <div className="mt-2 text-sm text-gray-600">

              💡 {activity.tips}

            </div>

          </div>
        )
      )}

    </div>
  );
}

export default ItineraryCard;