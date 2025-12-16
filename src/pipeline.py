"""Simple ETL Pipeline orchestrator."""
from typing import List


class Pipeline:
    """
    Coordinates extract, transform, and load operations.
    
    TODO: Run the complete ETL process
    """
    
    def __init__(self, extractor, transformers: List, loader):
        """
        TODO: Store extractor, transformers list, and loader
        """
        pass
    
    def run(self) -> dict:
        """
        Execute the ETL pipeline.
        
        TODO:
        1. Extract records from extractor
        2. For each record:
           a. Apply each transformer in order
           b. If transformer returns None, skip record (filtered)
           c. Otherwise, load the transformed record
        3. After all records, call loader.save()
        4. Return stats (records processed, filtered, loaded)
        
        Hint:
        processed = 0
        filtered = 0
        for record in self.extractor.extract():
            processed += 1
            # Apply transformers
            for transformer in self.transformers:
                record = transformer.transform(record)
                if record is None:
                    filtered += 1
                    break
            # Load if not filtered
            if record:
                self.loader.load(record)
        
        self.loader.save()
        return {"processed": processed, "filtered": filtered, "loaded": processed - filtered}
        """
        pass
