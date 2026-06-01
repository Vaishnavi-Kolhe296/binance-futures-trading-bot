# Binance Futures Testnet Trading Bot

## Overview

This project is a Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- MARKET Orders
- LIMIT Orders
- BUY and SELL Support
- Input Validation
- Logging
- Error Handling
- Binance Futures Testnet Integration

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a .env file:

```env
API_KEY=your_api_key
API_SECRET=your_secret_key
```

## MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## Project Structure

trading_bot/

- client.py
- cli.py
- validators.py
- orders.py
- logging_config.py
- README.md
- requirements.txt
- .env

## Assumptions

- User has Binance Futures Testnet account
- Valid API keys are configured
- Testnet funds are available