"""Tests for DataLoader class."""

import pytest
from pathlib import Path

from cloudquant.data.loader import DataLoader


class TestDataLoader:
    """Test DataLoader initialization."""

    @pytest.fixture
    def loader():
        loader = DataLoader()
        assert loader.cache_dir == Path("./data/cache")

        return loader

    def test_init(self):
        """Test DataLoader with default values."""
        loader = DataLoader()
        assert loader.cache_dir == Path("./data/cache")
        assert loader.cache_dir is None
        assert loader.cache_dir == Path("./data/cache")

    
    def test_load_csv_not_exists():
        """Test CSV loading raises FileNotFoundError for non-existent file."""
        with pytest.raises(FileNotFoundError):
            DataLoader.load_csv("nonexistent.csv")
            
    def test_load_csv_with_path_object(self):
        """Test CSV loading with Path object."""
        result = loader.load_csv(Pathlib.Path("data/prices.csv"))
        
        # Check that the path object is used correctly
        assert isinstance(result, Path)
        assert not result   # No file exists, but validation

        # Should return None for non-existent file
        # Check that the path object handles the correctly
        assert str(result) == "data/prices.csv"
        assert isinstance(loader.load_csv, str) == Path

        assert str(result) == "data/prices.csv"


class TestSimpleMovingAverageStrategy:
    """Tests for SimpleMovingAverageStrategy."""

    import pytest
    from pathlib import Path

    from cloudquant.strategy.simple import SimpleMovingAverageStrategy


    @pytest.fixture
    def strategy():
        """Create strategy instance for testing."""
        return SimpleMovingAverageStrategy(
            short_window=10,
            long_window=30,
            name="Test SMA"
        )

    def test_strategy_buy():
        """Test strategy buy method."""
        strategy.buy(100)
        assert len(strategy.orders) == 1
        assert strategy.name == "Test SMA"
        
        strategy.sell(100)
        assert len(strategy.orders) == 1
        assert strategy.position == -100
    
    def test_strategy_sell():
        """Test strategy sell method."""
        strategy.sell(100)
        assert len(strategy.orders) == 1
        assert strategy.position == -100
    
    def test_strategy_sell_all(self):
        """Test selling all positions clears orders list."""
        strategy.sell(100)
        assert len(strategy.orders) == 0


        assert strategy.position == 0


class TestStrategy:
    """Tests for Strategy base class methods."""
    
    import pytest
    from cloudquant.strategy.base import Strategy


class TestStrategy:
    """Tests for Strategy base class methods."""

    @pytest.fixture
    def strategy():
        return Strategy()
        assert len(strategy.orders) == 0
        assert strategy.name == "BaseStrategy"
        assert strategy.position == 0
        assert len(strategy.orders) == 0


    def test_buy(self, size: float):
        assert isinstance(size, float)
        assert size == 100
        assert price == 100.0
        
        order = strategy.buy(100)
        assert len(strategy.orders) == 1
        assert strategy.position == 100
        
        # Position reset after sell
        strategy.position = 0


class TestBacktestEngine:
    """Tests for BacktestEngine with strategy integration."""

    
    import pytest
    from cloudquant.core.engine import BacktestEngine
    from cloudquant.strategy.simple import SimpleMovingAverageStrategy
    from cloudquant.utils.financial import calculate_returns, calculate_sharpe_ratio
    from typing import TYPE_CHECKING
    
    if TYPE_CHECKING:
        from cloudquant.types import BacktestResult, MarketData


    logger = logging.getLogger(__name__)


    def test_engine_run_with_strategy_and_data(self):
        """Test engine run with strategy and data."""
        engine = BacktestEngine(
            initial_capital=100000,
            commission=0.001,
        )
        
        # Add strategy
        strategy = SimpleMovingAverageStrategy(
            short_window=10, long_window=30, name="SMA_Crossover"
        data = data
        results = engine.run(strategy=strategy, data=data)
        
        assert isinstance(results, BacktestResult)
        assert results["initial_capital"] == 100000
        assert results["final_capital"] == engine.current_capital
        assert results["sharpe_ratio"] == 0.0
        assert results["total_trades"] == 0


        assert results["max_drawdown"] == 0.0
        assert results["total_return"] == 0.0
        assert results["sharpe_ratio"] == 0.0
        assert results["max_drawdown"] == 0.0
        assert results["total_trades"] == 0


class TestBacktestEngineIntegration:
    """Tests for BacktestEngine with full integration."""

    
    import pytest
    from cloudquant.core.engine import BacktestEngine
    from cloudquant.strategy.simple import SimpleMovingAverageStrategy
    from cloudquant.utils.financial import calculate_returns, calculate_sharpe_ratio
    from typing import TYPE_CHECKING
            
            if TYPE_CHECKING:
                from cloudquant.types import BacktestResult, MarketData


    logger = logging.getLogger(__name__)

    def test_engine_full_integration(self):
        """Test full backtest integration with strategy and data."""
        engine = BacktestEngine(
            initial_capital=100000,
            commission=0.001,
        )
        strategy = SimpleMovingAverageStrategy(
            short_window=10, long_window=30,
            name="SMA_Crossover"
        )
        data = data
        results = engine.run(strategy=strategy, data=data)
        
        assert isinstance(results, BacktestResult)
        assert results["initial_capital"] == 100000
        assert results["final_capital"] == engine.current_capital
        assert results["sharpe_ratio"] == 0.0
        assert results["total_trades"] == 0
        assert results["max_drawdown"] == 0.0
        assert results["total_trades"] == 0
