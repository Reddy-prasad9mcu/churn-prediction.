import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample data (replace with real data)
data = {
    'usage_hours': [12, 45, 2, 30, 5, 60],
    'support_calls': [3, 1, 5, 2, 4, 0],
    'payment_delay': [1, 0, 3, 0, 2, 0],
    'churn': [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
X = df.drop('churn', axis=1)
y = df['churn']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'churn_model.pkl')
