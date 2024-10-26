import pandas as pd
import os
from pathlib import Path
import logging

# Configure logging
Path('logs').mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/data_transformer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def process_data(input_file_path, train_output_dir, test_output_dir, random_state=42, train_fraction=0.9):
    """
    Process data from a JSON file, split it into train/test sets, and save as JSONL files.
    
    Args:
        input_file_path (str): Path to input JSON file
        train_output_dir (str): Directory for training data
        test_output_dir (str): Directory for test data
        random_state (int): Random seed for reproducibility
        train_fraction (float): Fraction of data to use for training
    
    Returns:
        tuple: (train_df, test_df) DataFrames containing the split data
    """
    try:
        # Create output directories if they don't exist
        for directory in [train_output_dir, test_output_dir]:
            Path(directory).mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {directory}")
        
        # Read and process data
        logger.info(f"Reading data from {input_file_path}")
        df = pd.read_json(input_file_path)
        df = df.drop_duplicates()
        logger.info(f'Loaded {len(df)} unique examples')
        
        # Split data
        train_df = df.sample(frac=train_fraction, random_state=random_state)
        test_df = df.drop(train_df.index)
        
        logger.info(f'Split data into:')
        logger.info(f'Training set: {len(train_df)} examples')
        logger.info(f'Test set: {len(test_df)} examples')
        
        # Save files
        train_path = os.path.join(train_output_dir, 'train.jsonl')
        test_path = os.path.join(test_output_dir, 'test.jsonl')
        
        train_df.to_json(train_path, orient='records', lines=True)
        test_df.to_json(test_path, orient='records', lines=True)
        
        logger.info(f'Saved training data to: {train_path}')
        logger.info(f'Saved test data to: {test_path}')
        
        return train_df, test_df
        
    except FileNotFoundError:
        logger.error(f"Error: Input file '{input_file_path}' not found.")
        raise
    except pd.errors.EmptyDataError:
        logger.error(f"Error: The input file '{input_file_path}' is empty.")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    # Configure paths
    input_file = "data/extracted_data/menu_examples.json"
    train_dir = "data/train_data"
    test_dir = "data/test_data"
    
    # Process data
    try:
        logger.info("Starting data processing...")
        train_df, test_df = process_data(
            input_file_path=input_file,
            train_output_dir=train_dir,
            test_output_dir=test_dir
        )
        logger.info("Data processing completed successfully!")
    except Exception as e:
        logger.error("Data processing failed!", exc_info=True)