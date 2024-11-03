# dashboard/backend/app.py
from flask import Flask, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/price-data', methods=['GET'])
def get_price_data():
    data = pd.read_csv('../../data/processed/feature_data.csv').to_dict(orient='records')
    return jsonify(data)

@app.route('/model-predictions', methods=['GET'])
def get_model_predictions():
    arima_model = joblib.load('../../models/baseline/arima_model.pkl')
    predictions = arima_model.forecast(steps=30)  # Example: 30 days prediction
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
