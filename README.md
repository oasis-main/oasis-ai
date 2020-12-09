# Datasets-Models
Our goal is to help improve the mycology community. We believe that communittes are best served when ideas, information, and help is shared. Therefore we have committed to make tools available to everyone. 

This repository contains a trained computer-vision model and community-contributed dataset to detect contamination in substrate (http://52.3.252.207:8501/). Although it is a work in progress, we hope that this will eventually be good enough to detect trichoderma and similar contaminants at an early stage before they spread and risk entire cultures, grow rooms, etc. 

You can contribute labeled images of clean and contamitated mycelium to improve the model here (http://100.26.163.60:8501/). Please do! These models are open for use by the community, and you will be able to find your submission in the folder after a few days, since we go through them manually to avoid bad data.

If you would like to contribute in other ways (development, promotion, organizing) please contact mike@oasisregenerative.com

The image dataset is available here: https://www.kaggle.com/oasisregenerative/mycelium-contamination-image-dataset

Models in this repository:
  1. (BestLossModel.mdl_wts.hdf5) Binary classification: contaminated vs clean mycelium
