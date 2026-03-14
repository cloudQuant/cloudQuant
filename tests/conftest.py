"""Pytest configuration and fixtures."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest


@pytest.fixture
def sample_prices():
    return [100.0, 102.0, 101.0, 105.0, 103.0, 107.0]


@pytest.fixture
def sample_returns():
    return [0.01, -0.005, 0.02, 0.015, -0.008, 0.012]


@pytest.fixture
def sample_market_data():
    return [
        {"symbol": "AAPL", "timestamp": None, "close": 100.0, "volume": 1000},
        {"symbol": "AAPL", "timestamp": None, "close": 102.0, "volume": 1100},
        {"symbol": "AAPL", "timestamp": None, "close": 101.0, "volume": 900},
        {"symbol": "AAPL", "timestamp": None, "close": 105.0, "volume": 1200},
    ]
