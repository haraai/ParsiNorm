import re
import string
from urlextract import URLExtract

extractor = URLExtract()


class data_cleaning:
    def __init__(self):
        self.punctuations = list(string.punctuation)
        self.white = list(string.whitespace)
        self.english = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.digits.extend(["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"])
        self.punctuations.extend(["؟"])
        self.persian_characters = ["ا", "آ", "أ", "إ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ",
                                   "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ک", "گ", "ق", "ل", "م", "ن", "و", "ه",
                                   "ی", "ئ", "ء", "ؤ", "ۀ"]

    def remove_html_tags(self, sentence):
        script_tags = re.findall('<script.*?>', sentence)
        for script_tag in script_tags:
            sentence = sentence.replace(script_tag, " ")
        script_tags = re.findall('.*</script>', sentence)
        for script_tag in script_tags:
            sentence = sentence.replace(script_tag, " ")
        a_tags = re.findall('<a.*?', sentence)
        for a_tag in a_tags:
            sentence = sentence.replace(a_tag, " ")
        a_tags = re.findall('.*</a>', sentence)
        for a_tag in a_tags:
            sentence = sentence.replace(a_tag, " ")
        img_tags = re.findall('<img.*?/>', sentence)
        for img_tag in img_tags:
            sentence = sentence.replace(img_tag, " ")
        img_tags = re.findall('.*</img>', sentence)
        for img_tag in img_tags:
            sentence = sentence.replace(img_tag, " ")
        iframe_tags = re.findall('<iframe.*?', sentence)
        for iframe_tag in iframe_tags:
            sentence = sentence.replace(iframe_tag, " ")
        iframe_tags = re.findall('.*</iframe>', sentence)
        for iframe_tag in iframe_tags:
            sentence = sentence.replace(iframe_tag, " ")
        div_tags = re.findall('<div.*?>', sentence)
        for div_tag in div_tags:
            sentence = sentence.replace(div_tag, " ")
        div_tags = re.findall('</div>', sentence)
        for div_tag in div_tags:
            sentence = sentence.replace(div_tag, " ")
        style_tags = re.findall('<style.*?>', sentence)
        for style_tag in style_tags:
            sentence = sentence.replace(style_tag, " ")
        style_tags = re.findall('.*</style>', sentence)
        for style_tag in style_tags:
            sentence = sentence.replace(style_tag, " ")
            span_tags = re.findall('<span.*?>', sentence)
            for span_tag in span_tags:
                sentence = sentence.replace(span_tag, " ")
        td_tags = re.findall('<td.*.>', sentence)
        for td_tag in td_tags:
            sentence = sentence.replace(td_tag, " ")
        tr_tags = re.findall('<tr.*?>', sentence)
        for tr_tag in tr_tags:
            sentence = sentence.replace(tr_tag, " ")
        table_tags = re.findall('<table.*?>', sentence)
        for table_tag in table_tags:
            sentence = sentence.replace(table_tag, " ")
        sentence = sentence.replace("<p>", " ")
        sentence = sentence.replace("</p>", " ")
        sentence = sentence.replace("</span>", " ")
        sentence = sentence.replace("<br>", " ")
        sentence = sentence.replace("</td>", " ")
        sentence = sentence.replace("</tr>", " ")
        sentence = sentence.replace("</tbody>", " ")
        return sentence

    def remove_english_sentence(self, sentence):
        persian_character_length = 0
        is_english = True
        if (len(sentence) == 1) and (sentence in self.punctuations):
            is_english = False
        for ch in sentence:
            if not ch in self.english and not ch in self.punctuations and not ch in self.white and not ch in self.digits:
                is_english = False
            if ch in self.persian_characters:
                persian_character_length += 1
        if persian_character_length < 3:
            is_english = True
        if sentence.strip() == "":
            is_english = True
        if is_english == True:
            sentence = "\n"
        return sentence, is_english

    def remove_article_code(self, sentence):
        article_codes = re.findall(r"کد مطلب : \d*", sentence)
        article_codes_type2 = re.findall(r"کد خبر .*.<", sentence)
        article_sources = re.findall(r"منبع: .*.", sentence)
        wikipedia_types = re.findall(r"Wikipedia contributors.*.", sentence)
        for article_code in article_codes:
            sentence = sentence.replace(article_code, " ")
        for article_code in article_codes_type2:
            sentence = sentence.replace(article_code, " ")
        for article_source in article_sources:
            sentence = sentence.replace(article_source, " ")
        for wikipedia_type in wikipedia_types:
            sentence = sentence.replace(wikipedia_type, " ")
        return sentence

    def remove_just_url(self, sentence):
        urls = extractor.find_urls(sentence)
        if urls:
            words_list = sentence.split(" ")
            persian_length = 0
            for word in words_list:
                _, isEnglish = self.remove_english_sentence(word)
                if not isEnglish:
                    persian_length += 1
            if persian_length < 4:
                sentence = "\n"
        return sentence
