import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as plt_sns # Use a different alias to avoid conflicts if needed, or just sns
import seaborn as sns
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    print("Loading data...")
    df = pd.read_csv('data/StudentsPerformance.csv')
    
    # 1. EDA
    os.makedirs('ml/plots', exist_ok=True)
    
    plt.figure(figsize=(8, 6))
    sns.countplot(x='GradeClass', data=df, palette='viridis')
    plt.title('Distribution of Grade Classes')
    plt.savefig('ml/plots/grade_distribution.png')
    plt.close()
    
    plt.figure(figsize=(12, 10))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 8})
    plt.title('Feature Correlation Heatmap')
    plt.savefig('ml/plots/correlation_heatmap.png')
    plt.close()
    
    print("EDA graphs saved to ml/plots/")
    
    # 2. Data Preprocessing
    print("Preprocessing data...")
    # Fill Null values
    if df.isnull().sum().any():
        print("Handling missing values...")
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                # Use median for numerical cols
                df[col] = df[col].fillna(df[col].median())
                
    # Handle Outliers (e.g., in Absences using IQR or clipping)
    # Clipping Absences at 30
    df['Absences'] = np.clip(df['Absences'], 0, 30)
    
    # Feature Engineering
    # Drop StudentID as it's not predictive
    if 'StudentID' in df.columns:
        df.drop('StudentID', axis=1, inplace=True)
        
    # Split Data
    X = df.drop('GradeClass', axis=1)
    y = df['GradeClass']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scale Features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save processed data and scaler
    joblib.dump(X_train_scaled, 'data/X_train_scaled.pkl')
    joblib.dump(X_test_scaled, 'data/X_test_scaled.pkl')
    joblib.dump(y_train, 'data/y_train.pkl')
    joblib.dump(y_test, 'data/y_test.pkl')
    joblib.dump(scaler, 'data/scaler.pkl')
    
    # Save feature names for the backend API to know the expected order
    joblib.dump(list(X.columns), 'data/feature_names.pkl')
    
    print("Preprocessing complete. Scaled data and scaler saved to data/ directory.")

if __name__ == "__main__":
    main()
