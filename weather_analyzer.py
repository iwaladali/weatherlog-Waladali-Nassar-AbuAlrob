import numpy as np


class WeatherAnalyzer:

    def monthly_stats(self, logs: list) -> dict:
        groups = {}

        for r in logs:
            key = r["date"][:7]

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

    def find_extreme(self, logs: list, field: str, mode: str) -> dict:

        if mode == "max":
            return max(logs, key=lambda r: float(r[field]))

        elif mode == "min":
            return min(logs, key=lambda r: float(r[field]))

        else:
            raise ValueError("mode must be 'max' or 'min'")

    def condition_summary(self, logs: list) -> dict:

        summary = {}

        for r in logs:
            c = r["condition"]
            summary[c] = summary.get(c, 0) + 1

        return summary