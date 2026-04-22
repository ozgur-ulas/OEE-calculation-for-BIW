import matplotlib.pyplot as plt

def plot_line_performance(oee_df):
    """Generates a bar chart comparing OEE across different BIW lines."""
    plt.figure(figsize=(10, 6))
    lines = oee_df['Line']
    oee_values = oee_df['OEE']
    
    colors = ['green' if x > 85 else 'orange' if x > 70 else 'red' for x in oee_values]
    
    plt.bar(lines, oee_values, color=colors)
    plt.axhline(y=85, color='blue', linestyle='--', label='World Class OEE (85%)')
    
    plt.title('BIW Production Line OEE Comparison', fontsize=14)
    plt.ylabel('OEE %')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('oee_comparison.png')
    print("Graph saved as oee_comparison.png")
    plt.show()

# Run visualization if executed directly
if __name__ == "__main__":
    from oee_calculator import calculate_oee
    df = calculate_oee()
    plot_line_performance(df)
