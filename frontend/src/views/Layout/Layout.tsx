import React from "react";
import NavigationBar from "../../components/NavigationBar/NavigationBar";
import TopBar from "../../components/TopBar/TopBar";
import { LayoutProps } from "./types";
import "./style.css";

const Layout: React.FC<LayoutProps> = ({ children, title }) => (
  <div className="page-container">
    <NavigationBar />
    <div className="content-container">
      <div className="content">
        <TopBar title={title} />
        {children}
      </div>
    </div>
  </div>
);

export default Layout;
