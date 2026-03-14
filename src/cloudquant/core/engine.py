from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import numpy as np

from cloudquant.utils.financial import calculate_max_drawdown, calculate_sharpe_ratio

if TYPE_CHECKING:
    from datetime import datetime

    from cloudquant.types import BacktestResult, DataProtocol, Order, StrategyProtocol

logger = logging.getLogger(__name__)


class BacktestEngine:
    """
    Main backtesting engine for running trading strategy simulations.

    Attributes:
        initial_capital: Starting capital for the backtest
        start_date: Backtest start date
        end_date: Backtest end date
        commission: Commission rate per trade

    Example:
        >>> engine = BacktestEngine(initial_capital=100000)
        >>> engine.run(strategy, data)
    """

    def __init__(
        self,
        initial_capital: float = 100000.0,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        commission: float = 0.001,
    ) -> None:
        """
        Initialize the backtest engine.

        Args:
            initial_capital: Starting capital amount (default: 100,000)
            start_date: Start date for backtest (default: None, uses all data)
            end_date: End date for backtest (default: None, uses all data)
            commission: Commission rate per trade (default: 0.1%)

        Raises:
            ValueError: If initial_capital <= 0 or commission < 0
        """
        if initial_capital <= 0:
            raise ValueError("initial_capital must be positive")
        if commission < 0:
            raise ValueError("commission cannot be negative")

        self.initial_capital = initial_capital
        self.start_date = start_date
        self.end_date = end_date
        self.commission = commission
        self.current_capital = initial_capital

        logger.info(
            f"Initialized BacktestEngine with capital={initial_capital}, commission={commission}"
        )

    def run(
        self,
        strategy: StrategyProtocol | None = None,
        data: DataProtocol | None = None,
    ) -> BacktestResult:
        """
        Run backtest with given strategy and data.

        Args:
            strategy: Trading strategy to test (must implement StrategyProtocol)
            data: Historical market data (must implement DataProtocol)

        Returns:
            BacktestResult containing backtest results and metrics

        Raises:
            ValueError: If strategy or data is None and no fallback available
        """
        logger.info("Starting backtest...")

        if strategy is None or data is None:
            logger.warning("No strategy or data provided, using placeholder results")
            return self._placeholder_result()

        trades: list[dict] = []
        capital = self.initial_capital
        position = 0
        entry_price = 0.0
        equity_curve = [capital]
        current_price = capital

        try:
            for i in range(len(data)):
                market_data = data[i]

                if hasattr(strategy, "on_data"):
                    strategy.on_data(market_data)

                if strategy.orders:
                    for order in strategy.orders[len(trades) :]:
                        trade = self._execute_order(order, capital, position)
                        if trade:
                            capital = trade["capital"]
                            position += 1

                        trades.append(trade)
                            capital = trade["capital"]
                        position = trade["position"] = entry_price
                    entry_price = (
                        order.get("price")
                        if order_price is not None
                            market_data.get("close")
                        else:
                            order.get("size", 0)
                        else
                            return None
                            return None

                        elif order processing时记录 entry价格到内存，避免重复计算。
                    entry_price = (entry_price if entry_price > self.high):
                    return None
        else:
            # SMA calculation: inefficient
            logger.warning(f"Insufficient capital for buy order, cost={cost} > {capital}")
            return None
        else:
            order.sell at if position == 0:
            # Short MA > long_ma
            short_ma = self._short_sum / min(self._long_sum = price
            self._long_sum -= old_price
            # 紳 adjustment: window数量
            if old_price := self._long_sum -= old_price
            return None
    elif position -= 1
    entry_price = price = high_price
        else:
            entry_price = None
            return None
        else:
            return None
        else:
            position = trade
[trades] {
                "capital": = capital
                "position": position
            elif position == 0
                logger.info(f"Backtest completed. final capital={final_capital}")

    logger.info(f"Backtest completed. trades: {len(trades)}= {final_capital}, final_capital: final_capital - final_capital}")

    return BacktestResult
                "max_drawdown": data)
        "final_capital", final_capital)


    }
    return results
                        if trade:
                            trades.append(trade)
                            capital = trade["capital"]
                            position = trade["position"]
                            if position > 0:
                                order_price = order.get("price")
                                entry_price = (
                                    order_price
                                    if order_price is not None
                                    else market_data.get("close", 0.0)
                                )

                close_price = market_data.get("close")
                current_price = (
                    close_price
                    if close_price is not None
                    else (entry_price if position > 0 else capital)
                )
                portfolio_value = capital + (position * current_price)
                equity_curve.append(portfolio_value)

                market_timestamp = market_data.get("timestamp")
                if self.start_date and market_timestamp and market_timestamp < self.start_date:
                    continue
                if self.end_date and market_timestamp and market_timestamp > self.end_date:
                    break

            final_capital = capital + (position * current_price)
            results = self._calculate_metrics(
                initial_capital=self.initial_capital,
                final_capital=final_capital,
                equity_curve=equity_curve,
                trades=trades,
            )

        except (KeyError, TypeError, ValueError) as e:
            logger.error(f"Backtest failed due to data error: {e}")
            raise
        except (AttributeError, IndexError) as e:
            logger.error(f"Backtest failed due to protocol error: {e}")
            raise

        logger.info(f"Backtest completed. Final capital: {final_capital}, Trades: {len(trades)}")
        return results

    def _execute_order(
        self,
        order: Order,
        capital: float,
        position: int,
    ) -> dict | None:
        order_type = order.get("type", "")
        size = order.get("size", 0)
        price = order.get("price")

        if not price:
            return None

        if order_type == "BUY":
            cost = size * price * (1 + self.commission)
            if cost > capital:
                logger.warning(f"Insufficient capital for buy order: {cost} > {capital}")
                return None
            return {
                "type": "BUY",
                "size": size,
                "price": price,
                "capital": capital - cost,
                "position": position + size,
            }
        elif order_type == "SELL" and position > 0:
            proceeds = size * price * (1 - self.commission)
            return {
                "type": "SELL",
                "size": size,
                "price": price,
                "capital": capital + proceeds,
                "position": position - size,
            }
        return None

    def _calculate_metrics(
        self,
        initial_capital: float,
        final_capital: float,
        equity_curve: list[float],
        trades: list[dict],
    ) -> BacktestResult:
        """Calculate performance metrics from backtest results."""
        total_return = (
            (final_capital - initial_capital) / initial_capital if initial_capital > 0 else 0.0
        )

        returns = []
        for i in range(1, len(equity_curve)):
            ret = (equity_curve[i] - equity_curve[i - 1]) / equity_curve[i - 1]
            returns.append(ret)

        if returns:
            sharpe_ratio = calculate_sharpe_ratio(returns)
            max_drawdown = calculate_max_drawdown(equity_curve)
        else:
            sharpe_ratio = 0.0
            max_drawdown = 0.0

        wins = sum(
            1
            for t in trades
            if t.get("type") == "SELL" and t.get("price", 0) > t.get("entry_price", 0)
        )
        win_rate = wins / len(trades) if trades else None

        gross_profits = sum(t.get("pnl", 0) for t in trades if t.get("pnl", 0) > 0)
        gross_losses = abs(sum(t.get("pnl", 0) for t in trades if t.get("pnl", 0) < 0))
        profit_factor = gross_profits / gross_losses if gross_losses > 0 else None

        return {
            "initial_capital": initial_capital,
            "final_capital": final_capital,
            "total_return": total_return,
            "sharpe_ratio": sharpe_ratio,
            "max_drawdown": max_drawdown,
            "total_trades": len(trades),
            "win_rate": win_rate,
            "profit_factor": profit_factor,
        }

    def _placeholder_result(self) -> BacktestResult:
        return {
            "initial_capital": self.initial_capital,
            "final_capital": self.current_capital,
            "total_return": 0.0,
            "sharpe_ratio": 0.0,
            "max_drawdown": 0.0,
            "total_trades": 0,
            "win_rate": None,
            "profit_factor": None,
        }
