# Technical Requirements

This documentio will commit the standards for the inSight tool to allow users to
API into Finnhub and take advantage of the features of the tool.

# Project Requirements: Market Pulse CLI [inSight] (MVP)

## 1. Project Scope
Build a standalone command-line data ingestion tool that queries the Finnhub API for major market index ETF proxies (`QQQ`, `DIA`, `SPY`), normalizes the response payload, outputs a terminal summary, and persists the snapshot locally.

## 2. Functional Requirements
* **FR-1 (Auth & Config):** Load `FINNHUB_API_KEY` from a local `.env` file via `python-dotenv`.
* **FR-2 (Data Ingestion):** Query `GET https://finnhub.io/api/v1/quote` for configured ticker symbols (`QQQ`, `DIA`, `SPY`).
* **FR-3 (Normalization):** Extract and map raw Finnhub keys (`c`, `d`, `dp`, `h`, `l`, `o`, `pc`, `t`) into human-readable dictionary keys (`symbol`, `current_price`, `change`, `percent_change`, `high`, `low`, `open`, `prev_close`, `timestamp`).
* **FR-4 (Local Persistence):** Write the normalized payload to `data/market_snapshot.json`.
* **FR-5 (CLI Output):** Print a formatted summary of the fetched quotes to `stdout`.

## 3. Non-Functional & Environment Requirements
* **NFR-1 (Environment Isolation):** Project must use Python's standard `venv` module (`.venv/`), avoiding global or Conda base installations to ensure clean downstream PyInstaller bundling.
* **NFR-2 (Dependency Separation):** Runtime dependencies (`requests`, `python-dotenv`) must be isolated in `requirements.txt`. Development tools (`pytest`, `ruff`, `pyinstaller`) must be isolated in `requirements-dev.txt`.
* **NFR-3 (Resilience & Rate Limiting):** HTTP requests must include an explicit timeout (`10s`) and handle HTTP `429` (rate limit) and non-200 responses gracefully without crashing the batch loop.
* **NFR-4 (Security):** `.env` and `.venv/` must be excluded via `.gitignore`.

## 4. Out of Scope (Phase 1 MVP)
* Interactive TUI (Textual) interface.
* Automated cron/scheduled execution.
* LLM/Agent analysis integration.
