import pandas as pd
import random
from datetime import datetime
from pathlib import Path

temperature = random.randint(25, 42)
humidity = random.randint(40, 85)
wind = random.randint(2, 18)
aqi = random.randint(40, 250)
pm25 = random.randint(10, 150)

record = {
    "timestamp": datetime.now(),
    "temperature": temperature,
    "humidity": humidity,
    "wind_speed": wind,
    "aqi": aqi,
    "pm25": pm25
}

path = Path("data/raw/environment_data.csv")

if path.exists():
    df = pd.read_csv(path)
else:
    df = pd.DataFrame()

df = pd.concat(
    [df, pd.DataFrame([record])],
    ignore_index=True
)

df.to_csv(path, index=False)

print("Data collected")
print(record)