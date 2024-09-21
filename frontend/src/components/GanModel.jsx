import React, { useState } from 'react';

const GANModel = () => {
  const [data, setData] = useState(null);
  const [trainingProgress, setTrainingProgress] = useState(0);
  const [generatedSamples, setGeneratedSamples] = useState([]);
  const [message, setMessage] = useState('');

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = async (e) => {
      const content = e.target.result;
      const parsedData = JSON.parse(content);

      try {
        const response = await fetch('/upload_data', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ data: parsedData }),
        });

        if (response.ok) {
          const result = await response.json();
          setData(result);
          setMessage(`Data uploaded successfully. Shape: ${result.shape}`);
        } else {
          setMessage('Error uploading data');
        }
      } catch (error) {
        setMessage(`Error: ${error.message}`);
      }
    };

    reader.readAsText(file);
  };

  const handleTrain = async () => {
    try {
      const response = await fetch('/train', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ epochs: 10000, batch_size: 32 }),
      });

      if (response.ok) {
        setMessage('Training completed');
        for (let i = 0; i <= 100; i++) {
          setTrainingProgress(i);
          await new Promise(resolve => setTimeout(resolve, 100));
        }
      } else {
        setMessage('Error during training');
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    }
  };

  const handleGenerate = async () => {
    try {
      const response = await fetch('/generate?num_samples=5');
      if (response.ok) {
        const result = await response.json();
        setGeneratedSamples(result.generated_data);
        setMessage('Samples generated successfully');
      } else {
        setMessage('Error generating samples');
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '20px' }}>GAN Model Interface</h1>
      
      <div style={{ marginBottom: '20px' }}>
        <input type="file" onChange={handleFileUpload} accept=".json" />
      </div>

      <div style={{ marginBottom: '20px' }}>
        <button onClick={handleTrain} disabled={!data} style={{ padding: '10px 20px', backgroundColor: data ? '#4CAF50' : '#ddd', color: 'white', border: 'none', cursor: data ? 'pointer' : 'default' }}>
          Train Model
        </button>
      </div>

      {trainingProgress > 0 && (
        <div style={{ marginBottom: '20px' }}>
          <progress value={trainingProgress} max="100" style={{ width: '100%' }}></progress>
        </div>
      )}

      <div style={{ marginBottom: '20px' }}>
        <button onClick={handleGenerate} disabled={trainingProgress < 100} style={{ padding: '10px 20px', backgroundColor: trainingProgress === 100 ? '#2196F3' : '#ddd', color: 'white', border: 'none', cursor: trainingProgress === 100 ? 'pointer' : 'default' }}>
          Generate Samples
        </button>
      </div>

      {message && (
        <div style={{ marginBottom: '20px', padding: '10px', backgroundColor: '#f1f1f1', border: '1px solid #ddd' }}>
          {message}
        </div>
      )}

      {generatedSamples.length > 0 && (
        <div>
          <h2 style={{ fontSize: '20px', fontWeight: 'semibold', marginBottom: '10px' }}>Generated Samples:</h2>
          <pre style={{ backgroundColor: '#f1f1f1', padding: '10px', borderRadius: '4px', overflowX: 'auto' }}>
            {JSON.stringify(generatedSamples, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default GANModel;