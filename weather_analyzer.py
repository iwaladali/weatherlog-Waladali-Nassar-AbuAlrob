import numpy as np

class WeatherAnalyzer:

   def monthly_stats(self, logs: list) -> dict:
    groups = {}

    for r in logs:
        key = r["date"][:7]   # "YYYY-MM"
        if key not in groups:
            groups[key] = []
        groups[key].append(r)

    stats = {}

    for month_key, records in groups.items():
        temps = [float(r["temp_c"]) for r in records]
        humidities = [float(r["humidity_pct"]) for r in records]
        rainy_days = sum(1 for r in records if r["condition"] == "Rainy")

        stats[month_key] = {
            "avg_temp": round(float(np.mean(temps)), 2),
            "max_temp": round(float(np.max(temps)), 2),
            "min_temp": round(float(np.min(temps)), 2),
            "std_temp": round(float(np.std(temps)), 2),
            "avg_humidity": round(float(np.mean(humidities)), 2),
            "rainy_days": rainy_days,
            "total_days": len(records),
        }

    return stats
   
