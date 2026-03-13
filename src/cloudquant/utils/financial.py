"""
Financial utility functions.

This module provides common financial calculations used in quantitative trading.
"""

from typing import Sequence
import numpy as np


def calculate_returns(prices: Sequence[float]) -> np.ndarray:
    """
    Calculate simple returns from price series.
    
    Args:
        prices: Sequence of prices
    
    Returns:
        Array of returns (first element is NaN)
    
    Example:
        >>> prices = [100, 102, 101, 105]
        >>> returns = calculate_returns(prices)
        >>> # returns = [nan, 0.02, -0.0098, 0.0396]
    """
    prices_arr = np.array(prices, dtype=float)
    returns = np.diff(prices_arr) / prices_arr[:-1]
    return np.concatenate([[np.nan], returns])


def calculate_sharpe_ratio(
    returns: Sequence[float],
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252,
) -> float:
    """
    Calculate the Sharpe ratio of a return series.
    
    Args:
        returns: Sequence of returns
        risk_free_rate: Annual risk-free rate (default: 0.0)
        periods_per_year: Number of periods per year (default: 252 for daily)
    
    Returns:
        Sharpe ratio
    
    Example:
        >>> returns = [0.01, -0.005, 0.02, 0.015]
        >>> sharpe = calculate_sharpe_ratio(returns)
    """
    returns_arr = np.array(returns, dtype=float)
    returns_arr = returns_arr[~np.isnan(returns_arr)]
    
    if len(returns_arr) == 0:
        return 0.0
    
    excess_returns = returns_arr - risk_free_rate / periods_per_year
    mean_excess = np.mean(excess_returns)
    std_returns = np.std(returns_arr, ddof=1)
    
    if std_returns == 0:
        return 0.0
    
    sharpe = (mean_excess * periods_per_year) / (std_returns * np.sqrt(periods_per_year))
    return float(sharpe)
