import DevicesContainer from "../../components/DevicesContainer/DevicesContainer";
import DevicesOSPieChart from "../../components/DevicesOSPieChart/DevicesOSPieChart";
import Layout from "../Layout/Layout";
import "./style.css";

const DevicesPage = () => {
  return (
    <Layout title="Overview">
      <div className="layout">
        <DevicesContainer />
        <div className="column">
          <DevicesOSPieChart />
          <DevicesOSPieChart />
        </div>
      </div>
    </Layout>
  );
};

export default DevicesPage;
