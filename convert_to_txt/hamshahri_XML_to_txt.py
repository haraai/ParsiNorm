import pandas as pd
from bs4 import BeautifulSoup
import os


def save_to_file(sentence, path):
    with open(path, 'a') as file:
        file.write(str(sentence))


for filename in os.listdir('/hdd4/callcenter_storage/data/Language_Model/raw/hamshahri/hamshahri_dataset/2007'):
    with open('/hdd4/callcenter_storage/data/Language_Model/raw/hamshahri/hamshahri_dataset/2007/' + filename,
              'r') as f:
        data = f.read()
    Bs_data = BeautifulSoup(data, "xml")
    texts = Bs_data.find_all('TEXT')
    for text in texts:
        text = str(text).replace("</TEXT>", "").replace("<TEXT>", "")
        save_to_file(text,
                     "/hdd5/romina/bert/pre-processing/dataset/all_hamshahri.txt")
