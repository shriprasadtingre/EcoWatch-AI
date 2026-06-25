def calculate_ehi(temp, humidity, wind, aqi, pm25):

    score = 100

    if temp > 35:
        score -= (temp - 35) * 2

    if humidity > 75:
        score -= (humidity - 75)

    if aqi > 100:
        score -= (aqi - 100) * 0.15

    if pm25 > 50:
        score -= (pm25 - 50) * 0.3

    if wind > 10:
        score += 3

    score = max(0, min(100, round(score)))

    if score >= 80:
        status = "Excellent"
    elif score >= 60:
        status = "Good"
    elif score >= 40:
        status = "Moderate"
    elif score >= 20:
        status = "Poor"
    else:
        status = "Critical"

    return score, status