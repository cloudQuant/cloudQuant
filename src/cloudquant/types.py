"""
Type definitions for cloudQuant.

This module contains Protocol definitions, type aliases, and typed dictionaries
used throughout the codebase for better type safety and IDE support.
"""

from typing import Protocol, TypedDict, Optional, Any
from datetime import datetime
from enum import Enum


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
    bid: Optional[float]
    ask: Optional[float]


class MarketData(TypedDict, total=False):
    """Generic market data structure."""
    symbol: str
    timestamp: datetime
    close: float
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    volume: Optional[float]


class Order(TypedDict):
    """Order structure."""
    type: str  # OrderSide value
    side: OrderSide
    order_type: OrderType
    size: float
    price: Optional[float]
    timestamp: datetime
    symbol: Optional[str]


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
    win_rate: Optional[float]
    profit_factor: Optional[float]


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
    
    def buy(self, size: float, price: Optional[float] = None) -> Order:
        """Place a buy order."""
        ...
    
    def sell(self, size: float, price: Optional[float] = None) -> Order:
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
    "OrderSide",
    "OrderType",
    "BarData",
    "TickData",
    "MarketData",
    "Order",
    "Position",
    "BacktestResult",
    "StrategyProtocol",
    "DataProtocol",
]
