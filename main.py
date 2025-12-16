"""
Main entry point for the ETL pipeline.

TODO: Implement a complete example pipeline that:
1. Loads data from CSV
2. Cleans and filters it
3. Saves to JSON
"""

from src import (
    Pipeline,
    CSVExtractor,
    JSONExtractor,
    StringCleaner,
    FilterTransformer,
    CSVLoader,
    JSONLoader,
)


def main():
    """
    Run the ETL pipeline.
    
    TODO: Implement the following steps:
    
    1. Create sample input data (or use existing file)
    2. Create an extractor (CSVExtractor or JSONExtractor)
    3. Create transformers:
       - StringCleaner to clean text fields
       - FilterTransformer to remove unwanted records
    4. Create a loader (CSVLoader or JSONLoader)
    5. Create Pipeline with extractor, transformers, and loader
    6. Run pipeline and print results
    
    Example structure:
        # Setup
        extractor = CSVExtractor("data/raw/input.csv")
        transformers = [
            StringCleaner(strip=True, lowercase=True),
            FilterTransformer(lambda r: r.get("age", 0) > 18)
        ]
        loader = JSONLoader("data/output/processed.json")
        
        # Create and run pipeline
        pipeline = Pipeline(extractor, transformers, loader)
        stats = pipeline.run()
        
        print(f"Pipeline complete!")
        print(f"Processed: {stats['processed']} records")
        print(f"Filtered: {stats['filtered']} records")
        print(f"Loaded: {stats['loaded']} records")
    """
    print("ETL Pipeline - TODO: Implement main()")
    
    # TODO: Your implementation here
    pass


if __name__ == "__main__":
    main()
