"""
cloudQuant - AI-Powered Development Framework for Quantitative Trading Systems.

This package provides a comprehensive framework for building quantitative trading
systems with AI assistance and structured development methodologies.
"""

__version__ = "0.1.0"
__author__ = "cloudQuant Team"
__email__ = "yunjinqi@gmail.com"

from cloudquant.core.engine import BacktestEngine
from cloudquant.data.loader import DataLoader
from cloudquant.strategy.base import Strategy

__all__ = [
    "BacktestEngine",
    "DataLoader", 
    "Strategy",
    "__version__",
    "__author__",
    "__email__",
]
