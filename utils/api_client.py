"""
Simple HTTP client for Binance API
"""
import requests
from config import BASE_URL, TIMEOUT


class BinanceClient:
    """Simple Binance API client"""
    
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
    
    def get(self, endpoint, params=None):
        """Send GET request to Binance API"""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, timeout=self.timeout)
        return response
