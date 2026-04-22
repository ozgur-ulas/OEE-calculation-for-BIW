import pandas as pd

def load_all_data():
    production = pd.read_csv('data/sample_production.csv')
    downtime = pd.read_csv('data/sample_downtime.csv')
    cycle_times = pd.read_csv('data/cycle_times.csv').set_index('Model')['Ideal_Cycle_Time_Sec'].to_dict()
    
    # Merge downtime duration into production for OEE calculation
    total_downtime = downtime.groupby('Line')['Duration_Min'].sum().reset_index()
    df = pd.merge(production, total_downtime, on='Line', how='left').fillna(0)
    
    return df, cycle_times
