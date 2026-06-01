from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app) # Allow frontend to communicate with backend

# Load the saved ML components
try:
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, 'model.pkl')
    scaler_path = os.path.join(base_dir, '..', 'data', 'scaler.pkl')
    features_path = os.path.join(base_dir, '..', 'data', 'feature_names.pkl')
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature_names = joblib.load(features_path)
    print("Model, scaler, and features loaded successfully.")
except Exception as e:
    print(f"Error loading models (they might not be trained yet): {e}")

# MongoDB Setup
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['student_performance_db']
    predictions_collection = db['predictions']
    print("Connected to MongoDB successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Build dataframe using the expected feature order
        input_data = {}
        for feature in feature_names:
            # If a feature is missing from the request, fill with 0
            input_data[feature] = [data.get(feature, 0)]
            
        df = pd.DataFrame(input_data)
        
        # Scale the data
        scaled_data = scaler.transform(df)
        
        # Make prediction
        prediction = model.predict(scaled_data)[0]
        
        # Target classes:
        # 0: 'A' (GPA >= 3.5), 1: 'B', 2: 'C', 3: 'D', 4: 'F'
        grade_mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F'}
        predicted_grade = grade_mapping.get(int(prediction), 'Unknown')
        
        # Save to MongoDB
        record = {
            'input_features': data,
            'prediction_class': int(prediction),
            'predicted_grade': predicted_grade
        }
        predictions_collection.insert_one(record)
        
        return jsonify({
            'status': 'success',
            'prediction': int(prediction),
            'predicted_grade': predicted_grade
        }), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
