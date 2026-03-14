"""Tests for cloudquant package initialization."""

import pytest


def test_import_main_classes():
    """Test that main classes can be imported."""
    from cloudquant import BacktestEngine, DataLoader, Strategy
    
    assert BacktestEngine is not None
    assert DataLoader is not None
    assert Strategy is not None


def test_version():
    """Test that version is defined."""
    import cloudquant
    
    assert hasattr(cloudquant, "__version__")
    assert cloudquant.__version__ == "0.1.0"


def test_metadata():
    """Test package metadata."""
    import cloudquant
    
    assert cloudquant.__author__ == "cloudQuant Team"
    assert cloudquant.__email__ == "yunjinqi@gmail.com"
