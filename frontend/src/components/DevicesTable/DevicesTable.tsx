import React, { useState } from "react";
import { DataGrid, GridCellParams, GridColDef } from "@mui/x-data-grid";

import "./style.css";

const getStatusClassName = (status: string) => {
  if (status === "Available") return "available-status";
  if (status === "Unavailable") return "unavailable-status";
  // Add more conditions if needed
  return "";
};

const renderStatusCell = (params: GridCellParams) => {
  const { value } = params;
  const statusValue = value as string;
  const className = getStatusClassName(statusValue);
  return <div className={className}>{statusValue}</div>;
};

const DevicesTable: React.FC = () => {
  const [rows, setRows] = useState([
    {
      id: 1,
      name: "Computer A",
      description: "Desktop",
      ipAddress: "192.168.0.1",
      os: "Windows",
      status: "Available",
    },
    {
      id: 2,
      name: "Computer B",
      description: "Laptop",
      ipAddress: "192.168.0.2",
      os: "MacOS",
      status: "Unavailable",
    },
    {
      id: 3,
      name: "Computer C",
      description: "Desktop",
      ipAddress: "192.168.0.3",
      os: "Linux",
      status: "Available",
    },
    {
      id: 4,
      name: "Computer D",
      description: "Desktop",
      ipAddress: "192.168.0.4",
      os: "Linux",
      status: "Available",
    },
    {
      id: 5,
      name: "Computer E",
      description: "Desktop",
      ipAddress: "192.168.0.5",
      os: "Linux",
      status: "Available",
    },
    {
      id: 6,
      name: "Computer F",
      description: "Desktop",
      ipAddress: "192.168.0.6",
      os: "Windows",
      status: "Available",
    },
    {
      id: 7,
      name: "Computer G",
      description: "Desktop",
      ipAddress: "192.168.0.7",
      os: "Windows",
      status: "Available",
    },
    {
      id: 8,
      name: "Computer H",
      description: "Desktop",
      ipAddress: "192.168.0.8",
      os: "Windows",
      status: "Available",
    },
    {
      id: 9,
      name: "Computer I",
      description: "Desktop",
      ipAddress: "192.168.0.9",
      os: "Windows",
      status: "Available",
    },
    {
      id: 10,
      name: "Computer J",
      description: "Desktop",
      ipAddress: "192.168.0.10",
      os: "Windows",
      status: "Available",
    },
    {
      id: 9,
      name: "Computer I",
      description: "Desktop",
      ipAddress: "192.168.0.9",
      os: "Windows",
      status: "Available",
    },
    // Add more data as needed
  ]);

  return (
    <div style={{ height: "inherit", width: "100%" }}>
      <DataGrid
        rows={rows}
        columns={columns}
        className="custom-datagrid"
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 9,
            },
          },
        }}
        pageSizeOptions={[9]}
        disableRowSelectionOnClick
        pagination
      />
    </div>
  );
};

export default DevicesTable;

const columns: GridColDef[] = [
  { field: "id", headerName: "ID", width: 90 },
  { field: "name", headerName: "Name", width: 170 },
  { field: "description", headerName: "Description", width: 200 },
  { field: "ipAddress", headerName: "IP Address", width: 120 },
  { field: "os", headerName: "Operating System", width: 160 },
  {
    field: "status",
    headerName: "Status",
    width: 170,
    renderCell: renderStatusCell,
  },
  {
    field: "options",
    headerName: "Options",
    width: 100,
    renderCell: (params: GridCellParams) => {
      return <a className="hyper-link">More</a>;
    },
  },
];
