def calculate_score(data):
    score = 0

    # Emergency Fund
    if data.get("savings", 0) >= data.get("expenses", 0) * 6:
        score += 20

    # Insurance
    if data.get("insurance", 0) > 0:
        score += 15

    # Investments
    if data.get("investments", 0) > 0:
        score += 20

    # Debt
    if data.get("debt", 0) < data.get("income", 1) * 0.3:
        score += 15

    # Tax
    if data.get("tax_saving", False):
        score += 10

    # Retirement
    if data.get("retirement_plan", False):
        score += 20

    return score
