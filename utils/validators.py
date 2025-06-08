"""
Data validation utilities
"""
import re
from typing import Dict, Any, List
from datetime import datetime

class Validator:
    """Data validation helper"""
    
    @staticmethod
    def is_valid_price(price_str):
        """Check if price is valid number"""
        try:
            price = float(price_str)
            return price > 0
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_valid_symbol(symbol):
        """Check if symbol follows trading pair format"""
        pattern = r'^[A-Z]{3,10}(USDT|BTC|ETH|BNB)$'
        return bool(re.match(pattern, symbol))
    
    @staticmethod
    def is_time_reasonable(timestamp):
        """Check if timestamp is within reasonable range"""
        current_time = int(datetime.now().timestamp() * 1000)
        time_diff = abs(current_time - timestamp)
        return time_diff < 300000  # 5 minutes
