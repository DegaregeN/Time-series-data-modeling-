import os
from flask import Flask, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Use absolute paths
data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/processed_brent_oil_prices.csv')
model_path = os.path.join(os.path.dirname(__file__), '../../models/baseline/arima_model.pkl')

@app.route('/price-data', methods=['GET'])
def get_price_data():
    data = pd.read_csv(data_path).to_dict(orient='records')
    return jsonify(data)

@app.route('/model-predictions', methods=['GET'])
def get_model_predictions():
    arima_model = joblib.load(model_path)
    predictions = arima_model.forecast(steps=30)  # Example: 30 days prediction
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    #app.run(debug=True)