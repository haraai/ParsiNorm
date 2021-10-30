import argparse
import string
from hazm import POSTagger, Normalizer, word_tokenize
import re
from num2fawords import words, HUNDREDS
import sys

sys.path.append("/hdd4/callcenter_repo/tokenizer")
from tokenizer.public_tokenizer import make_tokens

class PreProcess(object):

    def __init__(self, filepath, outputpath, unkpath):
        super(PreProcess).__init__()
        self.InputPath = filepath
        self.OutputPath = outputpath
        self.UnkPath = unkpath
        self.input = open(self.InputPath, mode="r", encoding="utf-8")
        self.output = open(self.OutputPath, mode="w", encoding="utf-8")
        self.unk = open(self.UnkPath, mode="w", encoding="utf-8")
        self.tagger = POSTagger(model="/hdd4/callcenter_storage/models/phonemizer/" + "postagger.model")
        self.normalizer = Normalizer()

        self.sentence_number = 0

        self.English_digits = '0123456789'
        self.Persian_digits = '۰٠۱١۲٢۳٣۴٤۵٥۶٦۷٧۸٨۹٩'
        self.DesiredCharacter = "[۰-۹ 0-9 آ-ی \s، . ()!؟:]"
        self.punctuation = list(set('،؟.!@_{}[]#$?؟.,:+";*&^%)(=\'\\/|' + '!@#$?.,:+";*&^%)(=\'\\/|«»–-_…' + '<>؟،؛٬;`~|'))
        # self.english = string.ascii_uppercase + string.ascii_lowercase
        # English_Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
        # self.DesiredCharacter = "[۰-۹ 0-9 آ-ی \s، . ()!؟:]"
        # self.English_digits = '0123456789'
        # self.Persian_digits = '۰٠۱١۲٢۳٣۴٤۵٥۶٦۷٧۸٨۹٩'

        HUNDREDS[1] = 'صد'
        HUNDREDS[2] = 'دویست'
        HUNDREDS[3] = 'سیصد'
        HUNDREDS[4] = 'چهارصد'
        HUNDREDS[5] = 'پانصد'
        HUNDREDS[6] = 'ششصد'
        HUNDREDS[7] = 'هفتصد'
        HUNDREDS[8] = 'هشتصد'
        HUNDREDS[9] = 'نهصد'

    def EditFont(self, line):

        line = line.replace('أ', 'ا')
        line = line.replace('إ', 'ا')
        line = line.replace('ٱ', 'ا')
        line = line.replace('ٵ', 'ا')

        line = line.replace('ۂ', 'ه')
        line = line.replace('ۀ', 'ه')
        line = line.replace('ة', 'ه')

        line = line.replace('ی', 'ی')
        line = line.replace('ي', 'ی')
        line = line.replace('ئ', 'ی')
        line = line.replace('ٸ', 'ی')
        line = line.replace('ې', 'ی')
        line = line.replace('ے', 'ی')
        line = line.replace('ۓ', 'ی')
        line = line.replace('ی', 'ی')

        line = line.replace('ؤ', 'و')
        line = line.replace('ۆ', 'و')
        line = line.replace('ٶ', 'و')
        line = line.replace('ٷ', 'و')
        line = line.replace('ۉ', 'و')
        line = line.replace('ۇ', 'و')
        line = line.replace('ۆ', 'و')

        line = line.replace('ك', 'ک')
        line = line.replace('ڪ', 'ک')
        line = line.replace('ګ', 'ک')

        line = line.replace('ء', '')
        line = line.replace('ھ', 'ه')

        line = line.replace('ّ', '')  # tashdid
        line = line.replace('َ', '')  # fatheh
        line = line.replace('ِ', '')  # kasreh
        line = line.replace('ُ', '')  # zameh

        line = line.replace('ࣰ', '')  # tanvin
        line = line.replace('ࣱ', '')  # tanvin
        line = line.replace('ࣲ', '')  # tanvin

        # line = line.replace('.', '/')  # float

        line = line.replace('0', '۰')
        line = line.replace('1', '۱')
        line = line.replace('2', '۲')
        line = line.replace('3', '۳')
        line = line.replace('4', '۴')
        line = line.replace('5', '۵')
        line = line.replace('6', '۶')
        line = line.replace('7', '۷')
        line = line.replace('8', '۸')
        line = line.replace('9', '۹')

        line = line.replace("\u200c", " ")  # Nimfasele

        return line

    def Remove_punctuation(self, line):
        s = ""
        for ch in line:
            flag = True
            for p in self.punctuation:
                if (p == ch):
                    flag = False
            if (flag):
                s += ch
        return s

    def RemoveNewLine(self, line):
        if ((line == "") or (line == "\n")):
            self.output.write("\n")
        return line.replace('\n', ' ').strip()

    def edit_special_chars(self, line):
        return re.sub(r"[\x09-\x0c]", '', line)

    def VerbSeperator(self, line):
        sentences = []
        normalizer = Normalizer()
        line = normalizer.normalize(line)
        tagged = self.tagger.tag(word_tokenize(line))

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

    def RemoveOtherLanguages(self, line):
        return ''.join(re.findall(self.DesiredCharacter, line))

    def RemoveParentheses(self, line):
        if not (("(" in line) and (")" in line)):
            return line
        idx1 = line.find(')')
        idx2 = line.find('(')
        return line[:idx2] + ' ' + line[idx1+1:]

    def Remove_repeat_characters(self, line):
        splited_line = line.split(' ')
        s = []
        for word in splited_line:
            if (len(set(word)) <= 1):
                continue
            s.append(word)
        return ' '.join(s)



    def UNK_token(self, sentence):
        tokens = make_tokens(sentence)[1]
        if ('UNK' in tokens):
            return True, tokens
        else:
            return False, tokens

    def SaveToFile(self, sentences):
        for s in sentences:
            unk, tokens = self.UNK_token(s)
            if unk:
                self.unk.write(s + ' | ' + tokens + "\n")
            self.output.write(s)
            self.sentence_number += 1

    def ConvertNumberToLetter(self, line):
        newline = ''
        number = ''
        counter = 0
        for char in line:
            if (char in self.English_digits) or (char in self.Persian_digits):
                number += char
                if counter == len(line) - 1:
                    if len(number) == 4:
                        newline += words(number).replace('یک هزار', 'هزار')
                    else:
                        newline += words(number)
            else:
                if number:
                    if len(number) == 4:
                        newline += words(number).replace('یک هزار', 'هزار')
                    else:
                        newline += words(number)
                    number = ''
                newline += char
                if char == '\n':
                    break
            counter += 1
        return newline

    def ImproveText(self):
        line = self.input.readline()
        idx = 0

        while line:

            try:
                idx = idx + 1
                line = self.normalizer.normalize(line)
                line = self.Remove_repeat_characters(line)
                line = self.RemoveNewLine(line)
                line = self.EditFont(line)
                # line = self.RemoveParentheses(line)
                line = self.Remove_punctuation(line)
                # line = self.RemoveParentheses(line)
                line = self.RemoveOtherLanguages(line)
                sentences = self.VerbSeperator(line)
                self.SaveToFile(sentences)

            except Exception as e:
                print('error is {} in line: {} with idx: {}'.format(e, line, idx))
            line = self.input.readline()
            if idx % 10000 == 0:
                print(idx)

        print('\nsaved path = ', self.OutputPath)
        print('sentence number = ', self.sentence_number)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw', type=str, default='sample.txt')
    parser.add_argument('--output', type=str, default='cleaned_sample.txt')
    parser.add_argument('--unk', type=str, default='unk.txt')
    # parser.add_argument('--raw', type=str, default='/hdd4/callcenter_storage/data/Language_Model/raw/subtitle/opensubtitle.txt')
    # parser.add_argument('--output', type=str, default='/hdd4/callcenter_storage/data/Language_Model/process/subtitle/opensubtitle.txt')
    # parser.add_argument('--unk', type=str, default='/hdd4/callcenter_storage/data/Language_Model/process/subtitle/opensubtitle_unk.txt')
    args = parser.parse_args()
    pre_process = PreProcess(args.raw, args.output, args.unk)
    pre_process.ImproveText()


if __name__ == '__main__':
    main()