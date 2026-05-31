import pandas as pd
from data_loader import BIWDataLoader
from model_mix_adjustment import ModelMixAdjuster

class OEECalculator:
    def __init__(self, data_dir: str = "data"):
        self.loader = BIWDataLoader(data_dir)
        self.cycle_times = self.loader.get_ideal_cycle_times()
        self.adjuster = ModelMixAdjuster(self.cycle_times)

    def calculate_line_oee(self, line_name: str, planned_time_mins: float) -> dict:
        """
        Calculates the granular Availability, Performance, Quality, and overall OEE 
        for an explicit BIW area.
        """
        line_name = line_name.upper().strip()
        
        # Ingest and Filter Data
        prod_df = self.loader.load_production_data()
        down_df = self.loader.load_downtime_data()
        
        line_prod = prod_df[prod_df['line_name'] == line_name]
        line_down = down_df[down_df['line_name'] == line_name]

        # 1. Availability Calculation
        unplanned_down_mins = line_down[line_down['downtime_type'] == 'UNPLANNED']['duration_mins'].sum()
        planned_down_mins = line_down[line_down['downtime_type'] == 'PLANNED']['duration_mins'].sum()
        
        net_planned_run_time = planned_time_mins - planned_down_mins
        operating_time = net_planned_run_time - unplanned_down_mins
        
        availability = (operating_time / net_planned_run_time) if net_planned_run_time > 0 else 0.0

        # 2. Performance Calculation (Adjusted for Renault Model Mix)
        total_produced = line_prod['total_produced'].sum()
        weighted_ideal_cycle_time_sec = self.adjuster.calculate_weighted_ideal_time(line_prod)
        
        # Total operating time transformed to seconds for baseline alignment
        operating_time_sec = operating_time * 60.0
        expected_time_for_production = total_produced * weighted_ideal_cycle_time_sec
        
        performance = (expected_time_for_production / operating_time_sec) if operating_time_sec > 0 else 0.0
        # Cap performance at 1.0 to handle potential micro-adjustments or pacing variances
        performance = min(performance, 1.0)

        # 3. Quality Calculation
        scrap_units = line_prod['scrap_units'].sum()
        good_units = total_produced - scrap_units
        
        quality = (good_units / total_produced) if total_produced > 0 else 0.0

        # 4. Final OEE Combination
        oee = availability * performance * quality

        return {
            "Line Name": line_name,
            "Availability": round(availability, 4),
            "Performance": round(performance, 4),
            "Quality": round(quality, 4),
            "OEE": round(oee, 4),
            "Total Volume Output": int(total_produced)
        }

if __name__ == "__main__":
    # Standard engineering script invocation
    calculator = OEECalculator()
    # Assuming a standard 8-hour shift layout (480 minutes total planned)
    try:
        underbody_metrics = calculator.calculate_line_oee("UNDERBODY_LINE", planned_time_mins=480.0)
        print("--- BIW Shift Production Metrics ---")
        for k, v in underbody_metrics.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Pipeline Execution Error: {e}")
