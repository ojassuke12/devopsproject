import numpy as np
from sklearn.linear_model import LinearRegression

# Fake historical migration data
# [files_total, remediated, errors_found] -> days_taken
X_train = np.array([
    [100, 80, 5],
    [200, 150, 10],
    [50, 40, 2],
    [300, 200, 20],
    [150, 100, 8],
    [80, 60, 4],
])

y_train = np.array([30, 60, 15, 90, 45, 25])

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

def predict_completion(total_files, remediated, errors_found):
    features = np.array([[total_files, remediated, errors_found]])
    days = model.predict(features)[0]
    days = round(float(days), 1)
    status = "on track" if days <= 30 else "at risk"
    return {
        "predicted_days": days,
        "status": status
    }