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
    
    This example:
    1. Extracts data from CSV
    2. Cleans string fields (strips whitespace)
    3. Filters records where age >= 21
    4. Saves result to JSON
    """
    print("=" * 50)
    print("ETL Pipeline Starting...")
    print("=" * 50)
    
    # 1. Setup Extractor
    print("\n1. Setting up CSV extractor...")
    extractor = CSVExtractor("data/raw/sample_input.csv")
    
    # 2. Setup Transformers
    print("2. Setting up transformers...")
    transformers = [
        StringCleaner(strip=True, lowercase=False),  # Clean whitespace
        FilterTransformer(lambda r: int(r.get("age", 0)) >= 21)  # Adults only
    ]
    
    # 3. Setup Loader
    print("3. Setting up JSON loader...")
    loader = JSONLoader("data/output/processed_adults.json", pretty=True)
    
    # 4. Create and Run Pipeline
    print("\n4. Running pipeline...")
    pipeline = Pipeline(extractor, transformers, loader)
    stats = pipeline.run()
    
    # 5. Print Results
    print("\n" + "=" * 50)
    print("Pipeline Complete! ✓")
    print("=" * 50)
    print(f"Total Records Processed: {stats['processed']}")
    print(f"Records Filtered Out:    {stats['filtered']}")
    print(f"Records Loaded:          {stats['loaded']}")
    print(f"\nOutput saved to: data/output/processed_adults.json")
    print("=" * 50)


if __name__ == "__main__":
    main()
