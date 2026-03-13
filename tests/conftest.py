"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_prices():
    """Sample price data for testing."""
    return [100.0, 102.0, 101.0, 105.0, 103.0, 107.0]


@pytest.fixture
def sample_returns():
    """Sample return data for testing."""
    return [0.01, -0.005, 0.02, 0.015, -0.008, 0.012]
