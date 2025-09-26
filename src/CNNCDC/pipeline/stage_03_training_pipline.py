from CNNCDC.config.configuration import ConfigurationManager
from CNNCDC.components.training import Training
from CNNCDC.components.prepare_callbacks import PrepareCallbacks
from CNNCDC import logger

# Define a constant for the stage name, used in logging
STAGE_NAME = "Traning the model"

# Define the main pipeline class for this stage
class TrainingModelPipline:
    def __init__(self):
        # Constructor for the pipeline class.
        pass

    def main(self):
        """
        Executes the main logic for the 'Prepare base model' pipeline stage.
        
        This method gets the configuration, creates the component, and runs its
        primary functions to prepare the base model for training.
        """
        # Create an instance of the ConfigurationManager
        config = ConfigurationManager()

        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks( config = prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        
        # 1. Load the model's architecture and weights.
        training.get_base_model() 
        
        # 2. Re-compile the model. This is the crucial step.
        training.compile_model() 
        
        # 3. Set up the data generators.
        training.train_valid_generator()
        
        # 4. Start the training process.
        training.train(
            callbacks_list=callback_list
        )

# Entry point of the script
if __name__ == '__main__':
    try:
        # Log the start of the current stage
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Started <<<<<<<<<<<")
        
        # Create and run the pipeline object
        obj = TrainingModelPipline()
        obj.main()
        
        # Log the completion of the stage
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nX============X")

    except Exception as e:
        # Log any exceptions that occur during the process and re-raise them
        logger.exception(e)
        raise e