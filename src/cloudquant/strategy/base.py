"""
Base class for trading strategies.

All trading strategies should inherit from this base class
and implement the required methods.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

from cloudquant.types import OrderSide, OrderType

if TYPE_CHECKING:
    from cloudquant.types import BarData, MarketData, Order

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
        self.name = name
        self.position = 0
        self.orders: list[Order] = []
        logger.info(f"Initialized strategy: {name}")

    @abstractmethod
    def on_data(self, data: MarketData) -> None:
        """
        Process incoming data point.

        Args:
            data: Market data (price, volume, indicators, etc.)

        This method is called for each data point in the backtest.
        Implement your strategy logic here.
        """
        pass

    def on_bar(self, bar: BarData) -> None:
        """
        Process bar/candle data.

        Args:
            bar: Bar/candle data (OHLCV)

        Override this method for bar-based strategies.
        """
        logger.debug(f"Received bar: {bar}")

    def _create_order(
        self,
        side: str,
        size: float,
        price: float | None = None,
    ) -> Order:
        order: Order = {
            "type": side,
            "side": OrderSide.BUY if side == "BUY" else OrderSide.SELL,
            "order_type": OrderType.MARKET,
            "size": size,
            "price": price,
            "timestamp": datetime.now(),
            "symbol": None,
        }
        self.orders.append(order)
        logger.info(f"Placed {side} order: size={size}, price={price}")
        return order

    def buy(self, size: float, price: float | None = None) -> Order:
        return self._create_order("BUY", size, price)

    def sell(self, size: float, price: float | None = None) -> Order:
        return self._create_order("SELL", size, price)
