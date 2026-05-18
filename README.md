# devops-project
# Migration Health Dashboard

## What it does
Tracks the status of the migration activity.

## Tech Stack
- Python / Flask
- Scikit-learn (Linear Regression)
- Docker
- GitHub Actions CI/CD
- Deployed on Render

## Live Demo
https://migration-healthboard.onrender.com/

## API Endpoints
- GET / — Dashboard UI
- GET /metrics — Migration metrics
- GET /predict — ML prediction
- GET /health — Health check

## How to run locally
1. Clone the repo
2. cd app
3. pip install -r requirements.txt
4. python app.py