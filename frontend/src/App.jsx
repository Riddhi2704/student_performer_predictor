import React, { useState } from 'react';
import axios from 'axios';
import PredictorForm from './components/PredictorForm';
import Animation from './components/Animation';

function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handlePredict = async (data) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      // Simulate network delay to show off the animation
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      const response = await axios.post('http://localhost:5000/predict', data);
      
      if (response.data.status === 'success') {
        setResult(response.data.predicted_grade);
      } else {
        setError(response.data.message);
      }
    } catch (err) {
      setError(err.message || 'An error occurred while connecting to the backend.');
    } finally {
      setLoading(false);
    }
  };

  const getResultColor = (grade) => {
    if (grade === 'A' || grade === 'B') return 'var(--primary-green)';
    if (grade === 'C' || grade === 'D') return 'var(--primary-orange)';
    return '#d9534f'; // red for F
  };

  return (
    <div className="premium-card">
      <h1 style={{ marginBottom: '10px' }}>Student Performance Predictor</h1>
      <p style={{ color: 'var(--dark-green)', marginBottom: '30px' }}>
        Enter the student's details below to predict their final grade class.
      </p>

      {loading ? (
        <Animation />
      ) : result ? (
        <div style={{ padding: '40px', textAlign: 'center' }}>
          <h2 style={{ color: 'var(--dark-green)' }}>Prediction Result:</h2>
          <div style={{ 
            fontSize: '72px', 
            fontWeight: 'bold', 
            color: getResultColor(result),
            textShadow: '2px 2px 4px rgba(0,0,0,0.1)',
            margin: '20px 0'
          }}>
            Grade {result}
          </div>
          <button 
            className="btn-primary" 
            onClick={() => setResult(null)}
            style={{ backgroundColor: 'var(--primary-green)' }}
          >
            Predict Another Student
          </button>
        </div>
      ) : (
        <>
          {error && (
            <div style={{ color: '#d9534f', padding: '10px', backgroundColor: '#fdf3f2', borderRadius: '5px', marginBottom: '20px' }}>
              Error: {error}
            </div>
          )}
          <PredictorForm onSubmit={handlePredict} />
        </>
      )}
    </div>
  );
}

export default App;
