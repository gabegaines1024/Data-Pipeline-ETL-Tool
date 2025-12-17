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
        """Execute the ETL pipeline."""
        processed = 0
        filtered = 0
        
        # Extract records one at a time
        for record in self.extractor.extract():
            processed += 1  # Count every record we see
            
            # Apply ALL transformers in sequence
            for transformer in self.transformers:
                record = transformer.transform(record)
                if record is None:  # Transformer filtered it out
                    filtered += 1
                    break  # Stop processing this record
            
            # AFTER all transformers, load if not filtered
            if record is not None:
                self.loader.load(record)
        
        # Write all buffered records to file
        self.loader.save()
        
        return {
            'processed': processed,
            'filtered': filtered,
            'loaded': processed - filtered
        }