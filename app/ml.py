import random

def generate_recommendations(user_id):
    recommendations = [
        "Consider increasing your savings by 5% of your income.",
        "Look into diversifying your investment portfolio.",
        "Try to reduce your monthly expenses by cutting unnecessary subscriptions.",
        "Set up an emergency fund with 3-6 months of living expenses.",
        "Consider investing in low-cost index funds for long-term growth."
    ]
    return random.choice(recommendations)

def predict_future_expenses(user_id):
    # In a real scenario, this would use historical data and ML models
    return f"Based on your spending habits, your predicted expenses for next month are ${random.randint(1000, 5000)}"

def check_alerts(user_id):
    alerts = [
        "Your expenses are higher than usual this month.",
        "You're close to reaching your savings goal!",
        "Consider rebalancing your investment portfolio.",
        "You've consistently stayed under budget for 3 months!",
        "No alerts at this time."
    ]
    return random.choice(alerts)