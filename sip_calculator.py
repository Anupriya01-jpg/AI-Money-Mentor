def calculate_sip(monthly_investment, annual_rate, years):
    r = annual_rate / 12 / 100
    n = years * 12
    future_value = monthly_investment * (((1 + r)**n - 1) / r)
    return round(future_value, 2)
