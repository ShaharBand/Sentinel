<div align="center">
  <img src="./logo.png" width="250px" alt="Sentinel Logo" title="Sentinel Logo">
</div>

# Sentinel

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ShaharBand/Sentinel/blob/main/LICENSE)
[![Downloads](https://img.shields.io/github/downloads/ShaharBand/Sentinel/total.svg)](https://github.com/ShaharBand/Sentinel/releases)
[![GitHub repo size](https://img.shields.io/github/repo-size/ShaharBand/Sentinel.svg)](https://github.com/ShaharBand/Sentinel)
[![stars](https://img.shields.io/github/stars/ShaharBand/Sentinel.svg?style=badge)](https://github.com/ShaharBand/Sentinel/stargazers)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![last commit](https://img.shields.io/github/last-commit/ShaharBand/Sentinel.svg)](https://github.com/ShaharBand/Sentinel/commits/main)
[![Tests](https://github.com/ShaharBand/Sentinel/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/ShaharBand/Sentinel/actions/workflows/tests.yml)

A user-friendly Command & Control (C&C) web platform for remote monitoring, management, and task automation across multiple devices.
Equipped with agents, it enables users to seamlessly execute scripted tasks on target devices, empowering efficient data retrieval and remote actions.

<br>

## 🖥️ Technologies:

Agents Implementation: not implemented yet.

### Backend:

[FastAPI](https://github.com/tiangolo/fastapi),
[MongoDB](https://github.com/mongodb/mongo),
[Pydantic](https://github.com/samuelcolvin/pydantic),
[Beanie](https://github.com/roman-right/beanie).

### Frontend:

[ReactJS](https://github.com/facebook/react),
[ViteJS](https://github.com/vitejs/vite),
[TypeScript](https://github.com/microsoft/TypeScript),
[Material UI](https://github.com/mui/material-ui),
[EmotionJS](https://github.com/emotion-js/emotion).

<br>

## 🌱 Getting Started:

**1. Clone the repository:**

```commandline
https://github.com/ShaharBand/Sentinel.git
```

<br>

**2. Install Backend Dependencies:**

Navigate to the `backend` directory and install the backend dependencies using the following command:

```commandline
cd backend
pip install -r requirements.txt
```

<br>

**3. Install Frontend Dependencies:**

Before installing the Node Package Manager (NPM), you need to install Node.js.
You can download the latest version of Node.js from the official Node.js website.
<br>

Navigate to the frontend directory and install the frontend dependencies using the following command:

```commandline
cd frontend
npm install
```

This command installs the necessary Node.js packages specified in your project's `package.json` file.
<br><br>

**4. Modify the configuration settings:**

Update the configuration settings in `config.py` located in the backend directory.
<br><br>

**5. Run Backend**

In the `backend` directory, run the FastAPI backend using the following command:

```commandline
python main.py
```

<br>

**6. Run Frontend:**

In the `frontend` directory, run the Vite.js frontend using the following command:

```commandline
npm run dev
```

<br>

## 👨‍💻 Contributions:

We welcome contributions to this project! Please feel free to fork the repository and create pull requests.
<br><br>

## 💼 License:

This project is licensed under the MIT License.
