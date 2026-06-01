import pandas as pd
import numpy as np
import os

def generate_mock_data(num_samples=1000):
    np.random.seed(42)
    
    data = {
        'StudentID': np.arange(1001, 1001 + num_samples),
        'Age': np.random.randint(15, 19, num_samples),
        'Gender': np.random.randint(0, 2, num_samples),
        'Ethnicity': np.random.randint(0, 4, num_samples),
        'ParentalEducation': np.random.randint(0, 5, num_samples),
        'StudyTimeWeekly': np.random.uniform(0, 20, num_samples).round(2),
        'Absences': np.random.randint(0, 30, num_samples),
        'Tutoring': np.random.randint(0, 2, num_samples),
        'ParentalSupport': np.random.randint(0, 5, num_samples),
        'Extracurricular': np.random.randint(0, 2, num_samples),
        'Sports': np.random.randint(0, 2, num_samples),
        'Music': np.random.randint(0, 2, num_samples),
        'Volunteering': np.random.randint(0, 2, num_samples),
        'GPA': np.random.uniform(1.0, 4.0, num_samples).round(2),
        'GradeClass': np.random.randint(0, 5, num_samples)
    }
    
    # Introduce some logical correlation so the model has something to learn
    # High GPA -> lower GradeClass number (0 is 'A', 4 is 'F')
    conditions = [
        data['GPA'] >= 3.5,
        (data['GPA'] >= 3.0) & (data['GPA'] < 3.5),
        (data['GPA'] >= 2.5) & (data['GPA'] < 3.0),
        (data['GPA'] >= 2.0) & (data['GPA'] < 2.5),
        data['GPA'] < 2.0
    ]
    choices = [0, 1, 2, 3, 4]
    data['GradeClass'] = np.select(conditions, choices, default=4)
    
    df = pd.DataFrame(data)
    
    # Introduce some missing values and outliers for preprocessing to handle
    idx = np.random.choice(df.index, size=20, replace=False)
    df.loc[idx, 'StudyTimeWeekly'] = np.nan
    
    idx = np.random.choice(df.index, size=10, replace=False)
    df.loc[idx, 'Absences'] = 100 # Outlier
    
    return df

if __name__ == "__main__":
    df = generate_mock_data()
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/StudentsPerformance.csv', index=False)
    print("Mock dataset created successfully at data/StudentsPerformance.csv")
