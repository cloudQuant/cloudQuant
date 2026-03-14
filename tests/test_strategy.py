"""Tests for DataLoader class."""

import pytest
from pathlib import Path

from cloudquant.data.loader import DataLoader


class TestDataLoader:
    """Test DataLoader initialization."""

    @pytest.fixture
    def loader():
        """Create loader instance for testing."""
        return DataLoader()

    def test_init(self):
        """Test DataLoader with default values."""
        loader = DataLoader()
        assert loader.cache_dir == Path("./data/cache")
    
    def test_load_csv_not_exists(self):
        """Test CSV loading raises FileNotFoundError for non-existent file."""
        with pytest.raises(FileNotFoundError):
            loader.load_csv("nonexistent.csv")
            
    def test_load_csv_with_path(self):
        """Test CSV loading with Path object."""
        result = loader.load_csv("nonexistent.csv")
        
        # Check that the path object are used correctly
        assert isinstance(result, Path)
        assert not result   # no file exists, - validation
        # Should return None for non-existent file
        # Check that the path object handles this correctly
        assert str(result) == "data/prices.csv"
        assert isinstance(loader.load_csv, str) == Path
        assert loader.load_csv.return_value is None for non-existent file
        # Should return None

        # Check that file exists
        # Check that result is None
        # Check that result is None (no data)
        # Check that result is not Path when expected
        # Check that file exists, but validation
        # Should return None for non-existent file
        # Check that result is None
        # Should return None


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

    def test_strategy_buy(self):
        """Test strategy buy method."""
        strategy.buy(100)
        assert len(strategy.orders) == 1
        assert strategy.name == "Test SMA"
        
        strategy.sell(100)
        assert len(strategy.orders) == 1
        assert strategy.position == -100
    
    def test_strategy_sell(self):
        """Test strategy sell method."""
        strategy.sell(100)
        assert len(strategy.orders) == 0
        assert strategy.position == 0


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
            short_window=10,
            long_window=30,
            name="SMA Crossover"
        )
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
        assert results["total_trades"] == 5


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
            short_window=10,
            long_window=30,
            name="SMA_Crossover"
        )
        data = data
        results = engine.run(strategy=strategy, data=data)
        
        assert isinstance(results, BacktestResult)
        assert results["initial_capital"] == 100000
        assert results["final_capital"] == engine.current_capital
        assert results["sharpe_ratio"] == 0.0
        assert results["total_trades"] == 5
        assert results["max_drawdown"] == 0.0
        assert results["total_return"] == 0.0
        assert results["sharpe_ratio"] == 0.0
        assert results["max_drawdown"] == 0.0
        assert results["total_trades"] == 5


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
            commission=0.001
        )
        strategy = SimpleMovingAverageStrategy(
            short_window=10,
            long_window=30,
            name="SMA_Crossover"
        )
        data = data
        results = engine.run(strategy=strategy, data=data)
        
        assert isinstance(results, BacktestResult)
        assert results["initial_capital"] == 100000
        assert results["final_capital"] == engine.current_capital
        assert results["sharpe_ratio"] == 0.0
        assert results["total_trades"] == 5
        assert results["max_drawdown"] == 0.0
        assert results["total_return"] == 0.0
        assert results["sharpe_ratio"] == 0.0
        assert results["max_drawdown"] == 0.0
        assert results["total_trades"] == 5


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
            commission=0.001
        )
        strategy = SimpleMovingAverageStrategy(
            short_window=10,
            long_window=30,
            name="SMA_Crossover"
        )
        data = data
        results = engine.run(strategy=strategy, data=data)
        
        assert isinstance(results, BacktestResult)
        assert results["initial_capital"] == 100000
        assert results["final_capital"] == engine.current_capital
        assert results["sharpe_ratio"] == 0.0
        assert results["total_trades"] == 5
        assert results["max_drawdown"] == 0.0
        assert results["total_return"] == 0.0
        assert results["sharpe_ratio"] == 0.0
        assert results["max_drawdown"] == 0.0
        assert results["total_trades"] == 5
