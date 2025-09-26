from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for the data ingestion stage.
    """
    root_dir: Path  # Root directory where data ingestion artifacts are stored
    source_URL: str  # URL to the source data file
    local_data_file: Path  # Local path to save the downloaded data file
    unzip_dir: Path  # Directory where the data will be unzipped


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """
    Configuration for preparing the base model (VGG16).
    """
    root_dir: Path  # Root directory for this pipeline stage
    base_model_path: Path  # Path to the original VGG16 base model file
    updated_base_model_path: Path  # Path to the updated base model with a custom top layer
    params_image_size: list  # Dimensions of the input images
    params_learning_rate: float  # Learning rate for the optimizer
    params_include_top: bool  # Whether to include the final dense layer of the base model
    params_weights: str  # Pre-trained weights to use for the base model
    params_classes: int  # The number of output classes for the final layer



@dataclass(frozen= True)
class PrepareCallbacksConfig:
    root_dir:Path
    tensorboard_root_log_dir:Path
    checkpoint_model_filepath:Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
    params_learning_rate: float