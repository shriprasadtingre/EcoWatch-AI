import pandas as pd


def forecast_next_days(df, column, days=7):

    if len(df) < 2:
        return None

    values = df[column]

    change = values.diff().mean()

    latest = values.iloc[-1]

    predictions = []

    for i in range(1, days + 1):

        next_value = latest + (change * i)

        predictions.append({
            "Day": f"Day {i}",
            "Prediction": round(max(0, next_value), 2)
        })

    return pd.DataFrame(predictions)