def environmental_chat(user_input, latest):

    msg = user_input.lower()

    aqi = latest["aqi"]
    temp = latest["temperature"]
    pm25 = latest["pm25"]

    if "pollution" in msg:

        if aqi > 150:
            return """
High pollution detected.

Possible causes:
- Vehicle emissions
- Industrial activity
- Dry weather

Suggestions:
- Reduce outdoor exposure
- Use masks
- Prefer public transport
"""

        return "Pollution currently appears moderate."

    elif "heatwave" in msg:

        if temp >= 38:
            return """
Heatwave risk is elevated.

Possible causes:
- High temperature
- Seasonal conditions

Suggestions:
- Stay hydrated
- Limit outdoor activity
"""
        return "Heatwave risk currently appears low."

    elif "health" in msg:

        return f"""
Current conditions:

AQI: {aqi}
Temperature: {temp}
PM2.5: {pm25}

Monitor conditions regularly.
"""

    return """
I can answer:

- Pollution
- Heatwave
- Health
"""