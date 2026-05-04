from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Ojas DevOps Portfolio</h1><p>Built with Flask, Docker, and GitHub Actions</p>'

@app.route('/health')
def health():
    return {'status': 'healthy'}

@app.route('/metrics')
def metrics():
    return {'total_files':  10,
            'remediated' :   8,
            'errors_found' : 2}

@app.route('/predict')
def predict():
     total_files = 10
     remediated = 8
     days_elapsed = 30
    
     files_remaining = total_files - remediated
     daily_rate = remediated / days_elapsed
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
