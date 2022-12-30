## Requirements
gensim==4.3.0\
h5py==3.7.0\
nlg-metricverse==0.9.6\
nltk==3.7\
pickleshare==0.7.5\
Pillow==9.3.0\
tokenizers==0.13.2\
torch==1.13.1\
torchtext==0.14.1\
torchvision==0.14.1\
progressbar2==4.2.0

install Python requirements:
```
pip install -r requirements.txt
```
## Downloads and Setup
Once you clone this repo, run the vocab.py, store_dataset.py, split_dataset.py, train_vqgrad.py and evaluate_vqgrad.py file to process the dataset, to train and evaluate the model.
```shell
$ python vocab.py
$ python store_dataset.py
$ python train_vqgrad.py
$ python evaluate_vqgrad.py
```

## Citation
This repository was implemented and extended based on the following previous work:

```
@Article{info12080334,
AUTHOR = {Sarrouti, Mourad and Ben Abacha, Asma and Demner-Fushman, Dina},
TITLE = {Goal-Driven Visual Question Generation from Radiology Images},
JOURNAL = {Information},
VOLUME = {12},
YEAR = {2021},
NUMBER = {8},
ARTICLE-NUMBER = {334},
URL = {https://www.mdpi.com/2078-2489/12/8/334},
ISSN = {2078-2489}
}




```

## Contact
For more information, please contact me on ledri.thaqi[at]uzh.ch.


