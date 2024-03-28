import React from "react";
import Brightness3RoundedIcon from "@mui/icons-material/Brightness3Rounded";
import PersonRoundedIcon from "@mui/icons-material/PersonRounded";

import { TopBarProps } from "./types";
import "./style.css";
import Typography from "@mui/material/Typography/Typography";

const TopBar: React.FC<TopBarProps> = ({ title }) => (
  <div className="top-bar-container">
    <Typography variant="h4" className={"title"}>
      {title}
    </Typography>
    <div className="right-container">
      <Brightness3RoundedIcon />
      <PersonRoundedIcon />
    </div>
  </div>
);

export default TopBar;
