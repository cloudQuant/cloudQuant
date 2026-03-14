"""
Data loading utilities for market data.

This module provides functionality to load and preprocess market data
from various sources (CSV, databases, APIs)

External APIs (via plugins).
"""

from __future__ import annotations

import csv
import logging
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cloudquant.types import MarketData

import pandas as pd

logger = logging.getLogger(__name__)


class DataLoader:
    """
    Load and preprocess market data for backtesting.

    Supports loading data from:
    - CSV files
    - Parquet files
    - SQL databases
        - External APIs (via plugins)

    Attributes:
        cache_dir: Directory for caching downloaded data

    Example:
        >>> loader = DataLoader()
        >>> data = loader.load_csv("data/prices.csv")
    """

    def __init__(self, cache_dir: Path | None = None) -> None:
        """
        Initialize the DataLoader.

        Args:
            cache_dir: Directory for caching downloaded data
        """
        if cache_dir:
            cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir = cache_dir
        logger.info(f"Initialized DataLoader with cache_dir={cache_dir}")

    def load_csv(
        self,
        filepath: Path | str,
        symbol_column: str = "symbol",
        date_column: str = "date",
        close_column: str = "close",
        open_column: str | None = "open",
        high_column: str | None = "high",
        low_column: str | None = "low",
        volume_column: str | None = "volume",
    ) -> list[MarketData] | None:
        path = Path(filepath)

        if not path.exists():
            logger.warning(f"File not found: {filepath}")
            return None

        logger.info(f"Loading data from {filepath}")

        try:
            with path.open(newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        except Exception as e:
            logger.error(f"Failed to read CSV: {e}")
            return None

        data: list[MarketData] = []
        for i, row in enumerate(rows, start=1):
            try:
                if close_column not in row:
                    logger.warning(f"Row {i}: Missing required column '{close_column}', skipping")
                    continue

                timestamp = None
                if row.get(date_column):
                    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"):
                        try:
                            timestamp = datetime.strptime(row[date_column], fmt)
                            break
                        except ValueError:
                            continue

                try:
                    close_price = float(row[close_column])
                    if close_price < 0:
                        logger.warning(f"Row {i}: Negative close price {close_price}, skipping")
                        continue
                except (ValueError, TypeError) as e:
                    logger.warning(
                        f"Row {i}: Invalid close price '{row.get(close_column)}': {e}, skipping"
                    )
                    continue

                record: MarketData = {
                    "symbol": row.get(symbol_column, ""),
                    "timestamp": timestamp,
                    "close": close_price,
                }

                if open_column and open_column in row:
                    try:
                        open_price = float(row[open_column])
                        if open_price >= 0:
                            record["open"] = open_price
                        else:
                            logger.warning(f"Row {i}: Negative open price, ignoring")
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Row {i}: Invalid open price: {e}, ignoring")

                if high_column and high_column in row:
                    try:
                        high_price = float(row[high_column])
                        if high_price >= 0:
                            record["high"] = high_price
                        else:
                            logger.warning(f"Row {i}: Negative high price, ignoring")
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Row {i}: Invalid high price: {e}, ignoring")

                if low_column and low_column in row:
                    try:
                        low_price = float(row[low_column])
                        if low_price >= 0:
                            record["low"] = low_price
                        else:
                            logger.warning(f"Row {i}: Negative low price, ignoring")
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Row {i}: Invalid low price: {e}, ignoring")

                if volume_column and volume_column in row:
                    try:
                        volume = float(row[volume_column])
                        if volume >= 0:
                            record["volume"] = volume
                        else:
                            logger.warning(f"Row {i}: Negative volume, ignoring")
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Row {i}: Invalid volume: {e}, ignoring")

                data.append(record)
            except Exception as e:
                logger.warning(f"Row {i}: Unexpected error processing row: {e}, skipping")
                continue

        logger.info(f"Loaded {len(data)} records from {filepath}")
        return data

    def load_parquet(self, filepath: Path | str) -> list[MarketData] | None:
        """
        Load market data from a Parquet file.

        Args:
            filepath: Path to the Parquet file

        Returns:
            List of MarketData dictionaries, or None if file doesn't exist

        Raises:
            ImportError: If pyarrow or pandas is not installed
        """
        try:
            import pyarrow.parquet as pq
        except ImportError as e:
            logger.error(
                "pyarrow is required for Parquet support. Install with: pip install pyarrow"
            )
            raise ImportError(
                "pyarrow is required for Parquet support. Install with: pip install pyarrow"
            ) from e

        path = Path(filepath)

        if not path.exists():
            logger.warning(f"File not found: {filepath}")
            return None

        logger.info(f"Loading data from {filepath}")

        try:
            table = pq.read_table(path)
            df = table.to_pandas()

            data: list[MarketData] = []
            for _, row in df.iterrows():
                record: MarketData = {
                    "symbol": str(row.get("symbol", "")),
                    "timestamp": row.get("timestamp"),
                    "close": float(row.get("close", 0.0)),
                }

                if "open" in row and pd.notna(row["open"]):
                    record["open"] = float(row["open"])
                if "high" in row and pd.notna(row["high"]):
                    record["high"] = float(row["high"])
                if "low" in row and pd.notna(row["low"]):
                    record["low"] = float(row["low"])
                if "volume" in row and pd.notna(row["volume"]):
                    record["volume"] = float(row["volume"])

                data.append(record)

            logger.info(f"Loaded {len(data)} records from {filepath}")
            return data

        except Exception as e:
            logger.error(f"Failed to read Parquet file: {e}")
            return None

    def validate_data(self, data: list[MarketData]) -> bool:
        """
        Validate market data structure and values.

        Args:
            data: List of MarketData dictionaries to validate

        Returns:
            True if data is valid, False otherwise
        """
        if not data:
            logger.warning("Empty data list")
            return False

        required_fields = ["symbol", "timestamp", "close"]

        for i, record in enumerate(data):
            for field in required_fields:
                if field not in record:
                    logger.warning(f"Missing field '{field}' at index {i}")
                    return False

        return True


class DataList:
    """
    Wrapper class that implements DataProtocol for list-based market data.

    This class wraps a list of MarketData dictionaries and provides
    the DataProtocol interface for use with the BacktestEngine.

    Attributes:
        data: List of MarketData dictionaries
        symbol: Trading symbol (optional)

    Example:
        >>> market_data = [
        ...     {"symbol": "AAPL", "timestamp": datetime(2023, 1, 1), "close": 150.0},
        ...     {"symbol": "AAPL", "timestamp": datetime(2023, 1, 2), "close": 152.0},
        ... ]
        >>> data_list = DataList(market_data, symbol="AAPL")
        >>> len(data_list)
        2
    """

    def __init__(self, data: list[MarketData], symbol: str | None = None) -> None:
        self._data = data
        self.symbol = symbol or (data[0].get("symbol") if data else None)

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: int) -> MarketData:
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self._data)

    @property
    def data(self) -> list[MarketData]:
        return self._data


__all__ = ["DataList", "DataLoader"]
