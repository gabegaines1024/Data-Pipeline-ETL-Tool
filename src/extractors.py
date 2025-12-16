"""Data extractors for CSV and JSON files."""
import csv
import json
from typing import Iterator
from pathlib import Path
from .models import DataRecord


class CSVExtractor:
    """
    Extract data from CSV files.
    
    TODO: Read CSV and yield DataRecords
    """
    
    def __init__(self, filepath: str):
        """TODO: Store filepath"""
        pass
    
    def extract(self) -> Iterator[DataRecord]:
        """
        Extract records from CSV.
        
        TODO:
        1. Open CSV file
        2. Use csv.DictReader to read rows
        3. For each row, create DataRecord(data=row, source=filepath)
        4. Yield each record
        
        Hint: with open(self.filepath) as f:
                  reader = csv.DictReader(f)
                  for row in reader:
                      yield DataRecord(data=row, source=self.filepath)
        """
        pass


class JSONExtractor:
    """
    Extract data from JSON files.
    
    TODO: Read JSON and yield DataRecords
    """
    
    def __init__(self, filepath: str):
        """TODO: Store filepath"""
        pass
    
    def extract(self) -> Iterator[DataRecord]:
        """
        Extract records from JSON.
        
        TODO:
        1. Open and parse JSON file
        2. Handle both array format and object format
        3. For each item, yield DataRecord
        
        Hint: with open(self.filepath) as f:
                  data = json.load(f)
                  if isinstance(data, list):
                      for item in data:
                          yield DataRecord(data=item, source=self.filepath)
        """
        pass

