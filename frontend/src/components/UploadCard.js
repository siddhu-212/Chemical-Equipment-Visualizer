export default function UploadCard({ file, setFile, uploadFile, loading }) {
  return (
    <div className="card upload-card">
      <h3>Upload Equipment Data</h3>
      <p>Upload a CSV file to analyze chemical equipment parameters.</p>

      <label className="upload-box">
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <span>{file ? file.name : "Drop CSV here or click to browse"}</span>
      </label>

      <button onClick={uploadFile} disabled={loading}>
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </button>
    </div>
  );
}
