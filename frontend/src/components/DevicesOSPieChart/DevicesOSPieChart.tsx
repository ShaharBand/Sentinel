import { PieChart } from "@mui/x-charts/PieChart";
import "./style.css";

const DeviceOSPieChart = () => {
  const series = [
    {
      data: [
        { name: "Windows", value: 30 },
        { name: "MacOS", value: 25 },
        { name: "Linux", value: 20 },
        { name: "iOS", value: 15 },
        { name: "Android", value: 10 },
      ],
      innerRadius: 65,
      outerRadius: 100,
      paddingAngle: 5,
      cornerRadius: 5,
      startAngle: -90,
      endAngle: 180,
      cx: 150,
      cy: 150,
    },
  ];

  return (
    <div className="chart-container">
      <PieChart series={series} />{" "}
    </div>
  );
};

export default DeviceOSPieChart;
