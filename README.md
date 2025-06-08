# Binance API Test Framework

Automated testing framework for Binance public APIs using Python and pytest.

## Project Structure

```
api_test/
├── __init__.py # Package initialization
├── config.py # Configuration settings
├── requirements.txt # Dependencies
├── pytest.ini # Pytest configuration
├── utils/
│ ├── ___init___.py # Utils package init
│ ├── api_client.py # HTTP client wrapper
│ └── validators.py # Data validation utilities
├── tests/
│ ├── __init____.py # Tests package init
│ ├── conftest.py # Pytest fixtures
│ └── test_binance_api.py # Main test cases
└── README.md # Documentation
```

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Run Tests

```bash
# All tests
python3 -m pytest

# With detailed output
python3 -m pytest -v

# Generate HTML report
python3 -m pytest --html=report.html --self-contained-html
```

## Test Cases

| Test Case          | Type     | Endpoint               | Purpose                           |
| ------------------ | -------- | ---------------------- | --------------------------------- |
| Valid ticker price | Positive | `/api/v3/ticker/price` | Test valid symbol price retrieval |
| All ticker prices  | Positive | `/api/v3/ticker/price` | Test bulk price data              |
| Invalid symbols    | Negative | `/api/v3/ticker/price` | Test error handling               |
| Server time        | Positive | `/api/v3/time`         | Test time endpoint                |
| Exchange info      | Positive | `/api/v3/exchangeInfo` | Test metadata endpoint            |
| Invalid endpoint   | Negative | `/api/v3/invalid`      | Test 404 handling                 |

## Validation Strategy

- **HTTP Status Codes**: Verify API success/failure
- **Response Structure**: Ensure required fields exist
- **Data Format**: Validate business data quality
- **Error Handling**: Confirm proper error responses

## Framework Features

- **Modular Design**: Separated concerns (client, validation, tests)
- **Parametrized Tests**: Data-driven testing for efficiency
- **Fixtures**: Reusable test components
- **Clear Documentation**: Each test has clear steps and expectations

## Test Documentation Format

Each test case follows this structure:

- **Clear Steps**: Numbered, specific actions
- **Expected Result**: Measurable outcomes
- **Validation Method**: How results are verified and why

## Reporting

### HTML Reports

```bash
python3 -m pytest --html=reports/report.html --self-contained-html
```

### Coverage Reports

```bash
pip install pytest-cov
python3 -m pytest --cov=utils --cov-report=html
```

## Requirements

- Python 3.9+
- Stable internet connection
- No API keys required (uses public endpoints)

## Important Notes

1. **Command Usage**: Must use `python3 -m pytest` (not just `pytest`)
2. **Public Endpoints**: Only uses Binance public APIs
3. **Rate Limits**: Be aware of API frequency limitations
4. **Live Data**: Test data changes in real-time
5. **Network Dependency**: Requires stable internet connection
