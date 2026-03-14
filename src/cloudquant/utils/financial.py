"""
Financial utility functions.

This module provides common financial calculations used in quantitative trading.
"""

from collections.abc import Sequence

import numpy as np


def calculate_returns(prices: Sequence[float]) -> np.ndarray:
    prices_arr = np.array(prices, dtype=float)
    if len(prices_arr) < 2:
        return np.array([])
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


def calculate_max_drawdown(equity_curve: Sequence[float]) -> float:
    """
    Calculate the maximum drawdown from an equity curve.

    Args:
        equity_curve: Sequence of portfolio/equity values over time

    Returns:
        Maximum drawdown as a positive decimal (e.g., 0.20 = 20% drawdown)

    Example:
        >>> equity = [100, 110, 105, 95, 100]
        >>> max_dd = calculate_max_drawdown(equity)
        >>> abs(max_dd - 0.136) < 0.001  # ~13.6% drawdown
    """
    if not equity_curve:
        return 0.0

    equity = np.array(equity_curve, dtype=float)
    running_max = np.maximum.accumulate(equity)
    drawdown = (equity - running_max) / running_max
    return float(abs(np.min(drawdown)))
