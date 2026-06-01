import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report
import os

def main():
    print("Loading preprocessed data...")
    X_train = joblib.load('data/X_train_scaled.pkl')
    X_test = joblib.load('data/X_test_scaled.pkl')
    y_train = joblib.load('data/y_train.pkl')
    y_test = joblib.load('data/y_test.pkl')
    
    print("Training Random Forest with Hyperparameter Tuning...")
    rf = RandomForestClassifier(random_state=42)
    rf_param_dist = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    rf_search = RandomizedSearchCV(rf, param_distributions=rf_param_dist, n_iter=10, cv=3, random_state=42, n_jobs=-1, verbose=1)
    rf_search.fit(X_train, y_train)
    
    print("Training SVM with Hyperparameter Tuning...")
    svm = SVC(probability=True, random_state=42)
    svm_param_dist = {
        'C': [0.1, 1, 10, 100],
        'gamma': ['scale', 'auto', 0.1, 0.01],
        'kernel': ['rbf', 'linear']
    }
    svm_search = RandomizedSearchCV(svm, param_distributions=svm_param_dist, n_iter=10, cv=3, random_state=42, n_jobs=-1, verbose=1)
    svm_search.fit(X_train, y_train)
    
    # Evaluate Models
    rf_best = rf_search.best_estimator_
    svm_best = svm_search.best_estimator_
    
    rf_preds = rf_best.predict(X_test)
    svm_preds = svm_best.predict(X_test)
    
    rf_acc = accuracy_score(y_test, rf_preds)
    svm_acc = accuracy_score(y_test, svm_preds)
    
    print(f"\nRandom Forest Accuracy: {rf_acc:.4f}")
    print(f"SVM Accuracy: {svm_acc:.4f}")
    
    best_model = None
    best_acc = 0
    best_name = ""
    
    if rf_acc > svm_acc:
        best_model = rf_best
        best_acc = rf_acc
        best_name = "Random Forest"
    else:
        best_model = svm_best
        best_acc = svm_acc
        best_name = "SVM"
        
    print(f"\nBest Model: {best_name} with Accuracy {best_acc:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, best_model.predict(X_test)))
    
    # Save the best model
    os.makedirs('backend', exist_ok=True)
    joblib.dump(best_model, 'backend/model.pkl')
    print("Best model saved to backend/model.pkl")

if __name__ == "__main__":
    main()
