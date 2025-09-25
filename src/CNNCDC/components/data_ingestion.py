import os
# Remove: import urllib.request as request
import zipfile
from CNNCDC.utils.common import get_size
from CNNCDC import logger
from pathlib import Path
from CNNCDC.entity.config_entity import DataIngestionConfig

import requests
from tqdm import tqdm 



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        # The file will only be downloaded if it doesn't already exist
        if not os.path.exists(self.config.local_data_file):
            logger.info("Starting file download...")

            # --- START: Progress Bar Implementation ---
            url = self.config.source_URL
            local_filename = self.config.local_data_file
            
            # 1. Initiate the request with streaming enabled
            response = requests.get(url, stream=True)
            response.raise_for_status() # Check for bad status code

            # 2. Get the total file size (Content-Length)
            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte
            
            # 3. Use tqdm to track progress
            progress_bar = tqdm(
                total=total_size_in_bytes, 
                unit='iB', 
                unit_scale=True, 
                desc=local_filename
            )

            # 4. Write to file and update the progress bar
            with open(local_filename, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            
            progress_bar.close()
            # --- END: Progress Bar Implementation ---
            
            # Check if download was complete (optional integrity check)
            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                logger.warning("Download integrity check failed. File size mismatch.")
            
            # This replaces the original logger.info call
            logger.info(f"{local_filename} downloaded successfully!")
        
        else: 
            # Original logic for file already existing
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):

        """
        Extracts a zip file into a specified directory.
        
        This method takes the path of a downloaded zip file and extracts its
        contents to the designated `unzip_dir`. It ensures the destination
        directory exists before extraction.
        """
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Zip file extracted to {unzip_path}")