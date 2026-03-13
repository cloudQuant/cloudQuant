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


def test_engine_run():
    """Test engine run method returns results."""
    engine = BacktestEngine()
    results = engine.run(strategy=None, data=None)
    
    assert isinstance(results, dict)
    assert "initial_capital" in results
    assert "final_capital" in results
    assert "total_return" in results
    assert "sharpe_ratio" in results
