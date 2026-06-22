function BudgetCard({ budget, trip }) {

  const hasUserBudget =
    trip?.budget !== null &&
    trip?.budget !== undefined;

  return (
    <div className="bg-white rounded-xl shadow p-5">

      <h2 className="text-xl font-bold mb-4">
        💰 Budget Analysis
      </h2>

      {hasUserBudget && (
        <p>
          Budget Status:
          <span
            className={
              budget.sufficient
                ? "text-green-600 ml-2"
                : "text-red-600 ml-2"
            }
          >
            {budget.sufficient
              ? "Sufficient"
              : "Insufficient"}
          </span>
        </p>
      )}

      <p className="mt-2">
        Estimated Budget:
        ₹{budget.recommended_budget}
      </p>

      <div className="mt-3 p-3 bg-gray-100 rounded">
        {budget.reason}
      </div>

    </div>
  );
}

export default BudgetCard;