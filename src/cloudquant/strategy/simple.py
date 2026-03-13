"""Example trading strategy implementations."""

from cloudquant.strategy.base import Strategy
from typing import Any


class SimpleMovingAverageStrategy(Strategy):
    """
    Simple Moving Average crossover strategy.
    
    Generates buy signals when short MA crosses above long MA,
    and sell signals when short MA crosses below long MA.
    """
    
    def __init__(
        self,
        short_window: int = 10,
        long_window: int = 30,
        name: str = "SMA_Crossover",
    ) -> None:
        super().__init__(name=name)
        self.short_window = short_window
        self.long_window = long_window
        self.price_history: list[float] = []
    
    def on_data(self, data: Any) -> None:
        """Process new data point and generate signals."""
        if isinstance(data, dict) and "close" in data:
            price = float(data["close"])
            self.price_history.append(price)
            
            if len(self.price_history) >= self.long_window:
                short_ma = sum(self.price_history[-self.short_window:]) / self.short_window
                long_ma = sum(self.price_history[-self.long_window:]) / self.long_window
                
                if short_ma > long_ma and self.position <= 0:
                    self.buy(size=100)
                elif short_ma < long_ma and self.position > 0:
                    self.sell(size=self.position)
