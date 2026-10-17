# RapidRelief AI

**Real-Time Emergency Resource Prioritization — IBM Z Datathon 2026**

## Problem
During emergencies, teams may receive multiple reports and need help identifying which unresolved incidents to review first.

## Solution
RapidRelief AI is a prototype that reads emergency reports from a CSV file, calculates an illustrative priority score, ranks unresolved incidents, and displays them on a web dashboard.

## Features
- Reads reports from `emergency_reports.csv`
- Ranks unresolved incidents by priority score
- Displays urgent cases on a dashboard
- Shows a summary of emergency reports

## Technology
- Python
- CSV data processing
- HTML dashboard served using Python
- IBM LinuxONE development environment
- Git and GitHub

## Run the Project
Run the command-line prototype:

```bash
python3 main.py
```

Run the dashboard:

```bash
python3 dashboard.py
```

Open `http://127.0.0.1:8000` in a browser where the server port is accessible.

## Data and Limitations
The included reports are fictional demonstration data. The priority score is illustrative and has not been clinically or operationally validated. This prototype is not intended for real-world emergency dispatch or medical decision-making.

## Repository
https://github.com/ramya-0609/RapidRelief-AI
