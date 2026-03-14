"""Tests for DataLoader class."""

import pytest
from cloudquant.data.loader import DataLoader
from cloudquant.strategy.simple import SimpleMovingAverageStrategy
from cloudquant.core.engine import BacktestEngine


class TestDataLoader:
    def test_init_default(self):
        loader = DataLoader()
        assert loader.cache_dir is None

    def test_init_with_cache_dir(self, tmp_path):
        cache_dir = tmp_path / "cache"
        loader = DataLoader(cache_dir=cache_dir)
        assert loader.cache_dir == cache_dir

    def test_load_csv_not_exists(self):
        loader = DataLoader()
        result = loader.load_csv("nonexistent.csv")
        assert result is None

    def test_validate_data_empty(self):
        loader = DataLoader()
        assert loader.validate_data([]) is False

    def test_validate_data_valid(self, sample_market_data):
        loader = DataLoader()
        assert loader.validate_data(sample_market_data) is True

    def test_validate_data_missing_field(self):
        loader = DataLoader()
        invalid_data = [{"symbol": "AAPL"}]
        assert loader.validate_data(invalid_data) is False


class TestSimpleMovingAverageStrategy:
    def test_strategy_init(self):
        strategy = SimpleMovingAverageStrategy(short_window=5, long_window=10)
        assert strategy.short_window == 5
        assert strategy.long_window == 10
        assert strategy.name == "SMA_Crossover"

    def test_strategy_invalid_windows(self):
        with pytest.raises(ValueError, match="short_window must be at least 2"):
            SimpleMovingAverageStrategy(short_window=1)

        with pytest.raises(ValueError, match="long_window must be greater than short_window"):
            SimpleMovingAverageStrategy(short_window=10, long_window=5)

    def test_strategy_on_data(self, sample_market_data):
        strategy = SimpleMovingAverageStrategy(short_window=2, long_window=3)

        for data in sample_market_data:
            strategy.on_data(data)

        assert len(strategy.price_history) == len(sample_market_data)


class TestBacktestEngine:
    def test_engine_init(self):
        engine = BacktestEngine(initial_capital=100000, commission=0.001)
        assert engine.initial_capital == 100000
        assert engine.commission == 0.001

    def test_engine_run_no_data(self):
        engine = BacktestEngine()
        results = engine.run(strategy=None, data=None)
        assert results["total_trades"] == 0
        assert results["initial_capital"] == 100000
