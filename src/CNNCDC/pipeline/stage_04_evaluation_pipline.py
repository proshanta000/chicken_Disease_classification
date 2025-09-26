# Import necessary modules
from CNNCDC.config.configuration import ConfigurationManager
from CNNCDC.components.model_evaluation import Evaluation
from CNNCDC import logger

# Define a constant for the stage name to be used in logging
STAGE_NAME = "MOdel Evaluation"

# Define the main pipeline class for the data ingestion stage
class ModelEvaluationConfig:
    def __init__(self):
        # The constructor can be used to set up initial properties if needed.
        # In this case, it's empty as the main logic is in the 'main' method.
        pass

    def main(self):
        """
        Executes the main logic for the data ingestion pipeline.
        
        This method orchestrates the two primary steps:
        1. Getting the configuration for data ingestion.
        2. Creating a DataIngestion object and executing its methods.
        """
        # Create an instance of ConfigurationManager to access the configurations
        config = ConfigurationManager()
        
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation= Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()

# Entry point of the script
if __name__ == '__main__':
    try:
        # Log the start of the data ingestion stage
        logger.info(f"********************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        
        # Create an instance of the pipeline class
        obj = ModelEvaluationConfig()
        
        # Run the main method of the pipeline
        obj.main()
        
        # Log the successful completion of the stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========X")
    except Exception as e:
        # If any exception occurs, log it and re-raise to halt the process
        logger.exception(e)
        raise e