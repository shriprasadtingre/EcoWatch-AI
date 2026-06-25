def predict_heatwave(temp, humidity):

    if temp >= 40:
        return "High"

    elif temp >= 35:
        return "Medium"

    return "Low"


def predict_pollution(aqi, pm25):

    if aqi >= 180 or pm25 >= 100:
        return "High"

    elif aqi >= 100:
        return "Medium"

    return "Low"