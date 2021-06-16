# Datasets-Models
Our goal is to help improve the precision agriculture and mycology communities. We believe that comunities are best served when ideas, information, and help is shared. Therefore we have committed to make these tools available to everyone. 

This repository contains a trained computer-vision model and community-contributed dataset to detect contamination on samples of myceliuym (https://detectcontam.oasisgardens.ai/). Although it is a work in progress, we hope that this will eventually be good enough to detect trichoderma and similar contaminants at an early stage before they spread and risk entire cultures, grow rooms, etc. 

You can contribute labeled images of clean and contamitated mycelium to improve the model here (https://contributecontam.oasisgardens.ai/). Please do! These models are open for use by the community, and you will be able to find your submission in the folder after a few days, since we go through them manually to avoid bad data.

If you would like to contribute in other ways (development, promotion, organizing) please contact us through our website: https://oasis-iot.square.site/

The image dataset is available here: https://www.kaggle.com/oasisdata/mycelium-contamination-images
Models in this repository:
  1. (BestLossModel.mdl_wts.hdf5) Binary classification: contaminated vs clean mycelium
