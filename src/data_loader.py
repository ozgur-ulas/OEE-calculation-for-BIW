import os
import pandas as pd

class BIWDataLoader:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir

    def load_production_data(self, filename: str = "production_logs.csv") -> pd.DataFrame:
        """Loads and normalizes raw count files from the BIW lines."""
        path = os.path.join(self.data_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing production data at: {path}")
        
        df = pd.read_csv(path)
        df['line_name'] = df['line_name'].astype(str).str.upper().str.strip()
        df['model_name'] = df['model_name'].astype(str).str.strip()
        return df

    def load_downtime_data(self, filename: str = "downtime_logs.csv") -> pd.DataFrame:
        """Loads technical breakdown logs and micro-stops."""
        path = os.path.join(self.data_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing downtime logs at: {path}")
            
        df = pd.read_csv(path)
        df['line_name'] = df['line_name'].astype(str).str.upper().str.strip()
        df['downtime_type'] = df['downtime_type'].astype(str).str.upper().str.strip()
        return df

    def get_ideal_cycle_times(self) -> dict:
        """
        Returns engineering standard ideal cycle times (in seconds) 
        per Renault model based on BIW structural complexity.
        """
        return {
            "Clio 4 HB": 54.0,
            "Clio 4 SW": 58.0,
            "Clio 5": 52.0,
            "Megane 4": 65.0
        }
