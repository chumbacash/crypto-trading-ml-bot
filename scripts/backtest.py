import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Load the data and model
data = pd.read_csv('data/historical_data.csv', parse_dates=['date'])
data.set_index('date', inplace=True)
data['dummy_feature'] = data['close'].shift(1).fillna(method='bfill')
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# Create sequences
def create_sequences(data, seq_length):
    xs, ys = [], []
    for i in range(len(data) - seq_length):
        x = data[i:i + seq_length]
        y = data[i + seq_length, 3]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

seq_length = 60
X, y = create_sequences(scaled_data, seq_length)

# Load the model
model = load_model('models/lstm_model.h5')

# Generate predictions
y_pred = model.predict(X)
y_pred_rescaled = scaler.inverse_transform(np.hstack((np.zeros((y_pred.shape[0], scaled_data.shape[1] - 1)), y_pred)))
y_rescaled = scaler.inverse_transform(np.hstack((np.zeros((y.shape[0], scaled_data.shape[1] - 1)), y.reshape(-1, 1))))

# Simulation
initial_capital = 500
capital = initial_capital
num_shares = 0
portfolio_values = []

for i in range(len(y_pred_rescaled) - 1):
    current_price = y_rescaled[i, -1]
    next_predicted_price = y_pred_rescaled[i + 1, -1]

    if next_predicted_price > current_price:
        num_shares = capital // current_price
        capital -= num_shares * current_price
    elif next_predicted_price < current_price and num_shares > 0:
        capital += num_shares * current_price
        num_shares = 0

    portfolio_value = capital + num_shares * current_price
    portfolio_values.append(portfolio_value)

final_portfolio_value = portfolio_values[-1]
total_profit = final_portfolio_value - initial_capital
return_percentage = (total_profit / initial_capital) * 100

print(f'Initial Capital: ${initial_capital}')
print(f'Final Portfolio Value: ${final_portfolio_value:.2f}')
print(f'Total Profit: ${total_profit:.2f}')
print(f'Return Percentage: {return_percentage:.2f}%')

# Plot
plt.figure(figsize=(14, 7))
plt.plot(data.index[seq_length:-1], portfolio_values, color='green', label='Portfolio Value')
plt.title('Portfolio Value Over Time')
plt.xlabel('Date')
plt.ylabel('Portfolio Value (USD)')
plt.legend()
plt.show()
