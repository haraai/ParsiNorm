import re
import os
from hazm import POSTagger
import string


class Tokenizer:
    def __init__(self):
        self.english_characters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        self.persian_pattern_abbreviation = r"\b[آ-ی](?=([.]))(?:\1[آ-ی])*\b.?"
        self.english_pattern_abbreviation = r"\b[A-Z](?=([.]))(?:\1[A-Z])*\b.?"
        repo_root = os.path.dirname(__file__) + '/../../'
        self.tagger = POSTagger(model="resources/postagger.model")
        self.punctuation_pattern = re.compile(r'([؟!\?]+|\d[\d\.:\/\\]+\d|\d+|[:\.،؛»\]\)\}"«\[\(\{])')
        self.mail_pattern = re.compile(r"[A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+")
        self.url_pattern = re.compile(
            r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
        self.hashtag_pattern = re.compile(r"#(\w+)")
        self.mention_pattern = re.compile(r"\B@(?!(?:[a-z0-9.]*_){2})(?!(?:[a-z0-9_]*\.){2})[._a-z0-9]{3,24}\b")
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

    def remove_space_in_dot(self, sentences):
        if ' .' in sentences:
            if len(sentences) == 2 and sentences[0] == ' .':
                sentences[1] += sentences[0].strip()
                sentences.remove(sentences[0])
            else:
                dot_index = sentences.index(' .')
                sentences[dot_index - 1] = sentences[dot_index - 1] + sentences[dot_index]
                sentences.pop(dot_index)

    def sentence_tokenize(self, sentence, verb_seperator):
        # finding the abbrevations
        persian_abbrs = [x.group() for x in re.finditer(self.persian_pattern_abbreviation, sentence)]
        english_abbrs = [x.group() for x in re.finditer(self.english_pattern_abbreviation, sentence)]
        sentence = re.sub(self.persian_pattern_abbreviation, 'PERSIANABBRR', sentence)
        sentence = re.sub(self.english_pattern_abbreviation, 'ENGGABBRR', sentence)
        # finding the numbers
        pattern = r"[-+]?\d*\.\d+|\d+"
        nums_list = re.findall(pattern, sentence)
        sentence = re.sub(pattern, 'FLOATPPOOOINTNUMBER', sentence)
        # finding emails
        emails = re.findall(self.mail_pattern, sentence)
        sentence = re.sub(self.mail_pattern, "EEMMAAIILL", sentence)
        # finding urls
        urls = re.findall(self.url_pattern, sentence)
        urls = [x[0] for x in urls]
        sentence = re.sub(self.url_pattern, "UURRLLSS", sentence)

        pattern = r'([!\.\?؟]+)[\n]*'
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r':\n'
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r';\n'
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r'؛\n'
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = r'[\n]+'
        sentence = re.sub(pattern, self.add_tab, sentence)

        pattern = 'FLOATPPOOOINTNUMBER'
        for number in nums_list:
            sentence = re.sub(pattern, number, sentence, 1)
        pattern = 'ENGGABBRR'
        for english_abbr in english_abbrs:
            sentence = re.sub(pattern, english_abbr, sentence, 1)
        pattern = 'PERSIANABBRR'
        for persian_abbr in persian_abbrs:
            sentence = re.sub(pattern, persian_abbr, sentence, 1)
        pattern = 'EEMMAAIILL'
        for email in emails:
            sentence = re.sub(pattern, email, sentence, 1)
        pattern = 'UURRLLSS'
        for url in urls:
            sentence = re.sub(pattern, url, sentence, 1)
        sentences = sentence.split('\t\t')
        self.remove_space_in_dot(sentences)
        sentences = [x for x in sentences if len(x.strip()) > 0]
        if verb_seperator:
            for index in range(len(sentences)):
                sentences_with_verb_seperator = self.verbSeperator(sentences[index])
                sentences_with_verb_seperator.reverse()
                sentences_with_verb_seperator = [x for x in sentences_with_verb_seperator if len(x.strip()) > 0]
                if len(sentences_with_verb_seperator) > 1:
                    self.remove_space_in_dot(sentences_with_verb_seperator)
                    sentences.pop(index)
                    for sent in sentences_with_verb_seperator:
                        sentences.insert(index, sent)
        return sentences

    def verbSeperator(self, line):
        line = str(line)
        sentences = []
        tagged = self.tagger.tag(self.word_tokenize(line))

        has_verb = True
        verb_count = 0
        for i, word in enumerate(self.word_tokenize(line)):
            if tagged[i][1] == 'V':
                has_verb = False
                verb_count += 1
        if has_verb:
            sentences.append(line)
            return sentences

        temp = ''
        verb_found = 0
        for i, word in enumerate(self.word_tokenize(line)):
            temp = temp + ' ' + word
            if tagged[i][1] == 'V':
                verb_found += 1
                sentences.append(temp)
                temp = ''
            if i == len(self.word_tokenize(line)) - 1 and verb_count == verb_found and tagged[i][1] != 'V':
                sentences.append(temp)
        return sentences

    def is_mix(self, word):
        word1 = None
        word2 = None
        language = ""
        for index in range(len(word)):
            if word[index] in self.english_characters:
                if language == "Farsi":
                    language = "mix"
                    word1 = word[index:]
                    word2 = word[:index]
                    break
                else:
                    language = "English"
            else:
                if language == "English":
                    language = "mix"
                    word1 = word[index:]
                    word2 = word[:index]
                    break
                else:
                    language = "Farsi"
        if language == "mix":
            return language, word1, word2
        else:
            return language, word, None

    def word_tokenize(self, sentence):
        emails = re.findall(self.mail_pattern, sentence)
        sentence = re.sub(self.mail_pattern, "EEMMAAIILL", sentence)
        urls = re.findall(self.url_pattern, sentence)
        urls = [x[0] for x in urls]
        sentence = re.sub(self.url_pattern, "UURRLLSS", sentence)
        hashtags = re.findall(self.hashtag_pattern, sentence)
        sentence = re.sub(self.hashtag_pattern, "HHAASHSHTTAAGG", sentence)
        mentions = re.findall(self.mention_pattern, sentence)
        sentence = re.sub(self.mention_pattern, "MMEENNTION", sentence)
        for index in range(len(hashtags)):
            language, _, _ = self.is_mix(hashtags[index])
            if language == "English":
                hashtags[index] = hashtags[index] + "#"
            else:
                hashtags[index] = "#" + hashtags[index]
        sentence = re.sub(self.punctuation_pattern, r' \1 ', sentence)
        sentence = re.sub(self.emoji_pattern, r' \1 ', sentence)
        sentence = sentence.replace('\n', ' ').replace('\t', ' ')
        tokens = sentence.strip().split()
        for token in tokens:
            language, word1, word2 = self.is_mix(token)
            if language == "mix":
                index_of_element = tokens.index(token)
                tokens.pop(index_of_element)
                tokens.insert(index_of_element, word1)
                tokens.insert(index_of_element, word2)
            if token == "EEMMAAIILL":
                index_of_email = tokens.index("EEMMAAIILL")
                tokens.pop(index_of_email)
                tokens.insert(index_of_email, emails[0])
                emails.pop(0)
            if token == "UURRLLSS":
                index_of_url = tokens.index("UURRLLSS")
                tokens.pop(index_of_url)
                tokens.insert(index_of_url, str(urls[0]))
                urls.pop(0)
            if token == "HHAASHSHTTAAGG":
                index_of_hashtag = tokens.index("HHAASHSHTTAAGG")
                tokens.pop(index_of_hashtag)
                tokens.insert(index_of_hashtag, str(hashtags[0]))
                hashtags.pop(0)
            if token == "MMEENNTION":
                index_of_mention = tokens.index("MMEENNTION")
                tokens.pop(index_of_mention)
                tokens.insert(index_of_mention, mentions[0])
                mentions.pop(0)
        tokens = [x.strip("\u200c") for x in tokens if len(x.strip("\u200c")) != 0]
        tokens = [x.strip() for x in tokens]
        return tokens
