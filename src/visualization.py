import matplotlib.pyplot as plt

class BIWVisualizer:
    @staticmethod
    def plot_oee_losses(metrics: dict, save_path: str = "reports/loss_breakdown.png"):
        """
        Generates a clean breakdown visualization showing the degradation path 
        from ideal 100% efficiency to the actual current line OEE.
        """
        labels = ['Availability', 'Performance', 'Quality', 'Overall OEE']
        # Convert ratios to standard display percentages
        values = [
            metrics['Availability'] * 100,
            metrics['Performance'] * 100,
            metrics['Quality'] * 100,
            metrics['OEE'] * 100
        ]

        plt.figure(figsize=(8, 5))
        colors = ['#2b5c8f', '#4682b4', '#60a3bc', '#e55039']
        
        bars = plt.bar(labels, values, color=colors, width=0.5)
        plt.ylim(0, 105)
        plt.ylabel("Efficiency Percentage (%)")
        plt.title(f"BIW Line Performance Profiling - Line ID: {metrics.get('Line Name', 'Unknown')}")
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        # Draw values clearly on top of the bars
        for bar in bars:
            height = bar.get_height()
            plt.annotate(f'{height:.1f}%',
                         xy=(bar.get_x() + bar.get_width() / 2, height),
                         xytext=(0, 3),  
                         textcoords="offset points",
                         ha='center', va='bottom', fontweight='bold')

        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"OEE analytical loss visualization saved directly to: {save_path}")
