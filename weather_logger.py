
import csv
class WeatherLogger:

    def load(self, filepath: str) -> list:
        
        try:
            with open(filepath, "r") as file:
                data = list(csv.DictReader(file))
        except:
            raise FileNotFoundError
        
        return data
            
        
    
    def save(self, logs: list, filepath: str) -> None:
        
        with open(filepath, 'w') as f:
            Fieldnames= ["date", "temp_c", "humidity_pct", "wind_kph", "condition"]
            writer = csv.DictWriter(f, fieldnames=Fieldnames)
            writer.writeheader()
            writer.writerows(logs)
        print(f"Successfuly was Saved The Data in file where path is {filepath}")
    
    def add_entry(self, logs: list, date_str: str, temp_c: float, 
                  humidity_pct: float, wind_kph: float, 
                  condition: str) -> list:
        
        from datetime import datetime
        
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        
        if any(r["date"] == date_str for r in logs):
          raise ValueError(f"A record for {date_str} already exists") 
        
        if not (-20 <= temp_c <= 50):
           raise ValueError("Temperature must be between -20 and 50°C")
        
        if not (0 <= humidity_pct <= 100):
          raise ValueError("Humidity must be between 0 and 100")
        
        VALID_CONDITIONS = ["Sunny", "Cloudy", "Rainy", "Foggy"]

        if condition not in VALID_CONDITIONS:
            raise ValueError(f"Condition must be one of {VALID_CONDITIONS}")
        
        logs.append({
            "date":         date_str,
            "temp_c":       str(temp_c),
            "humidity_pct": str(humidity_pct),
            "wind_kph":     str(wind_kph),
            "condition":    condition
                     })
        return logs
    
    def get_by_month(self, logs: list, year: int, month: int) -> list:
        prefix = f"{year}-{month:02d}"   # e.g. "2026-03"
        return [r for r in logs if r["date"].startswith(prefix)]
    
        
