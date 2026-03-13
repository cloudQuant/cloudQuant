"""Example trading strategy implementations."""

from __future__ import annotations

from cloudquant.strategy.base import Strategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cloudquant.types import MarketData


class SimpleMovingAverageStrategy(Strategy):
    """
    Simple Moving Average crossover strategy.
    
    Generates buy signals when short MA crosses above long MA,
    and sell signals when short MA crosses below long MA.
    
    Attributes:
        short_window: Short moving average window period
        long_window: Long moving average window period
        price_history: List of historical prices for MA calculation
    """
    
    def __init__(
        self,
        short_window: int = 10,
        long_window: int = 30,
        name: str = "SMA_Crossover",
    ) -> None:
        """
        Initialize SMA crossover strategy.
        
        Args:
            short_window: Short MA window period (must be >= 2)
            long_window: Long MA window period (must be > short_window)
            name: Strategy name for logging
        
        Raises:
            ValueError: If window parameters are invalid
        """
        if short_window < 2:
            raise ValueError("short_window must be at least 2")
        if long_window <= short_window:
            raise ValueError("long_window must be greater than short_window")
        
        super().__init__(name=name)
        self.short_window = short_window
        self.long_window = long_window
        self.price_history: list[float] = []
    
    def on_data(self, data: "MarketData") -> None:
        """
        Process new data point and generate signals.
        
        Args:
            data: Market data containing at least 'close' price
        
        Note:
            This implementation uses simple SMA crossover logic.
            For production use, consider using exponential moving averages
            or more sophisticated signal generation.
        """
        if not isinstance(data, dict):
            return
        
        if "close" not in data:
            return
        
        price = float(data["close"])
        self.price_history.append(price)
        
        # Need enough data points for both MAs
        if len(self.price_history) < self.long_window:
            return
        
        short_ma = sum(self.price_history[-self.short_window:]) / self.short_window
        long_ma = sum(self.price_history[-self.long_window:]) / self.long_window
        
        # Generate signals based on crossover
        if short_ma > long_ma and self.position <= 0:
            # Golden cross - buy signal
            self.buy(size=100)
        elif short_ma < long_ma and self.position > 0:
            # Death cross - sell signal
            self.sell(size=self.position)
