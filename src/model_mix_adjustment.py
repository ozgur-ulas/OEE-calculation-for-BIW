import pandas as pd

class ModelMixAdjuster:
    def __init__(self, ideal_cycle_times: dict):
        self.ideal_cycle_times = ideal_cycle_times

    def calculate_weighted_ideal_time(self, shift_production_df: pd.DataFrame) -> float:
        """
        Calculates the dynamically blended target cycle time for a mixed run.
        Formula: Sum(Units_m * Ideal_Time_m) / Total_Units
        """
        total_units = shift_production_df['total_produced'].sum()
        if total_units == 0:
            return 0.0

        weighted_time_sum = 0.0
        for _, row in shift_production_df.iterrows():
            model = row['model_name']
            units = row['total_produced']
            ideal_time = self.ideal_cycle_times.get(model, 60.0) # Default 60s fallback
            weighted_time_sum += (units * ideal_time)

        return weighted_time_sum / total_units
