def get_advice(message):
    message = message.lower()

    if "invest" in message:
        return "You should invest 20% of your income in SIPs."
    elif "tax" in message:
        return "Use 80C deductions like ELSS and PPF."
    elif "save" in message:
        return "Maintain an emergency fund of 6 months expenses."
    else:
        return "Diversify your investments and track your expenses."
