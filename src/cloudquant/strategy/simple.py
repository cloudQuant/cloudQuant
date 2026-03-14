from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from cloudquant.strategy.base import Strategy

if TYPE_CHECKING:
    from cloudquant.types import MarketData

logger = logging.getLogger(__name__)


class SimpleMovingAverageStrategy(Strategy):
    def __init__(
        self,
        short_window: int = 10,
        long_window: int = 30,
        name: str = "SMA_Crossover",
    ) -> None:
        if short_window < 2:
            raise ValueError("short_window must be at least 2")
        if long_window <= short_window:
            raise ValueError("long_window must be greater than short_window")

        super().__init__(name=name)
        self.short_window = short_window
        self.long_window = long_window
        self.price_history: list[float] = []
        self._short_sum = 0.0
        self._long_sum = 0.0

    def on_data(self, data: MarketData) -> None:
        if not isinstance(data, dict):
            return

        if "close" not in data:
            return

        price = float(data["close"])
        self.price_history.append(price)
        self._short_sum += price
        self._long_sum += price

        if len(self.price_history) > self.long_window:
            old_price = self.price_history[-self.long_window - 1]
            self._long_sum -= old_price
        if len(self.price_history) > self.short_window:
            old_price = self.price_history[-self.short_window - 1]
            self._short_sum -= old_price

        if len(self.price_history) < self.long_window:
            return

        short_ma = self._short_sum / min(len(self.price_history), self.short_window)
        long_ma = self._long_sum / min(len(self.price_history), self.long_window)

        if short_ma > long_ma and self.position <= 0:
            self.buy(size=100)
            self.position = 100
        elif short_ma < long_ma and self.position > 0:
            self.sell(size=self.position)
            self.position = 0
