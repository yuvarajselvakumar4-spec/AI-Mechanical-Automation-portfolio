import pandas as pd
import numpy as np

class UniversalFactoryAutomationAI:
    def __init__(self):
        print("Initializing Universal Factory Automation AI Engine...")

    def run_complete_factory_pipeline(self):
        # 1. Simulate Combined Plant & Quality Data
        np.random.seed(2026)
        data = {
            'Machine_ID': [f'MC_{i:03d}' for i in range(1, 101)],
            'Temperature_C': np.random.uniform(60.0, 110.0, size=100),
            'Vibration_Hz': np.random.uniform(1.0, 8.0, size=100),
            'Defect_Flag': np.random.choice([0, 1], size=100, p=[0.9, 0.1])
        }
        df = pd.DataFrame(data)

        # 2. Automated Action Logic
        df['Action_Required'] = np.where(
            (df['Temperature_C'] > 100.0) | (df['Vibration_Hz'] > 7.0) | (df['Defect_Flag'] == 1),
            'STOP_MACHINE_AND_INSPECT',
            'CONTINUE_PRODUCTION'
        )

        # 3. Output Summary
        alerts = len(df[df['Action_Required'] == 'STOP_MACHINE_AND_INSPECT'])
        print(f"Total Units Checked: {len(df)}")
        print(f"Critical Actions Triggered: {alerts}")
        return df

if __name__ == "__main__":
    automation_ai = UniversalFactoryAutomationAI()
    final_report = automation_ai.run_complete_factory_pipeline()
