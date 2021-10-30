from general_normalization import general_normalization
from TTS_normalization import TTS_normalization
from date_time_to_text import date_time_to_text
from mail_url_cleaner import mail_url_cleaner
from abbreviation import abbreviation
from telephone_number import telephone_number
from Tokenizer import Tokenizer
from special_numbers import special_numbers
from data_cleaning import data_cleaning
from hazm import *
import re


class clean:
    def __init__(self):
        self.mail_url_cleaner = mail_url_cleaner()
        self.general_normalization = general_normalization()
        self.date_time_to_text = date_time_to_text()
        self.TTS_normalization = TTS_normalization()
        self.abbreviation = abbreviation()
        self.telephone_number = telephone_number()
        self.tokenizer = Tokenizer()
        self.normalizer = Normalizer()
        self.special_numbers = special_numbers()
        self.data_cleaning = data_cleaning()

    def clean_sentence(self, sentence):
        sentence = self.data_cleaning.remove_just_url(sentence=sentence)
        sentence = self.mail_url_cleaner.find_mails_clean(sentence=sentence)
        sentence = self.mail_url_cleaner.find_urls_clean(sentence=sentence)
        sentence, _ = self.data_cleaning.remove_english_sentence(sentence=sentence)
        sentence = self.data_cleaning.remove_html_tags(sentence=sentence)
        sentence = self.date_time_to_text.date_to_text(sentence=sentence)
        sentence = self.date_time_to_text.time_to_text(sentence=sentence)
        sentence = self.mail_url_cleaner.remove_meaning_less_url(sentence=sentence)
        sentence = self.data_cleaning.remove_article_code(sentence=sentence)
        sentence = self.general_normalization.alphabet_correction(sentence=sentence)
        sentence = self.general_normalization.english_correction(sentence=sentence)
        sentence = self.general_normalization.html_correction(sentence=sentence)
        sentence = self.general_normalization.arabic_correction(sentence=sentence)
        sentence = self.general_normalization.punctuation_correction(sentence=sentence)
        sentence = self.general_normalization.specials_chars(sentence=sentence)
        sentence = self.general_normalization.remove_emojis(sentence=sentence)
        sentence = self.general_normalization.unique_floating_point(sentence=sentence)
        sentence = self.general_normalization.remove_comma_between_numbers(sentence=sentence)
        sentence = self.general_normalization.number_correction(sentence=sentence)
        sentence = self.general_normalization.remove_not_desired_chars(sentence=sentence)
        sentence, _ = self.data_cleaning.remove_english_sentence(sentence=sentence)
        sentence = self.special_numbers.convert_numbers_to_text(sentence=sentence)
        sentence = self.telephone_number.find_phones_replace(sentence=sentence)
        sentence = self.abbreviation.replace_date_abbreviation(sentence=sentence)
        sentence = self.abbreviation.replace_persian_label_abbreviation(sentence=sentence)
        sentence = self.abbreviation.replace_law_abbreviation(sentence=sentence)
        sentence = self.abbreviation.replace_book_abbreviation(sentence=sentence)
        sentence = self.abbreviation.replace_other_abbreviation(sentence=sentence)
        sentence = self.abbreviation.replace_English_abbrevations(sentence=sentence)
        sentence = self.tokenizer.replace_other(sentence=sentence)
        sentence = self.TTS_normalization.math_correction(sentence=sentence)
        sentence = self.TTS_normalization.replace_currency(sentence=sentence)
        sentence = self.special_numbers.replace_national_code(sentence=sentence)
        sentence = self.special_numbers.replace_card_number(sentence=sentence)
        sentence = self.special_numbers.replace_shaba(sentence=sentence)
        # sentence = self.general_normalization.space_between_punctuations_and_text(sentence=sentence)
        sentence = self.general_normalization.remove_repeated_punctuation(sentence=sentence)
        sentence = self.normalizer.affix_spacing(sentence)
        sentence = " ".join(sentence.split())
        return sentence
