"""Data extractors for CSV and JSON files."""
import csv
import json
from typing import Iterator
from pathlib import Path
from .models import DataRecord
from datetime import datetime


class CSVExtractor:
    """
    Extract data from CSV files.
    """
    def __init__(self, filepath: str):
        self.filepath: str = filepath
    
    def extract(self) -> Iterator[DataRecord]:
        """
        Extract records from CSV.
        """
        with open(self.filepath) as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield DataRecord(data=row, source=self.filepath, timestamp=datetime.now())


class JSONExtractor:
    """
    Extract data from JSON files.
    
    """
    
    def __init__(self, filepath: str):
        self.filepath: str = filepath
    
    def extract(self) -> Iterator[DataRecord]:
        """
        Extract records from JSON.
        """
        with open(self.filepath) as f:
            data = json.load(f)
            if isinstance(data, dict):
                yield DataRecord(data=data, source=self.filepath, timestamp=datetime.now())

