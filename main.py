from weather_logger import WeatherLogger
from weather_analyzer import WeatherAnalyzer
from visualizer import Visualizer


def main():
    DATA_FILE = "weather_log.csv"

    wl = WeatherLogger()
    wa = WeatherAnalyzer()
    viz = Visualizer()

    # Step 1: Load data
    print("[1/5] Loading weather log...")
    logs = wl.load(DATA_FILE)
    print(f"      Records loaded: {len(logs)}\n")

    # Step 2: Add today's entry
    print("[2/5] Adding today's observation...")
    from datetime import date
    today = date.today().strftime("%Y-%m-%d")

    try:
        logs = wl.add_entry(logs, today, 22.5, 60.0, 18.0, "Sunny")
        wl.save(logs, DATA_FILE)
        print(f"      Entry added for {today}")
    except ValueError as e:
        print(f"      Skipped: {e}")

    # Step 3: Analyze
    print("\n[3/5] Analyzing data...")
    stats = wa.monthly_stats(logs)

    print(f"\n  {'Month':<10} {'Avg Temp':>10} {'Max':>8} {'Min':>8} {'Rainy Days':>12}")
    print(f"  {'-'*10} {'-'*10} {'-'*8} {'-'*8} {'-'*12}")

    for month, s in sorted(stats.items()):
        print(f"  {month:<10} {s['avg_temp']:>9}°C {s['max_temp']:>7}°C {s['min_temp']:>7}°C {s['rainy_days']:>12}")

    hottest = wa.find_extreme(logs, "temp_c", "max")
    coldest = wa.find_extreme(logs, "temp_c", "min")

    print(f"\n  Hottest day : {hottest['date']} — {hottest['temp_c']}°C ({hottest['condition']})")
    print(f"  Coldest day : {coldest['date']} — {coldest['temp_c']}°C ({coldest['condition']})")

    summary = wa.condition_summary(logs)
    print(f"\n  Condition breakdown: {summary}")

    # Step 4: Show charts
    print("\n[4/5] Displaying charts...")
    viz.temp_trend(logs)
    viz.monthly_avg_chart(stats)
    viz.humidity_scatter(logs)

    print("\n[5/5] Done!")


if __name__ == "__main__":
    main()