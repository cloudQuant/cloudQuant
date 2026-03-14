"""
Type definitions for cloudQuant.

This module contains Protocol definitions, type aliases, and typed dictionaries
used throughout the codebase for better type safety and IDE support.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Protocol, TypedDict


class OrderSide(str, Enum):
    """Order side enumeration."""
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    """Order type enumeration."""
    MARKET = "MARKET"
    LIMIT = "LIMIT"


class BarData(TypedDict, total=False):
    """OHLCV bar/candle data structure."""
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


class TickData(TypedDict, total=False):
    """Tick data structure."""
    timestamp: datetime
    price: float
    volume: float
    bid: float | None
    ask: float | None


class MarketData(TypedDict, total=False):
    """Generic market data structure."""

    symbol: str
    timestamp: datetime | None
    close: float
    open: float | None
    high: float | None
    low: float | None
    volume: float | None


class Order(TypedDict):
    """Order structure."""
    type: str  # OrderSide value
    side: OrderSide
    order_type: OrderType
    size: float
    price: float | None
    timestamp: datetime
    symbol: str | None


class Position(TypedDict):
    """Position structure."""
    symbol: str
    size: float
    entry_price: float
    current_price: float
    unrealized_pnl: float
    realized_pnl: float


class BacktestResult(TypedDict):
    """Backtest result structure."""
    initial_capital: float
    final_capital: float
    total_return: float
    sharpe_ratio: float
    max_drawdown: float
    total_trades: int
    win_rate: float | None
    profit_factor: float | None


class StrategyProtocol(Protocol):
    """Protocol defining the interface for trading strategies."""

    name: str
    position: int
    orders: list[Order]

    def on_data(self, data: MarketData) -> None:
        """Process incoming market data."""
        ...

    def on_bar(self, bar: BarData) -> None:
        """Process bar/candle data."""
        ...

    def buy(self, size: float, price: float | None = None) -> Order:
        """Place a buy order."""
        ...

    def sell(self, size: float, price: float | None = None) -> Order:
        """Place a sell order."""
        ...


class DataProtocol(Protocol):
    """Protocol defining the interface for market data."""

    def __len__(self) -> int:
        """Return number of data points."""
        ...

    def __getitem__(self, key: int) -> MarketData:
        """Get data point by index."""
        ...

    def to_dataframe(self) -> Any:
        """Convert to DataFrame format."""
        ...


__all__ = [
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
]
