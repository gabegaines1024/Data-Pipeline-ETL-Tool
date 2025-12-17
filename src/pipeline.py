"""Simple ETL Pipeline orchestrator."""
from typing import List


class Pipeline:
    """
    Coordinates extract, transform, and load operations.
    """
    
    def __init__(self, extractor, transformers: List, loader):
       self.extractor = extractor
       self.transformers = transformers
       self.loader = loader
    
    def run(self) -> dict:
        """
        Execute the ETL pipeline.
        """
        processed = 0
        filtered = 0
        for record in self.extractor.extract():
            for transformer in self.transformers:
                record = transformer.transform(record)
                if record is None:
                    filtered += 1
                    break
                if record:
                    self.loader.load(record)
                    processed += 1
        self.loader.save()
        return {'processed': processed, 'filtered': filtered, 'loaded': processed - filtered}