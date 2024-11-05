# src/model_building.py
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
import joblib

def train_arima(data):
    model = ARIMA(data['Price'], order=(5,1,0))
    results = model.fit()
    joblib.dump(results, '../models/baseline/arima_model.pkl')
    return results

def train_garch(data):
    model = arch_model(data['Price_Change'].dropna(), vol='Garch', p=1, q=1)
    results = model.fit()
    joblib.dump(results, '../models/baseline/garch_model.pkl')
    return results

# Example usage
if __name__ == '__main__':
    data = pd.read_csv('C:\\Users\\1221\\Desktop\\Acadamy AIM 2\\Time-series-data-modeling-\\data\\processed\\processed_brent_oil_prices.csv', parse_dates=['DATE'])
    train_arima(data)
    train_garch(data)
