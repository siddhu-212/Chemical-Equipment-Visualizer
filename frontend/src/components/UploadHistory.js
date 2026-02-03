import React from "react";
import "../styles/dashboard.css";

function UploadHistory({ history }) {
  if (history.length === 0) return null;

  return (
    <div className="card history-card">
      <h3>Recent Uploads</h3>

      <table className="history-table">
        <thead>
          <tr>
            <th>File Name</th>
            <th>Equipment</th>
            <th>Uploaded At</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {history.map((item, index) => (
            <tr key={index}>
              <td>{item.fileName}</td>
              <td>{item.total}</td>
              <td>{item.time}</td>
              <td className="status-ok">{item.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default UploadHistory;
