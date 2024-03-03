from us_visa.components.data_ingestion import DataIngestion

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact

from us_visa.exception import USvisaException
from us_visa.logger import logging
import sys


class TrainingPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.dataingestion = DataIngestion()

    def start_data_ingestion(self)->DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e, sys) from e
        
    def run_pipeline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            #data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            #data_transformation_artifact = self.start_data_transformation(
            #    data_ingestion_artifact=data_ingestion_artifact, data_validation_artifact=data_validation_artifact)
            #model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)


        
        except Exception as e:
            raise USvisaException(e, sys) from e
