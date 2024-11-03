// dashboard/frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

function App() {
  const [priceData, setPriceData] = useState([]);
  const [predictions, setPredictions] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/price-data')
      .then(response => setPriceData(response.data))
      .catch(error => console.error(error));

    axios.get('http://127.0.0.1:5000/model-predictions')
      .then(response => setPredictions(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Brent Oil Prices Dashboard</h1>
      <LineChart width={800} height={400} data={priceData}>
        <XAxis dataKey="Date" />
        <YAxis dataKey="Price" />
        <Tooltip />
        <CartesianGrid stroke="#f5f5f5" />
        <Line type="monotone" dataKey="Price" stroke="#ff7300" />
        <Line type="monotone" dataKey={predictions ? 'Predicted Price' : 'Price'} data={predictions} stroke="#387908" />
      </LineChart>
    </div>
  );
}

export default App;