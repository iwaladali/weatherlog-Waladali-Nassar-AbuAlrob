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