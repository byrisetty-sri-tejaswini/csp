import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/sensor")
      .then(response => setSensorData(response.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Water Quality Monitoring Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>pH</th>
            <th>Turbidity</th>
            <th>Temperature</th>
            <th>TDS</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {sensorData.map((data, index) => (
            <tr key={index}>
              <td>{data.ph}</td>
              <td>{data.turbidity}</td>
              <td>{data.temperature}</td>
              <td>{data.tds}</td>
              <td>{data.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
