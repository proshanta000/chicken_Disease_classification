import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from CNNCDC.entity.config_entity import PrepareCallbacksConfig



class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _creat_tb_callbacks(self):
        timestamp= time.strftime("%Y-%m-%d-%H-%S")
        tb_runing_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir, 
            f"tb_logs_at_(timestamp)"
        )

        return tf.keras.callbacks.TensorBoard(log_dir=tb_runing_log_dir)
    
    @property
    def _creat_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath= self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    

    def get_tb_ckpt_callbacks(self):
        return[
            self._creat_tb_callbacks,
            self._creat_ckpt_callbacks
        ]