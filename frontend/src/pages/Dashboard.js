import { useState } from "react";
import "../styles/dashboard.css";
import UploadCard from "../components/UploadCard";
import MetricCard from "../components/MetricCard";
import Charts from "../components/Charts";

export default function Dashboard() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [uploadHistory, setUploadHistory] = useState([]);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/api/upload/", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      alert("Backend not running");
    }
    setLoading(false);
  };

  return (
  <div className="dashboard-page">
    <div className="dashboard-container">
        <div className="dashboard-header">
          <h1>Chemical Equipment Visualizer</h1>
          <p>Data Analysis Dashboard</p>
        </div>


        <div className="top-grid">
          <UploadCard
            file={file}
            setFile={setFile}
            uploadFile={uploadFile}
            loading={loading}
          />

          {result && (
            <div className="metrics-grid">
              <MetricCard title="Total Equipment" value={result.total_equipment} />
              <MetricCard title="Avg Flowrate" value={result.avg_flowrate} unit="L/min" />
              <MetricCard title="Avg Pressure" value={result.avg_pressure} unit="bar" />
              <MetricCard title="Avg Temperature" value={result.avg_temperature} unit="°C" />
            </div>
          )}
        </div>

        {result && (
          <div className="chart-card">
            <h2>Equipment Type Distribution</h2>
            <Charts data={result.type_distribution} />
          </div>
        )}
      </div>
    </div>
  );
}
