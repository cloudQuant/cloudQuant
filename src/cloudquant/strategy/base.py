"""
Base class for trading strategies.

All trading strategies should inherit from this base class
and implement the required methods.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING
from datetime import datetime
import logging

if TYPE_CHECKING:
    from cloudquant.types import MarketData, BarData, Order

logger = logging.getLogger(__name__)


class Strategy(ABC):
    """
    Abstract base class for trading strategies.
    
    All strategies must implement:
    - on_data: Called for each data point
    - on_bar: Called for each bar/candle
    
    Example:
        >>> class MyStrategy(Strategy):
        ...     def on_data(self, data):
        ...         # Strategy logic here
        ...         pass
    """
    
    def __init__(self, name: str = "BaseStrategy") -> None:
        """
        Initialize strategy.
        
        Args:
            name: Strategy name for logging and identification
        """
        self.name = name
        self.position = 0
        self.orders = []
        logger.info(f"Initialized strategy: {name}")
    
    @abstractmethod
    def on_data(self, data: "MarketData") -> None:
        """
        Process incoming data point.
        
        Args:
            data: Market data (price, volume, indicators, etc.)
        
        This method is called for each data point in the backtest.
        Implement your strategy logic here.
        """
        pass
    
    def on_bar(self, bar: "BarData") -> None:
        """
        Process bar/candle data.
        
        Args:
            bar: Bar/candle data (OHLCV)
        
        Override this method for bar-based strategies.
        """
        logger.debug(f"Received bar: {bar}")
    
    def buy(self, size: float, price: Optional[float] = None) -> dict:
        """
        Place a buy order.
        
        Args:
            size: Position size
            price: Limit price (None for market order)
        
        Returns:
            Order dictionary
        """
        order = {
            "type": "BUY",
            "size": size,
            "price": price,
            "timestamp": datetime.now(),
        }
        self.orders.append(order)
        logger.info(f"Placed BUY order: size={size}, price={price}")
        return order
    
    def sell(self, size: float, price: Optional[float] = None) -> dict:
        """
        Place a sell order.
        
        Args:
            size: Position size
            price: Limit price (None for market order)
        
        Returns:
            Order dictionary
        """
        order = {
            "type": "SELL",
            "size": size,
            "price": price,
            "timestamp": datetime.now(),
        }
        self.orders.append(order)
        logger.info(f"Placed SELL order: size={size}, price={price}")
        return order
