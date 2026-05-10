from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Ojas DevOps Portfolio</h1><p>Built with Flask, Docker, and GitHub Actions</p>'

@app.route('/health')
def health():
    return {'status': 'healthy'}

@app.route('/metrics')
def metrics():
    with open('data.json') as f:
     data = json.load(f)
    return data

@app.route('/predict')
def predict():
     with open('data.json') as f:
       data = json.load(f)
    
     files_remaining = data['total_files'] - data['remediated']
     daily_rate = data['remediated'] / data['days_elapsed']
     days_remaining = files_remaining / daily_rate
    
     if days_remaining <= 10:
        status = "on track"
     else:
        status = "at risk"
    
     return {
        'days_remaining': round(days_remaining, 1),
        'status': status
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
