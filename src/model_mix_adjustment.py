def calculate_weighted_cycle_time(row, ideal_times):
    """
    Calculates the total theoretical time required for a specific mix.
    Formula: Sum(Units_model_i * Ideal_CT_model_i)
    """
    total_theoretical_seconds = 0
    total_units = 0
    
    for model, ideal_ct in ideal_times.items():
        units = row[model]
        total_theoretical_seconds += (units * ideal_ct)
        total_units += units
        
    weighted_ideal_ct = total_theoretical_seconds / total_units if total_units > 0 else 0
    return weighted_ideal_ct, total_units, total_theoretical_seconds
