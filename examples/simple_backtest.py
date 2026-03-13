"""
Example backtest script.

This script demonstrates how to run a simple backtest
using the cloudQuant framework.
"""

from cloudquant.core.engine import BacktestEngine
from cloudquant.strategy.simple import SimpleMovingAverageStrategy
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def main():
    """Run example backtest."""
    strategy = SimpleMovingAverageStrategy(short_window=10, long_window=30)
    engine = BacktestEngine(initial_capital=100000, commission=0.001)
    
    print(f"Running backtest with strategy: {strategy.name}")
    print(f"Initial capital: ${engine.initial_capital:,.2f}")
    print(f"Commission rate: {engine.commission * 100:.2f}%")
    
    results = engine.run(strategy=strategy, data=None)
    
    print("\n" + "=" * 50)
    print("Backtest Results")
    print("=" * 50)
    for key, value in results.items():
        if isinstance(value, float):
            print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
