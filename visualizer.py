import matplotlib.pyplot as plt
import numpy as np


class Visualizer:

    def temp_trend(self, logs: list):
        if not logs:
            print("No weather logs available.")
            return

        recent = logs[-30:]

        dates = [r["date"][5:] for r in recent]
        temps = [float(r["temp_c"]) for r in recent]

        x = range(len(recent))

        fig, ax = plt.subplots(figsize=(12, 5))

        ax.plot(x, temps, color="tomato", linewidth=2, marker="o", markersize=4)
        ax.fill_between(x, temps, alpha=0.15, color="tomato")

        ax.set_xticks(x)
        ax.set_xticklabels(dates, rotation=45, fontsize=8)

        ax.set_ylabel("Temperature (°C)")
        ax.set_title("Daily Temperature Trend — Last 30 Days")

        mean_temp = np.mean(temps)

        ax.axhline(
            y=mean_temp,
            color="gray",
            linestyle="--",
            alpha=0.7,
            label=f"Mean: {mean_temp:.1f}°C"
        )

        ax.legend()
        plt.tight_layout()
        plt.show()
        
        
    def monthly_avg_chart(self, stats: dict):

        months = sorted(stats.keys())

        avgs = [stats[m]["avg_temp"] for m in months]

        colors = [
            "orangered" if t >= 25
            else "steelblue" if t <= 15
            else "gold"
            for t in avgs
        ]

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.bar(months, avgs, color=colors, edgecolor="black")

        ax.set_ylabel("Avg Temperature (°C)")
        ax.set_title("Monthly Average Temperature")

        ax.set_xticklabels(months, rotation=30)

        for i, v in enumerate(avgs):
            ax.text(i, v + 0.2, f"{v}°C", ha="center", fontsize=10)

        plt.tight_layout()
        plt.show()
        
        
        
        