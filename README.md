# Simple ETL Data Pipeline

A lightweight Extract-Transform-Load pipeline for processing data from CSV/JSON sources.

## Project Structure

```
data_pipeline/
├── src/
│   ├── models.py        # DataRecord model
│   ├── extractors.py    # CSV and JSON extractors
│   ├── transformers.py  # Data cleaning and filtering
│   ├── loaders.py       # CSV and JSON loaders
│   ├── pipeline.py      # Main pipeline orchestrator
│   └── utils/
│       ├── priority_queue.py  # Job scheduling utilities
│       └── lru_cache.py       # Caching utilities
├── config/
│   └── pipeline_config.yaml   # Configuration
├── data/
│   ├── raw/            # Input data
│   ├── processed/      # Intermediate data
│   └── output/         # Final output
├── tests/
│   └── test_pipeline.py
└── main.py             # Entry point

```

## Getting Started

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from src import Pipeline, CSVExtractor, StringCleaner, JSONLoader

# Create components
extractor = CSVExtractor("data/raw/input.csv")
transformers = [StringCleaner(strip=True)]
loader = JSONLoader("data/output/processed.json")

# Build and run pipeline
pipeline = Pipeline(extractor, transformers, loader)
stats = pipeline.run()

print(f"Processed {stats['loaded']} records")
```

## Components to Implement

### 1. Models (`src/models.py`)
- `DataRecord`: Container for data with get/set methods

### 2. Extractors (`src/extractors.py`)
- `CSVExtractor`: Read from CSV files
- `JSONExtractor`: Read from JSON files

### 3. Transformers (`src/transformers.py`)
- `StringCleaner`: Clean text data
- `FilterTransformer`: Filter records based on conditions

### 4. Loaders (`src/loaders.py`)
- `CSVLoader`: Write to CSV
- `JSONLoader`: Write to JSON

### 5. Pipeline (`src/pipeline.py`)
- `Pipeline`: Orchestrate ETL process

### 6. Main (`main.py`)
- Set up and run a complete example

## Practice Plan

Start with these files in order:

1. **`src/models.py`** - Simplest, just a data container
2. **`src/extractors.py`** - Practice file I/O and iteration
3. **`src/loaders.py`** - More file I/O practice
4. **`src/transformers.py`** - Data manipulation
5. **`src/pipeline.py`** - Putting it all together
6. **`main.py`** - Create a working example
7. **`tests/test_pipeline.py`** - Write tests

## Extending Later

If you want to expand this later, consider adding:
- API extractors
- Database loaders
- More transformers (type conversion, validation, etc.)
- Scheduling and monitoring
- Error handling and retry logic

## Running Tests

```bash
pytest tests/
```
