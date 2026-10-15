# Finnhub API Tool
This project is the first effort to set up an API to Finnhub. Features will evolve as follows:

## Feature List:

| #    | DESCRITPION                     | Priority |
| :--- | :------------------------------ | -------: |
| 1    | Pull Data in real time from API | 1        |
| 2    | Display the Data                | 2        |

# Market Pulse CLI

A lightweight Python CLI utility that fetches real-time US market index ETF quotes (`QQQ`, `DIA`, `SPY`) via the Finnhub REST API and saves normalized snapshots locally.

## Prerequisites
* Python 3.10+
* A free [Finnhub API Key](https://finnhub.io/)

## Environment Setup (`venv`)

1. **Clone the repository and navigate to the project root:**
   ```bash
   git clone <your-repo-url>
   cd market-pulse-cli

Create and activate an isolated virtual environment:

Note: If using Conda, run conda deactivate first.

Linux / macOS / Codespaces:
python3 -m venv .venv
source .venv/bin/activate

## pip install --upgrade pip
pip install --upgrade pip
pip install -r requirements.txt

## For Development (Testing, Linting & PyInstaller Packaging):
pip install --upgrade pip
pip install -r requirements-dev.txt

## Configure API Credentials:
Copy the example environment file and add your Finnhub API key:
cp .env.example .env

When finished working, exit the virtual environment by running:
deactivate
