
import os
from CNNCDC import logger
from CNNCDC.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from CNNCDC.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipline
from CNNCDC.pipeline.stage_03_traning_pipline import TrainingModelPipline


STAGE_NAME = "Data Ingestion Stage"


if __name__=='__main__':
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>>  stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionTraningPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX============X")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} Started <<<<<<<<<<<")
    obj= PrepareBaseModelPipline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nX============X")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Traning the model"

try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} Started <<<<<<<<<<<")
    obj= TrainingModelPipline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nX============X")

except Exception as e:
    logger.exception(e)
    raise e