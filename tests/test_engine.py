"""Tests for BacktestEngine."""

import pytest
from datetime import datetime
from cloudquant.core.engine import BacktestEngine


def test_engine_initialization():
    """Test engine initializes with correct parameters."""
    engine = BacktestEngine(initial_capital=100000, commission=0.001)

    assert engine.initial_capital == 100000
    assert engine.commission == 0.001
    assert engine.current_capital == 100000


def test_engine_default_values():
    """Test engine default values."""
    engine = BacktestEngine()

    assert engine.initial_capital == 100000.0
    assert engine.commission == 0.001
    assert engine.start_date is None
    assert engine.end_date is None


def test_engine_invalid_capital():
    """Test engine rejects invalid capital."""
    with pytest.raises(ValueError, match="initial_capital must be positive"):
        BacktestEngine(initial_capital=0)

    with pytest.raises(ValueError, match="initial_capital must be positive"):
        BacktestEngine(initial_capital=-100)


def test_engine_invalid_commission():
    """Test engine rejects negative commission."""
    with pytest.raises(ValueError, match="commission cannot be negative"):
        BacktestEngine(commission=-0.001)


def test_engine_run_placeholder():
    """Test engine run method returns placeholder results when no strategy/data."""
    engine = BacktestEngine()
    results = engine.run(strategy=None, data=None)

    assert isinstance(results, dict)
    assert results["initial_capital"] == 100000.0
    assert results["final_capital"] == 100000.0
    assert results["total_trades"] == 0


def test_engine_with_dates():
    """Test engine accepts date parameters."""
    start = datetime(2023, 1, 1)
    end = datetime(2023, 12, 31)
    engine = BacktestEngine(start_date=start, end_date=end)

    assert engine.start_date == start
    assert engine.end_date == end
