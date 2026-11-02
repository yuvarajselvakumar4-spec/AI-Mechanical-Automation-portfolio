import pandas as pd
import numpy as np

# 1. Simulate Manufacturing Plant Data (உற்பத்தி ஆலை டேட்டாவை உருவாக்குதல்)
def generate_factory_data(num_records=100):
    np.random.seed(42)
    data = {
        'Machine_ID': np.random.choice(['MC_001', 'MC_002', 'MC_003'], size=num_records),
        'Operating_Hours': np.random.randint(100, 5000, size=num_records),
        'Temperature_C': np.random.uniform(60.0, 115.0, size=num_records),
        'Vibration_Hz': np.random.uniform(1.0, 8.5, size=num_records),
        'Output_Units': np.random.randint(500, 2000, size=num_records),
        'Downtime_Hours': np.random.randint(0, 50, size=num_records)
    }
    return pd.DataFrame(data)

# 2. Advanced Analytics & Predictive Maintenance Logic
class ManufacturingAnalyticsAI:
    def __init__(self, df):
        self.df = df

    def analyze_plant_health(self):
        print("=== MANUFACTURING AI ANALYTICS REPORT ===")
        
        # Risk Prediction Logic (வெப்பநிலை மற்றும் அதிர்வு அதிகமாக இருந்தால் Fault Risk உண்டு)
        self.df['Failure_Risk'] = np.where(
            (self.df['Temperature_C'] > 100.0) | (self.df['Vibration_Hz'] > 7.0), 
            'HIGH_RISK_MAINTENANCE_REQUIRED', 
            'NORMAL'
        )
        
        # Summary metrics
        high_risk_machines = self.df[self.df['Failure_Risk'] == 'HIGH_RISK_MAINTENANCE_REQUIRED']
        
        print(f"Total Machines Monitored: {len(self.df)}")
        print(f"Machines Needing Immediate Maintenance: {len(high_risk_machines)}")
        print("\n--- Detailed Risk Alert Feed ---")
        print(high_risk_machines[['Machine_ID', 'Temperature_C', 'Vibration_Hz', 'Failure_Risk']].head(10))
        
        return self.df

# --- EXECUTION ---
if __name__ == "__main__":
    # Generate factory dataset
    factory_df = generate_factory_data(150)
    
    # Run our AI Analytics Engine
    ai_engine = ManufacturingAnalyticsAI(factory_df)
    analyzed_data = ai_engine.analyze_plant_health()
