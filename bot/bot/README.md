# Binance Futures Testnet Trading Bot

## Setup

1. Install Python 3.x
2. Install dependencies

pip install -r requirements.txt

3. Set environment variables

Windows:

set BINANCE_API_KEY=your_key  
set BINANCE_API_SECRET=your_secret

## Run

### MARKET order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000

## Features

- MARKET & LIMIT orders
- CLI input validation
- Logging
- Error handling

## Assumptions

- Using Binance Futures Testnet
- API keys provided via environment variables
