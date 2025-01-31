import sqlite3

# Create a SQLite database
conn = sqlite3.connect('churn_predictions.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS ChurnPredictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usage_hours INTEGER,
        support_calls INTEGER,
        payment_delay INTEGER,
        prediction INTEGER,
        prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()
