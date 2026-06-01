import React, { useState } from 'react';

const PredictorForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    Age: 15,
    Gender: 0,
    Ethnicity: 0,
    ParentalEducation: 0,
    StudyTimeWeekly: 10,
    Absences: 0,
    Tutoring: 0,
    ParentalSupport: 2,
    Extracurricular: 0,
    Sports: 0,
    Music: 0,
    Volunteering: 0,
    GPA: 2.5
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: parseFloat(value)
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="grid-2">
        <div className="input-group">
          <label>Age (15-18)</label>
          <input type="number" name="Age" min="15" max="18" value={formData.Age} onChange={handleChange} required />
        </div>
        <div className="input-group">
          <label>Gender</label>
          <select name="Gender" value={formData.Gender} onChange={handleChange}>
            <option value={0}>Male</option>
            <option value={1}>Female</option>
          </select>
        </div>
        <div className="input-group">
          <label>Ethnicity (0-3)</label>
          <select name="Ethnicity" value={formData.Ethnicity} onChange={handleChange}>
            <option value={0}>Caucasian</option>
            <option value={1}>African American</option>
            <option value={2}>Asian</option>
            <option value={3}>Other</option>
          </select>
        </div>
        <div className="input-group">
          <label>Parental Education (0-4)</label>
          <select name="ParentalEducation" value={formData.ParentalEducation} onChange={handleChange}>
            <option value={0}>None</option>
            <option value={1}>High School</option>
            <option value={2}>Some College</option>
            <option value={3}>Bachelor's</option>
            <option value={4}>Higher</option>
          </select>
        </div>
        <div className="input-group">
          <label>Study Time Weekly (Hours)</label>
          <input type="number" step="0.1" name="StudyTimeWeekly" value={formData.StudyTimeWeekly} onChange={handleChange} required />
        </div>
        <div className="input-group">
          <label>Absences</label>
          <input type="number" name="Absences" value={formData.Absences} onChange={handleChange} required />
        </div>
        <div className="input-group">
          <label>GPA (0.0 - 4.0)</label>
          <input type="number" step="0.1" name="GPA" min="0" max="4.0" value={formData.GPA} onChange={handleChange} required />
        </div>
        <div className="input-group">
          <label>Parental Support (0-4)</label>
          <input type="number" name="ParentalSupport" min="0" max="4" value={formData.ParentalSupport} onChange={handleChange} required />
        </div>
      </div>
      
      <div className="grid-2">
        <div className="input-group">
          <label>Tutoring</label>
          <select name="Tutoring" value={formData.Tutoring} onChange={handleChange}>
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select>
        </div>
        <div className="input-group">
          <label>Extracurricular</label>
          <select name="Extracurricular" value={formData.Extracurricular} onChange={handleChange}>
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select>
        </div>
        <div className="input-group">
          <label>Sports</label>
          <select name="Sports" value={formData.Sports} onChange={handleChange}>
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select>
        </div>
        <div className="input-group">
          <label>Music</label>
          <select name="Music" value={formData.Music} onChange={handleChange}>
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select>
        </div>
        <div className="input-group">
          <label>Volunteering</label>
          <select name="Volunteering" value={formData.Volunteering} onChange={handleChange}>
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select>
        </div>
      </div>

      <button type="submit" className="btn-primary">Predict Performance</button>
    </form>
  );
};

export default PredictorForm;
