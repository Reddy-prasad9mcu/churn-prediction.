import azure.functions as func
import joblib
import pandas as pd
import sqlite3

# Load model
model = joblib.load('churn_model.pkl')

def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    data = [[req_body['usage_hours'], req_body['support_calls'], req_body['payment_delay']]]

    # Predict
    prediction = model.predict(pd.DataFrame(data, columns=['usage_hours', 'support_calls', 'payment_delay']))

    # Store in SQLite
    conn = sqlite3.connect('churn_predictions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO ChurnPredictions (usage_hours, support_calls, payment_delay, prediction)
        VALUES (?, ?, ?, ?)
    ''', (data[0][0], data[0][1], data[0][2], int(prediction[0])))
    conn.commit()
    conn.close()

    return func.HttpResponse(f"Prediction: {prediction[0]}", status_code=200)
