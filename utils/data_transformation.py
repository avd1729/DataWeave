import pandas as pd
import os
from pathlib import Path

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
            
        # Read and process data
        df = pd.read_json(input_file_path)
        df = df.drop_duplicates()
        print(f'Loaded {len(df)} unique examples. Here are the first few:')
        print(df.head())
        
        # Split data
        train_df = df.sample(frac=train_fraction, random_state=random_state)
        test_df = df.drop(train_df.index)
        
        print(f'\nSplit data into:')
        print(f'Training set: {len(train_df)} examples')
        print(f'Test set: {len(test_df)} examples')
        
        # Save files
        train_path = os.path.join(train_output_dir, 'train.jsonl')
        test_path = os.path.join(test_output_dir, 'test.jsonl')
        
        train_df.to_json(train_path, orient='records', lines=True)
        test_df.to_json(test_path, orient='records', lines=True)
        
        print(f'\nSaved files:')
        print(f'Training data: {train_path}')
        print(f'Test data: {test_path}')
        
        return train_df, test_df
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The input file '{input_file_path}' is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Configure paths
    input_file = "data/extracted_data/menu_examples.json"
    train_dir = "data/train_data"
    test_dir = "data/test_data"
    
    # Process data
    train_df, test_df = process_data(
        input_file_path=input_file,
        train_output_dir=train_dir,
        test_output_dir=test_dir
    )