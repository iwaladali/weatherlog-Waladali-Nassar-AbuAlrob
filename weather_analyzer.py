import numpy as np

class WeatherAnalyzer:

    def monthly_stats(self, logs: list) -> dict:
        groups = {}

        for r in logs:
            key = r["date"][:7]  # YYYY-MM

            if key not in groups:
                groups[key] = []

            groups[key].append(r)

        stats = {}

