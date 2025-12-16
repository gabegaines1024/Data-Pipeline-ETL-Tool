"""Data loaders for CSV and JSON output."""
import csv
import json
from typing import List
from pathlib import Path
from .models import DataRecord


class CSVLoader:
    """
    Load data to CSV file.
    
    TODO: Write DataRecords to CSV
    """
    
    def __init__(self, filepath: str):
        """TODO: Store filepath, initialize buffer"""
        self.filepath = filepath
        self.records = []
    
    def load(self, record: DataRecord) -> None:
        """
        Add record to buffer.
        
        TODO: Append record to self.records list
        """
        pass
    
    def save(self) -> None:
        """
        Write all buffered records to CSV file.
        
        TODO:
        1. Create parent directories if needed
        2. Get fieldnames from first record
        3. Open file and create csv.DictWriter
        4. Write header and all rows
        
        Hint: Path(self.filepath).parent.mkdir(parents=True, exist_ok=True)
        Hint: fieldnames = list(self.records[0].data.keys())
        Hint: writer.writeheader()
              writer.writerows([r.data for r in self.records])
        """
        pass


class JSONLoader:
    """
    Load data to JSON file.
    
    TODO: Write DataRecords to JSON
    """
    
    def __init__(self, filepath: str, pretty: bool = True):
        """TODO: Store filepath and pretty flag"""
        self.filepath = filepath
        self.pretty = pretty
        self.records = []
    
    def load(self, record: DataRecord) -> None:
        """
        Add record to buffer.
        
        TODO: Append record to self.records list
        """
        pass
    
    def save(self) -> None:
        """
        Write all records to JSON file.
        
        TODO:
        1. Create parent directories
        2. Convert records to list of dicts
        3. Write to JSON file with optional pretty printing
        
        Hint: data = [r.data for r in self.records]
        Hint: json.dump(data, f, indent=2 if self.pretty else None)
        """
        pass

