
import csv
class WeatherLogger:
    def load(self, filepath: str) -> list:
        
        try:
            with open(filepath, "r") as file:
                data = list(csv.DictReader(file))
        except:
            raise FileNotFoundError
        
        return data
            
        
   
        
