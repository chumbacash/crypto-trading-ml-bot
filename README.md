# Crypto Trading Bot

This repository contains code for a cryptocurrency trading bot that uses an LSTM model to predict future prices and make trading decisions. The bot can be backtested using historical data and is designed to learn and improve over time.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Training the Model](#training-the-model)
- [Backtesting the Model](#backtesting-the-model)
- [Live Trading](#live-trading)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/chumbacash/crypto-ml-trading-bot.git
    cd crypto-trading-ml-bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Files

- `data/data.csv`: The historical cryptocurrency data file.
- `models/lstm_model.h5`: The pre-trained LSTM model.
- `scripts/train_model.py`: Script to train the model.
- `scripts/backtest.py`: Script to backtest the trading strategy.
- `scripts/live_trading_bot.py`: Script for live trading (optional).

### Training the Model

To train the model, run the `train_model.py` script. Ensure you have the historical data in the `data` folder.

    ```bash
    pip install -r requirements.txt
    ```

### Backtesting the Model

To backtest the model, run the `backtest.py` script. This will simulate trading on historical data and output the performance metrics.

    ```bash
    pip install -r requirements.txt
    ```


### Live Trading
For live trading, you can use the `live_trading_bot.py` script (optional). Note that this script is a template and will need to be customized with your trading platform API details.

    ```bash
    pip install -r requirements.txt
    ```
### By Chumbacash ✌🌷
This is not a financial advice whatsoever, I create it for fun TF!
