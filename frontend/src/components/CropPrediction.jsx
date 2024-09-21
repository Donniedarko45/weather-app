import React, { useState } from 'react'

const CropPrediction= function() {
  const [cropData, setCropData] = useState({
    soil_type: '',
    weather_conditions: '',
    irrigation_level: '',
    fertilizers_used: '',
  })
  const [prediction, setPrediction] = useState(null)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      // Simulating API call
      // In a real application, replace this with your actual API call
      // const response = await api.post('/predictions', cropData);
      // setPrediction(response.data);
      setPrediction({ yield: Math.floor(Math.random() * 100) + 1 })
      setError('')
    } catch (err) {
      setError('Failed to get prediction')
    }
  }

  return (
    <div className="min-h-screen bg-cover bg-center flex items-center justify-center p-4" style={{backgroundImage: "url('https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2340&q=80')"}}>
      <div className="w-full max-w-md bg-white/90 backdrop-blur-sm shadow-xl rounded-lg p-6">
        <h2 className="text-2xl font-bold text-center text-green-800 mb-6">Crop Yield Prediction</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <label htmlFor="soil_type" className="block text-sm font-medium text-gray-700">Soil Type</label>
            <input
              id="soil_type"
              className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500"
              placeholder="e.g., Clay, Sandy, Loam"
              value={cropData.soil_type}
              onChange={(e) => setCropData({ ...cropData, soil_type: e.target.value })}
            />
          </div>
          <div className="space-y-2">
            <label htmlFor="weather_conditions" className="block text-sm font-medium text-gray-700">Weather Conditions</label>
            <input
              id="weather_conditions"
              className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500"
              placeholder="e.g., Sunny, Rainy, Cloudy"
              value={cropData.weather_conditions}
              onChange={(e) => setCropData({ ...cropData, weather_conditions: e.target.value })}
            />
          </div>
          <div className="space-y-2">
            <label htmlFor="irrigation_level" className="block text-sm font-medium text-gray-700">Irrigation Level (mm)</label>
            <input
              id="irrigation_level"
              type="number"
              className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500"
              placeholder="e.g., 50"
              value={cropData.irrigation_level}
              onChange={(e) => setCropData({ ...cropData, irrigation_level: e.target.value })}
            />
          </div>
          <div className="space-y-2">
            <label htmlFor="fertilizers_used" className="block text-sm font-medium text-gray-700">Fertilizers Used (kg/ha)</label>
            <input
              id="fertilizers_used"
              type="number"
              className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500"
              placeholder="e.g., 100"
              value={cropData.fertilizers_used}
              onChange={(e) => setCropData({ ...cropData, fertilizers_used: e.target.value })}
            />
          </div>
          <button 
            type="submit"
            className="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
          >
            Predict Yield
          </button>
        </form>

        {error && <p className="text-red-600 mt-4">{error}</p>}

        {prediction && (
          <div className="mt-6 p-4 bg-green-100 rounded-lg">
            <h3 className="text-lg font-semibold text-green-800 mb-2">Prediction Result</h3>
            <p className="text-green-700">Estimated Yield: {prediction.yield} bushels per acre</p>
          </div>
        )}
      </div>
    </div>
  )
}
export default CropPrediction;