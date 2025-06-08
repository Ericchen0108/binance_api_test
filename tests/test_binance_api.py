"""
Binance API Test Cases
"""
import pytest
from config import TEST_SYMBOLS, INVALID_SYMBOLS

class TestBinanceAPI:
    """Binance API test suite"""
    
    @pytest.mark.parametrize("symbol", TEST_SYMBOLS)
    def test_get_ticker_price_success(self, client, validator, symbol):
        """
        Test Case: Get ticker price for valid symbols
        
        Steps:
        1. Send GET request to /api/v3/ticker/price with valid symbol
        2. Verify response status is 200
        3. Verify response contains symbol and price
        4. Verify price format is valid
        
        Expected Result:
        - Status code: 200
        - Response contains 'symbol' and 'price' fields
        - Price is positive number
        - Symbol matches request
        
        Validation:
        - HTTP status validates API success
        - Field validation ensures data completeness
        - Format validation ensures data quality
        """
        response = client.get("/api/v3/ticker/price", {"symbol": symbol})
        
        assert response.status_code == 200
        
        data = response.json()
        assert "symbol" in data
        assert "price" in data
        assert data["symbol"] == symbol
        assert validator.is_valid_price(data["price"])
    
    def test_get_all_ticker_prices(self, client, validator):
        """
        Test Case: Get all ticker prices
        
        Steps:
        1. Send GET request to /api/v3/ticker/price without parameters
        2. Verify response is array with multiple items
        3. Verify sample items have correct structure
        
        Expected Result:
        - Status code: 200
        - Response is array with 100+ items
        - Each item has symbol and price
        
        Validation:
        - Array validation ensures correct data structure
        - Sample validation ensures data quality
        """
        response = client.get("/api/v3/ticker/price")
        
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 100
        
        # Validate first 3 items
        for item in data[:3]:
            assert "symbol" in item
            assert "price" in item
            assert validator.is_valid_symbol(item["symbol"])
            assert validator.is_valid_price(item["price"])
    
    @pytest.mark.parametrize("symbol", INVALID_SYMBOLS)
    def test_get_ticker_price_invalid_symbol(self, client, symbol):
        """
        Test Case: Get ticker price with invalid symbols
        
        Steps:
        1. Send GET request with invalid symbol
        2. Verify error response
        
        Expected Result:
        - Status code: 400
        - Response contains error code and message
        
        Validation:
        - Error status validates proper error handling
        - Error structure validates API consistency
        """
        response = client.get("/api/v3/ticker/price", {"symbol": symbol})
        
        assert response.status_code == 400
        
        data = response.json()
        assert "code" in data
        assert "msg" in data
    
    def test_get_server_time(self, client, validator):
        """
        Test Case: Get server time
        
        Steps:
        1. Send GET request to /api/v3/time
        2. Verify response contains serverTime
        3. Verify time is reasonable
        
        Expected Result:
        - Status code: 200
        - Response contains serverTime
        - Time is within reasonable range
        
        Validation:
        - Field validation ensures API completeness
        - Range validation ensures data reasonableness
        """
        response = client.get("/api/v3/time")
        
        assert response.status_code == 200
        
        data = response.json()
        assert "serverTime" in data
        assert isinstance(data["serverTime"], int)
        assert validator.is_time_reasonable(data["serverTime"])
    
    def test_get_exchange_info(self, client):
        """
        Test Case: Get exchange information
        
        Steps:
        1. Send GET request to /api/v3/exchangeInfo
        2. Verify response structure
        3. Verify symbols array
        
        Expected Result:
        - Status code: 200
        - Response contains required fields
        - Symbols array is not empty
        
        Validation:
        - Structure validation ensures API completeness
        - Content validation ensures meaningful data
        """
        response = client.get("/api/v3/exchangeInfo")
        
        assert response.status_code == 200
        
        data = response.json()
        assert "timezone" in data
        assert "serverTime" in data
        assert "symbols" in data
        assert len(data["symbols"]) > 0
    
    def test_invalid_endpoint(self, client):
        """
        Test Case: Access invalid endpoint
        
        Steps:
        1. Send GET request to non-existent endpoint
        2. Verify 404 response
        
        Expected Result:
        - Status code: 404
        
        Validation:
        - 404 status validates proper routing
        """
        response = client.get("/api/v3/invalid_endpoint")
        
        assert response.status_code == 404 