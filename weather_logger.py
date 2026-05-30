
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
        
