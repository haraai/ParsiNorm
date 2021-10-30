from multiprocessing import Pool
import sys
import os
import argparse
from nltk import flatten

from multiprocessing import Pool
import sys
import os
import argparse
from nltk import flatten

## normalization
sys.path += [os.path.abspath('.')]
sys.path += [sys.path[-1] + '/pre-processing/preprocessing codes/']
from clean import clean
from Tokenizer import Tokenizer

if __name__ == "__main__":

    clean = clean()
    tokenizer = Tokenizer()


    def save_to_file(file_path, data):
        with open(file_path, 'a', encoding='utf-8') as file:
            for line in data:
                file.write("%s\n" % line)


    def read_data(file_address):
        file = open(file_address, 'r', encoding='utf-8', errors='ignore')
        sentences = file.readlines()
        return sentences


    def pre_process_per_sentence(sentence):
        try:
            sentence = clean.clean_sentence(sentence)
            segment = []
            for sentence in tokenizer.sentence_tokenize(sentence):
                segment.append(sentence)
            return segment
        except:
            sentence


    def _print(sentences, processed_sentences):
        # for i, sentence in enumerate(processed_sentences):
        #     print("input = ", sentences[i])
        #     print("output = ", sentence)
        pass


    parser = argparse.ArgumentParser(description='normalization')
    parser.add_argument('-thread', '--thread_number', default=32, type=int, help='thread number')
    parser.add_argument('-input', '--input_file',
                        default='/hdd4/callcenter_storage/data/Language_Model/raw/miras/raw_miras/xaa',
                        help='path of input file')
    parser.add_argument('-output', '--output_file',
                        default='/hdd4/callcenter_storage/data/Language_Model/process/miras/raw_miras/xaa',
                        help='path of output file')
    args = sys.argv[1:]
    args = parser.parse_args(args)

    sentences = read_data(args.input_file)
    with Pool(args.thread_number) as p:
        try:
            processed_sentences = p.map(pre_process_per_sentence, sentences)
        except:
            print(processed_sentences)
            save_to_file("/hdd4/callcenter_storage/data/Language_Model/process/miras/raw_miras/errors.txt",
                         processed_sentences)
    save_to_file(args.output_file, flatten(processed_sentences))
