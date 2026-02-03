export default function MetricCard({ title, value, unit }) {
  return (
    <div className="card metric-card">
      <p className="metric-title">{title}</p>
      <h2>
        {value} <span>{unit}</span>
      </h2>
    </div>
  );
}
