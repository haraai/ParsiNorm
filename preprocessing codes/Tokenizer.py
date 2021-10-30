import re


class Tokenizer:
    def __init__(self):
        self.pattern_abbreviation = r"\b[آ-ی](?=([.]))(?:\1[آ-ی])*\b"

    def remove_dot_in_abbrevations(self, sentence):
        abbrevations = [x.group() for x in re.finditer(self.pattern_abbreviation, sentence)]
        for abbrevation in abbrevations:
            abbrevation_with_end_dot = abbrevation + "."
            modified_abbrevation = abbrevation_with_end_dot.replace(".", " ")
            sentence = sentence.replace(abbrevation_with_end_dot, modified_abbrevation)
            modified_abbrevation = abbrevation.replace(".", " ")
            sentence = sentence.replace(abbrevation, modified_abbrevation)
        return sentence

    def replace_other(self, sentence):
        others = re.findall('و\.\.\.', sentence)
        if others:
            for other in others:
                sentence = sentence.replace(str(other), "و غیره")
        more_dots = re.findall('\.\.+', sentence)
        if more_dots:
            for more_dot in more_dots:
                sentence = sentence.replace(str(more_dot), " ")

        return sentence

    def add_tab(self, sentence):
        sentence = sentence.group()  # this method return the string matched by re
        sentence = sentence.strip(' ')  # ommiting the whitespace around the pucntuation
        sentence = sentence.strip('\n')  # ommiting the newline around the pucntuation
        sentence = " " + sentence + "\t\t"  # adding a space after and before punctuation
        return sentence

    def sentence_tokenize(self, sentence):
        sentence = self.remove_dot_in_abbrevations(sentence)
        # finding the numbers
        pattern = r"[-+]?\d*\.\d+|\d+"
        nums_list = re.findall(pattern, sentence)
        sentence = re.sub(pattern, 'floatingpointnumber', sentence)

        pattern = r'([!\.\?؟]+)[\n]*'
        tmp = re.findall(pattern, sentence)
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r':\n'
        tmp = re.findall(pattern, sentence)
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r';\n'
        tmp = re.findall(pattern, sentence)
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r'؛\n'
        tmp = re.findall(pattern, sentence)
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r'[\n]+'
        sentence = re.sub(pattern, self.add_tab, sentence)

        for number in nums_list:
            pattern = 'floatingpointnumber'
            sentence = re.sub(pattern, number, sentence, 1)

        sentence = sentence.split('\t\t')
        sentence = [x for x in sentence if len(x) > 0]
        return sentence
