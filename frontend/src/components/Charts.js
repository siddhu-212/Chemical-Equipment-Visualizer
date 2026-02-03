import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

export default function Charts({ data }) {
  const labels = Object.keys(data);
  const values = Object.values(data);

  return (
    <div style={{ width: "360px", margin: "0 auto" }}>
      <Pie
        data={{
          labels,
          datasets: [
            {
              data: values,
              backgroundColor: [
                "#2563eb",
                "#16a34a",
                "#f59e0b",
                "#9333ea",
                "#dc2626",
                "#0ea5e9",
              ],
              borderWidth: 2,
            },
          ],
        }}
        options={{
          responsive: true,
          maintainAspectRatio: true,
          plugins: {
            legend: {
              position: "bottom",
              labels: {
                boxWidth: 14,
                padding: 15,
              },
            },
          },
        }}
      />
    </div>
  );
}
