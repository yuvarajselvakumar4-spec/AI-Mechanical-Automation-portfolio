import pandas as pd
import numpy as np

# 1. Simulate Product Quality Data (உற்பத்தி பொருட்களின் தரத்தை பரிசோதிக்கும் டேட்டா)
def generate_quality_data(num_records=200):
    np.random.seed(101)
    data = {
        'Product_ID': [f'PRD_{i:03d}' for i in range(1, num_records + 1)],
        'Weight_grams': np.random.normal(500.0, 5.2, size=num_records),
        'Length_mm': np.random.normal(150.0, 1.5, size=num_records),
        'Surface_Defects': np.random.choice([0, 1, 2], size=num_records, p=[0.85, 0.12, 0.03]),
        'Material_Strength_MPa': np.random.uniform(220.0, 280.0, size=num_records)
    }
    return pd.DataFrame(data)

# 2. Quality Control & Auto-Rejection AI Logic
class QualityControlAI:
    def __init__(self, df):
        self.df = df

    def inspect_products(self):
        print("=== QUALITY CONTROL AI INSPECTION REPORT ===")
        
        # Defect Detection Logic (எடை மாறுபாடு அல்லது மேற்பரப்பு குறைபாடு இருந்தால் REJECT)
        self.df['Inspection_Status'] = np.where(
            (self.df['Surface_Defects'] > 0) | 
            (self.df['Weight_grams'] < 485.0) | 
            (self.df['Weight_grams'] > 515.0),
            'REJECTED_DEFECTIVE', 
            'PASSED_APPROVED'
        )
        
        # Summary metrics
        total_checked = len(self.df)
        rejected_count = len(self.df[self.df['Inspection_Status'] == 'REJECTED_DEFECTIVE'])
        approved_count = len(self.df[self.df['Inspection_Status'] == 'PASSED_APPROVED'])
        
        print(f"Total Products Inspected: {total_checked}")
        print(f"Approved Products: {approved_count}")
        print(f"Rejected Defective Products: {rejected_count}")
        print("\n--- Defective Items Alert Log ---")
        print(self.df[self.df['Inspection_Status'] == 'REJECTED_DEFECTIVE'][['Product_ID', 'Weight_grams', 'Surface_Defects', 'Inspection_Status']].head(10))
        
        return self.df

# --- EXECUTION ---
if __name__ == "__main__":
    # Generate quality dataset
    quality_df = generate_quality_data(200)
    
    # Run Quality Control AI
    qc_ai = QualityControlAI(quality_df)
    inspected_data = qc_ai.inspect_products()
