"""Tests for financial utilities."""

import pytest
import numpy as np
from cloudquant.utils.financial import calculate_returns, calculate_sharpe_ratio


def test_calculate_returns():
    """Test returns calculation."""
    prices = [100, 102, 101, 105]
    returns = calculate_returns(prices)
    
    assert len(returns) == len(prices)
    assert np.isnan(returns[0])  # First return is NaN
    assert np.isclose(returns[1], 0.02, atol=1e-6)
    assert np.isclose(returns[2], -0.0098, atol=1e-4)
    assert np.isclose(returns[3], 0.0396, atol=1e-4)


def test_calculate_returns_empty():
    """Test returns with empty array."""
    returns = calculate_returns([])
    assert len(returns) == 0


def test_calculate_sharpe_ratio():
    """Test Sharpe ratio calculation."""
    returns = [0.01, -0.005, 0.02, 0.015, 0.008]
    sharpe = calculate_sharpe_ratio(returns)
    
    assert isinstance(sharpe, float)
    # Sharpe ratio should be reasonable for positive mean returns
    assert sharpe > 0


def test_calculate_sharpe_ratio_with_nan():
    """Test Sharpe ratio handles NaN values."""
    returns = [np.nan, 0.01, -0.005, 0.02, np.nan, 0.015]
    sharpe = calculate_sharpe_ratio(returns)
    
    assert isinstance(sharpe, float)


def test_calculate_sharpe_ratio_empty():
    """Test Sharpe ratio with empty array."""
    sharpe = calculate_sharpe_ratio([])
    assert sharpe == 0.0


def test_calculate_sharpe_ratio_zero_std():
    """Test Sharpe ratio with zero standard deviation."""
    returns = [0.01, 0.01, 0.01, 0.01]
    sharpe = calculate_sharpe_ratio(returns)
    
    # Zero std should return 0
    assert sharpe == 0.0
