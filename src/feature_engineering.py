
# src/feature_engineering.py
import pandas as pd

def add_features(input_path, output_path):
    data = pd.read_csv(input_path, parse_dates=['date'])
    data['Price_Change'] = data['Price'].pct_change()
    data['Rolling_Mean'] = data['Price'].rolling(window=30).mean()
    data['Rolling_Std'] = data['Price'].rolling(window=30).std()
    data.to_csv(output_path, index=False)
    return data

# usage
if __name__ == '__main__':
    add_features('C:\\Users\\1221\\Desktop\\Acadamy AIM 2\\Time-series-data-modeling-\\data\\processed\\processed_brent_oil_prices.csv', 
                 'C:\\Users\\1221\\Desktop\\Acadamy AIM 2\\Time-series-data-modeling-\\data\\processed\\processed_brent_oil_prices.csv')
