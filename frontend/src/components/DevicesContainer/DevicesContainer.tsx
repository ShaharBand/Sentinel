import { Typography, useTheme } from "@mui/material";
import FileDownloadRoundedIcon from "@mui/icons-material/FileDownloadRounded";

import { getClasses } from "./style";

import DevicesTable from "../DevicesTable/DevicesTable";

const theme = useTheme();
const classes = getClasses(theme);

const DevicesContainer = () => {
  return (
    <div className={classes.TableContainer}>
      <div className="table-top-row">
        <div className="table-header">
          <Typography variant="h5">Devices</Typography>
          <Typography variant="subtitle2" className="subtitle">
            3,000 devices.
          </Typography>
        </div>
        <div className="table-tools">
          <FileDownloadRoundedIcon />
          <span>Report</span>
        </div>
      </div>

      <div className="table-content">
        <DevicesTable />
      </div>
    </div>
  );
};

export default DevicesContainer;
