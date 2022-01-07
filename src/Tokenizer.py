import re
from hazm import POSTagger, Normalizer, word_tokenize


class Tokenizer:
    def __init__(self):
        self.pattern_abbreviation = r"\b[آ-ی](?=([.]))(?:\1[آ-ی])*\b"
        self.tagger = POSTagger(model="resources/postagger.model")
        self.punctuation_pattern = re.compile(r'([؟!\?]+|\d[\d\.:\/\\]+\d|[:\.،؛»\]\)\}"«\[\(\{])')
        self.emoji_pattern = re.compile(
            "(["
            "\U00002500-\U00002BEF"  # chinese char
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F700-\U0001F77F"  # alchemical symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251"
            "\U0001f926-\U0001f937"
            "\U00010000-\U0010ffff"
            "\u23f0"
            "\u2640-\u2642"
            "\u2600-\u2B55"
            "\u200d"
            "\u23cf"
            "\u23e9"
            "\u231a"
            "\ufe0f"  # dingbats
            "\u3030"
            "])"
        )

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

    def VerbSeperator(self, line):
        line = str(line)
        sentences = []
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
                sentences.append(temp)
                temp = ''
        return sentences

    def word_tokenize(self, sentence):
        sentence = re.sub(self.punctuation_pattern, r' \1 ', sentence)
        sentence = re.sub(self.emoji_pattern, r' \1 ', sentence)
        sentence = sentence.replace('\n', ' ').replace('\t', ' ')
        tokens = sentence.strip().split()
        tokens = [x.strip("\u200c") for x in tokens if len(x.strip("\u200c")) != 0]
        return tokens
