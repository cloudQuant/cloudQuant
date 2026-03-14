"""
cloudQuant - AI-Powered Development Framework for quantitative trading systems.
"""

from cloudquant.config import (
    DEFAULT_COMMISSION_RATE,
    DEFAULT_INITIAL_CAPITAL,
    DEFAULT_LONG_WINDOW,
    DEFAULT_SHORT_WINDOW,
    DEFAULT_TRADE_SIZE,
    MIN_SHORT_WINDOW,
    RISK_FREE_RATE,
    TRADING_DAYS_PER_YEAR,
)
from cloudquant.core.engine import BacktestEngine
from cloudquant.data.loader import DataLoader, DataList
from cloudquant.strategy.base import Strategy
from cloudquant.types import (
    BacktestResult,
    BarData,
    DataProtocol,
    MarketData,
    Order,
    OrderSide,
    OrderType,
    Position,
    StrategyProtocol,
    TickData,
)

__version__ = "0.1.0"
__author__ = "cloudQuant Team"
__email__ = "yunjinqi@gmail.com"

__all__ = [
    "BacktestEngine",
    "DataLoader",
    "DataList",
    "Strategy",
    "BacktestResult",
    "BarData",
    "DataProtocol",
    "MarketData",
    "Order",
    "OrderSide",
    "OrderType",
    "Position",
    "StrategyProtocol",
    "TickData",
    "DEFAULT_COMMISSION_RATE",
    "DEFAULT_INITIAL_CAPITAL",
    "DEFAULT_LONG_WINDOW",
    "DEFAULT_SHORT_WINDOW",
    "DEFAULT_TRADE_SIZE",
    "MIN_SHORT_WINDOW",
    "RISK_FREE_RATE",
    "TRADING_DAYS_PER_YEAR",
    "__author__",
    "__email__",
    "__version__",
]
