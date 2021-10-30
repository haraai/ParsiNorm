import pandas as pd


def save_to_file(sentence, path):
    with open(path, 'a') as file:
        file.write(str(sentence))


df = pd.read_csv("/hdd4/callcenter_storage/data/Language_Model/raw/hamshahri/hamshahri_crawl1.csv")

for text in df["text"]:
    save_to_file(text,
                 "/hdd5/romina/bert/pre-processing/dataset/all_hamshahri_csv.txt")

df = pd.read_csv("/hdd4/callcenter_storage/data/Language_Model/raw/hamshahri/hamshahri_crawl2.csv")

for text in df["text"]:
    save_to_file(text,
                 "/hdd5/romina/bert/pre-processing/dataset/all_hamshahri_csv.txt")
