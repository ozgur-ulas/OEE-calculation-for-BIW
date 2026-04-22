import pandas as pd
import numpy as np

def load_production_data():
    """
    Simulates or loads the BIW production log.
    Models: Clio 4 HB, Clio 4 SW, Clio 5, Megane 4
    """
    data = {
        'Line': ['Underbody', 'Bodyside_1', 'Bodyside_2', 'Main_Connection'],
        'Clio_4_HB': [150, 140, 145, 140],
        'Clio_4_SW': [50, 45, 48, 45],
        'Clio_5': [200, 190, 195, 190],
        'Megane_4': [80, 75, 78, 75],
        'Down_Time_Min': [45, 60, 30, 50],
        'Rework_Units': [5, 8, 4, 10],
        'Planned_Time_Min': [480, 480, 480, 480]  # 8-hour shift
    }
    return pd.DataFrame(data)

def get_ideal_cycle_times():
    """Returns the theoretical ideal cycle time (seconds) per model."""
    return {
        'Clio_4_HB': 54.0,
        'Clio_4_SW': 58.0,
        'Clio_5': 52.0,
        'Megane_4': 65.0
    }
