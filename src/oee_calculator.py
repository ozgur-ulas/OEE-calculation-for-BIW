from data_loader import load_production_data, get_ideal_cycle_times
from model_mix_adjustment import calculate_weighted_cycle_time

def calculate_oee():
    df = load_production_data()
    ideal_times = get_ideal_cycle_times()
    
    results = []
    
    for _, row in df.iterrows():
        # 1. Availability = (Planned Time - Down Time) / Planned Time
        operating_time = row['Planned_Time_Min'] - row['Down_Time_Min']
        availability = operating_time / row['Planned_Time_Min']
        
        # 2. Performance = (Total Units * Weighted Ideal CT) / Operating Time
        w_ideal_ct, total_units, total_theo_sec = calculate_weighted_cycle_time(row, ideal_times)
        performance = (total_theo_sec / 60) / operating_time if operating_time > 0 else 0
        
        # 3. Quality = (Total Units - Rework) / Total Units
        quality = (total_units - row['Rework_Units']) / total_units if total_units > 0 else 0
        
        # OEE = A * P * Q
        oee = availability * performance * quality
        
        results.append({
            'Line': row['Line'],
            'Availability': round(availability * 100, 2),
            'Performance': round(performance * 100, 2),
            'Quality': round(quality * 100, 2),
            'OEE': round(oee * 100, 2)
        })
        
    return pd.DataFrame(results)

if __name__ == "__main__":
    oee_df = calculate_oee()
    print(oee_df)
