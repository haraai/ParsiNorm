import random
import argparse
import string
import random
from hazm import POSTagger, Normalizer, word_tokenize
import re
from num2fawords import words, HUNDREDS
import sys
from get_phonetic import get_phonetic
from tqdm import tqdm
import os
from urlextract import URLExtract
import warnings

warnings.filterwarnings("ignore")

tagger = POSTagger(model="/hdd4/callcenter_storage/models/phonemizer/" + "postagger.model")
normalizer = Normalizer()


def VerbSeperator(line):
    sentences = []
    normalizer = Normalizer()
    line = normalizer.normalize(line)
    tagged = tagger.tag(word_tokenize(line))

    flag_has_verb = True
    for i, word in enumerate(word_tokenize(line)):
        if tagged[i][1] == 'V':
            flag_has_verb = False
    if flag_has_verb:
        sentences.append(line)
        return sentences

    temp = ''
    for i, word in enumerate(word_tokenize(line)):
        temp = temp + ' ' + word
        if tagged[i][1] == 'V':
            sentences.append(temp + '\n')
            temp = ''
    return sentences


def save_to_file(sentence, path):
    with open(path, 'a') as file:
        file.write(str(sentence) + os.linesep)


with open("./lines_with_english.txt", "r") as myfile:
    sentences = myfile.readlines()

selected_sentences = random.sample(sentences, 100000)

# removing mails and urls
extractor = URLExtract()
for index in tqdm(range(len(selected_sentences))):
    urls = extractor.find_urls(selected_sentences[index])
    if urls:
        for url in urls:
            selected_sentences[index] = selected_sentences[index].replace(url, " ")
    mails = re.findall('\S+@\S+', selected_sentences[index])
    if mails:
        for mail in mails:
            selected_sentences[index] = selected_sentences[index].replace(mail, " ")

# partitioning by verb and check sentences with english characters
english_chars = string.ascii_uppercase
english_chars += string.ascii_lowercase
lines_with_english = []
for index in tqdm(range(len(selected_sentences))):
    seprated_sentences = VerbSeperator(selected_sentences[index])
    for seprated_sentence in seprated_sentences:
        has_english = False
        for character in seprated_sentence:
            if character in english_chars:
                has_english = True
                lines_with_english.append(seprated_sentence)
                break

# remove \n at the end of sentences
for index in tqdm(range(len(lines_with_english))):
    lines_with_english[index] = lines_with_english[index].replace("\n", "")

# get errors in phonemizer
for index in tqdm(range(len(lines_with_english))):
    try:
        text, phonetic = get_phonetic(lines_with_english[index], cuda_device="cuda:1")
    except:
        save_to_file(lines_with_english[index], "./selected_errors.txt")
