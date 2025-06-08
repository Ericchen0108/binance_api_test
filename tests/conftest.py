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


def pytest_configure(config):
    """pytest configuration"""
    config.addinivalue_line(
        "markers", "smoke: Smoke tests for critical functionality"
    )
    config.addinivalue_line(
        "markers", "regression: Regression tests for full coverage"
    )
    config.addinivalue_line(
        "markers", "negative: Negative test scenarios"
    ) 