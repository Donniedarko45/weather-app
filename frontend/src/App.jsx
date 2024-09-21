// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header.jsx';
import Weather from './components/Weather.jsx';
import CropPrediction from './components/CropPrediction.jsx';
import Feedback from './components/Feedback.jsx';
import GanModel from './components/GanModel.jsx';
import Home from './components/Home.jsx';
function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/weather/" element={<Weather />} />
        <Route path="/crop-prediction" element={<CropPrediction />} />
        <Route path="/feedback" element={<Feedback />} />
        <Route path="/" element={<Home />} />
        <Route path='/gandmodel' element={<GanModel/>}/>
      </Routes>
    </Router>
  );
}

export default App;