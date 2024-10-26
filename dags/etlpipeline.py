from airflow.decorators import dag, task
from pendulum import datetime
from utils import data_extraction , data_transformation , data_loading
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/main.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Starting dag...")


@dag(
    start_date=datetime(2024, 11, 19),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["data-gen"],
)

def main():
    
    @task
    def extract():
        try:
            # Initialize classes
            prompt = data_extraction.Prompt()
            generator = data_extraction.DataGenerator()

            logger.info("Started Data extraction...")
            # Generate examples and save to JSON
            df, json_path = generator.generate_and_save_examples(
                prompt=prompt.prompt,
                number_of_examples=5,
                filename="data/extracted_data/data.json"
            )
            logger.info("Data extraction completed successfully!")
            return df , json_path
    
        except Exception as e:
            logger.error("Data extraction failed!", exc_info=True)
            raise

    @task
    def transform():
        input_file = "data/extracted_data/data.json"
        train_dir = "data/train_data"
        test_dir = "data/test_data"
    
        # Process data
        try:
            logger.info("Starting Data processing...")
            train_df, test_df = data_transformation.process_data(
                input_file_path=input_file,
                train_output_dir=train_dir,
                test_output_dir=test_dir
            )
            logger.info("Data processing completed successfully!")
        except Exception as e:
            logger.error("Data processing failed!", exc_info=True)
            raise

    @task
    def load():
        try:
            logger.info("Starting Data Loading...")
            data_loading.main()
            logger.info("Data Loading completed successfully!")
        except Exception as e:
            logger.error("Data Loading failed!", exc_info=True)
            raise

        
        
main()