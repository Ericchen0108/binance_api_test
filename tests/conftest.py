"""
Test configuration and fixtures
"""
import pytest
from utils.api_client import BinanceClient
from utils.validators import Validator

@pytest.fixture
def client():
    """Binance API client"""
    return BinanceClient()

@pytest.fixture
def validator():
    """Data validator"""
    return Validator()

@pytest.fixture(scope="session")
def test_symbols():
    """Valid test symbols"""
    return ['BTCUSDT', 'ETHUSDT', 'ADAUSDT']

@pytest.fixture(scope="session")
def invalid_symbols():
    """Invalid test symbols"""
    return ['INVALIDCOIN', 'NOTEXIST', '123ABC', '']

# pytest配置
def pytest_configure(config):
    """pytest配置"""
    config.addinivalue_line(
        "markers", "smoke: 标记冒烟测试"
    )
    config.addinivalue_line(
        "markers", "regression: 标记回归测试"
    )
    config.addinivalue_line(
        "markers", "negative: 标记负面测试"
    ) 