import csv
import random
from datetime import date, timedelta

def create_sample_data(filepath="weather_log.csv"):
    conditions = ["Sunny", "Cloudy", "Rainy", "Foggy"]
    weights    = [0.40, 0.30, 0.20, 0.10]   # Sunny is most common

    today = date.today()
    rows  = [["date", "temp_c", "humidity_pct", "wind_kph", "condition"]]

    for i in range(74, -1, -1):
        day       = today - timedelta(days=i)
        temp      = round(random.uniform(10.0, 32.0), 1)
        humidity  = round(random.uniform(40.0, 95.0), 1)
        wind      = round(random.uniform(5.0, 45.0), 1)
        condition = random.choices(conditions, weights=weights)[0]
        rows.append([day.strftime("%Y-%m-%d"), temp, humidity, wind, condition])

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Sample data saved: {filepath}  ({len(rows) - 1} days)")

if __name__ == "__main__":
    create_sample_data()