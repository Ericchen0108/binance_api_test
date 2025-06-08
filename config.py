"""
Configuration settings for Binance API tests
"""

# API Configuration
BASE_URL = "https://api.binance.com"
TIMEOUT = 10
TEST_SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT']
INVALID_SYMBOLS = ['INVALIDCOIN', 'NOTEXIST', '123ABC', '']
