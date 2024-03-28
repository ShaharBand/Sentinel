import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Typography } from "@mui/material";
import PhonelinkRoundedIcon from "@mui/icons-material/PhonelinkRounded";
import TerminalRoundedIcon from "@mui/icons-material/TerminalRounded";
import LayersRoundedIcon from "@mui/icons-material/LayersRounded";
import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";
import ExitToAppIcon from "@mui/icons-material/ExitToApp";
import logo from "../../assets/images/logo.png";
import { NavLinkProps } from "./types";
import "./style.css";

const NavLink: React.FC<NavLinkProps> = ({
  to,
  icon,
  label,
  selected,
  onClick,
}) => (
  <Link
    to={to}
    className={`nav-link ${selected ? "selected" : ""}`}
    onClick={onClick}
  >
    {React.cloneElement(icon)}
    <Typography>{label}</Typography>
  </Link>
);

const NavigationBar: React.FC = () => {
  const [selectedPage, setSelectedPage] = useState("/");

  const handleNavLinkClick = (to: string) => {
    setSelectedPage(to);
  };

  return (
    <nav className="navbar-container">
      <div className="logo-container">
        <img src={logo} alt="Logo" className="logo-img" />
        <Typography className="logo-label">Sentinel</Typography>
      </div>
      <div className="navlinks-container">
        <NavLink
          to="/"
          icon={<PhonelinkRoundedIcon />}
          label="Devices"
          selected={selectedPage === "/"}
          onClick={() => handleNavLinkClick("/")}
        />
        <NavLink
          to="/agents"
          icon={<TerminalRoundedIcon />}
          label="Agents"
          selected={selectedPage === "/agents"}
          onClick={() => handleNavLinkClick("/agents")}
        />
        <NavLink
          to="/actions"
          icon={<LayersRoundedIcon />}
          label="Actions"
          selected={selectedPage === "/actions"}
          onClick={() => handleNavLinkClick("/actions")}
        />
        <NavLink
          to="/settings"
          icon={<SettingsRoundedIcon />}
          label="Settings"
          selected={selectedPage === "/settings"}
          onClick={() => handleNavLinkClick("/settings")}
        />

        <div className="navlinks-bottom">
          <NavLink
            to="/logout"
            icon={<ExitToAppIcon />}
            label="Logout"
            selected={selectedPage === "/logout"}
            onClick={() => handleNavLinkClick("/logout")}
          />
        </div>
      </div>
    </nav>
  );
};

export default NavigationBar;
