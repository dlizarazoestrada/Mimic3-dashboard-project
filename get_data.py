import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Descarga el dataset
dataset = 'asjad99/mimiciii'
path = os.getcwd()
api.dataset_download_files(dataset, path=path, unzip=True)
