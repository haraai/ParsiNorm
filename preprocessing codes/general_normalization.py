import re
from num2fawords import words
from decimal import Decimal
import copy
from itertools import groupby
from string import punctuation


class general_normalization:

    def __init__(self):
        self.persian_erab = {'ٰ': '', 'ً': '', 'ٌ': '', 'ٍ': '', 'َ': '', 'ُ': '', 'ِ': '', 'ّ': '', 'ْ': '', 'ٓ': '',
                             'ٔ': '', 'ٖ': '', 'ؕ': '', 'ٕ': '', 'ٙ': '', 'ٴ': '', '̒': '', '́': '', 'ـ': ''}

        self.persian_A = {'ﺁ': 'آ', 'ﺂ': 'آ'}

        self.persian_a = {'ﺍ': 'ا', 'ﺎ': 'ا', 'ٲ': 'أ', 'ٵ': 'أ', 'ﭐ': 'ا', 'ﭑ': 'ا', 'ﺃ': 'أ', 'ﺄ': 'أ', 'ٳ': 'إ',
                          'ﺇ': 'إ', 'ﺈ': 'إ', 'إ': 'إ', 'أ': 'أ', 'ꙇ': 'ا', 'ٱ': 'ا'}

        self.persian_b = {'ٮ': 'ب', 'ٻ': 'ب', 'ڀ': 'ب', 'ݐ': 'ب', 'ݒ': 'ب', 'ݔ': 'ب', 'ݕ': 'ب', 'ݖ': 'ب', 'ﭒ': 'ب',
                          'ﭓ': 'ب', 'ﭔ': 'ب', 'ﭕ': 'ب', 'ﺏ': 'ب', 'ﺐ': 'ب', 'ﺑ': 'ب', 'ﺒ': 'ب'}

        self.persian_p = {'ﭖ': 'پ', 'ﭗ': 'پ', 'ﭘ': 'پ', 'ﭙ': 'پ', 'ﭚ': 'پ', 'ﭛ': 'پ', 'ﭜ': 'پ', 'ﭝ': 'پ'}

        self.persian_t1 = {'ٹ': 'ت', 'ٺ': 'ت', 'ټ': 'ت', 'ٿ': 'ت', 'ݓ': 'ت', 'ﭞ': 'ت', 'ﭟ': 'ت', 'ﭠ': 'ت', 'ﭡ': 'ت',
                           'ﭦ': 'ت', 'ﭧ': 'ت', 'ﭨ': 'ت', 'ﭩ': 'ت', 'ﺕ': 'ت', 'ﺖ': 'ت', 'ﺗ': 'ت', 'ﺘ': 'ت'}

        self.persian_c1 = {'ٽ': 'ث', 'ݑ': 'ث', 'ﺙ': 'ث', 'ﺚ': 'ث', 'ﺛ': 'ث', 'ﺜ': 'ث', 'ﭢ': 'ث', 'ﭣ': 'ث', 'ﭤ': 'ث',
                           'ﭥ': 'ث'}

        self.persian_j = {'ڃ': 'ج', 'ڄ': 'ج', 'ﭲ': 'ج', 'ﭳ': 'ج', 'ﭴ': 'ج', 'ﭵ': 'ج', 'ﭶ': 'ج', 'ﭷ': 'ج', 'ﭸ': 'ج',
                          'ﭹ': 'ج', 'ﺝ': 'ج', 'ﺞ': 'ج', 'ﺟ': 'ج', 'ﺠ': 'ج'}

        self.persian_ch = {'ڇ': 'چ', 'ڿ': 'چ', 'ﭺ': 'چ', 'ﭻ': 'چ', 'ݘ': 'چ', 'ﭼ': 'چ', 'ﭽ': 'چ', 'ﭾ': 'چ', 'ﭿ': 'چ',
                           'ﮀ': 'چ', 'ﮁ': 'چ', 'ݯ': 'چ'}

        self.persian_h1 = {'ځ': 'ح', 'ڂ': 'ح', 'څ': 'ح', 'ݗ': 'ح', 'ݮ': 'ح', 'ﺡ': 'ح', 'ﺢ': 'ح', 'ﺣ': 'ح', 'ﺤ': 'ح'}

        self.persian_kh = {'ﺥ': 'خ', 'ﺦ': 'خ', 'ﺧ': 'خ', 'ﺨ': 'خ'}

        self.persian_d = {'ڈ': 'د', 'ډ': 'د', 'ڊ': 'د', 'ڋ': 'د', 'ڍ': 'د', 'ۮ': 'د', 'ݙ': 'د', 'ݚ': 'د', 'ﮂ': 'د',
                          'ﮃ': 'د', 'ﮄ': 'د', 'ﮈ': 'د', 'ﮉ': 'د', 'ﺩ': 'د', 'ﺪ': 'د'}

        self.persian_zal = {'ڌ': 'ذ', 'ﱛ': 'ذ', 'ﺫ': 'ذ', 'ﺬ': 'ذ', 'ڎ': 'ذ', 'ڏ': 'ذ', 'ڐ': 'ذ', 'ﮅ': 'ذ', 'ﮆ': 'ذ',
                            'ﮇ': 'ذ'}

        self.persian_r = {'ڑ': 'ر', 'ڒ': 'ر', 'ړ': 'ر', 'ڔ': 'ر', 'ڕ': 'ر', 'ږ': 'ر', 'ۯ': 'ر', 'ݛ': 'ر', 'ﮌ': 'ر',
                          'ﮍ': 'ر', 'ﱜ': 'ر', 'ﺭ': 'ر', 'ﺮ': 'ر'}

        self.persian_z = {'ڗ': 'ز', 'ݫ': 'ز', 'ݬ': 'ز', 'ﺯ': 'ز', 'ﺰ': 'ز'}

        self.persian_zh = {'ڙ': 'ژ', 'ﮊ': 'ژ', 'ﮋ': 'ژ'}

        self.persian_s = {'ښ': 'س', 'ڛ': 'س', 'ﺱ': 'س', 'ﺲ': 'س', 'ﺳ': 'س', 'ﺴ': 'س'}

        self.persian_sh = {'ڜ': 'ش', 'ۺ': 'ش', 'ﺵ': 'ش', 'ﺶ': 'ش', 'ﺷ': 'ش', 'ﺸ': 'ش', 'ݜ': 'ش', 'ݭ': 'ش'}

        self.persian_sad = {'ڝ': 'ص', 'ڞ': 'ص', 'ﺹ': 'ص', 'ﺺ': 'ص', 'ﺻ': 'ص', 'ﺼ': 'ص'}

        self.persian_zad = {'ۻ': 'ض', 'ﺽ': 'ض', 'ﺾ': 'ض', 'ﺿ': 'ض', 'ﻀ': 'ض'}

        self.persian_ta = {'ﻁ': 'ط', 'ﻂ': 'ط', 'ﻃ': 'ط', 'ﻄ': 'ط'}

        self.persian_za = {'ﻅ': 'ظ', 'ﻆ': 'ظ', 'ﻇ': 'ظ', 'ﻈ': 'ظ', 'ڟ': 'ظ'}

        self.persian_eyn = {'ڠ': 'ع', 'ݝ': 'ع', 'ݞ': 'ع', 'ݟ': 'ع', 'ﻉ': 'ع', 'ﻊ': 'ع', 'ﻋ': 'ع', 'ﻌ': 'ع'}

        self.persian_ghein = {'ۼ': 'غ', 'ﻍ': 'غ', 'ﻎ': 'غ', 'ﻏ': 'غ', 'ﻐ': 'غ'}

        self.persian_f = {'ڡ': 'ف', 'ڢ': 'ف', 'ڣ': 'ف', 'ڤ': 'ف', 'ڥ': 'ف', 'ڦ': 'ف', 'ݠ': 'ف', 'ݡ': 'ف', 'ﭪ': 'ف',
                          'ﭫ': 'ف', 'ﭬ': 'ف', 'ﭭ': 'ف', 'ﭮ': 'ف', 'ﭯ': 'ف', 'ﭰ': 'ف', 'ﭱ': 'ف', 'ﻑ': 'ف', 'ﻒ': 'ف',
                          'ﻓ': 'ف', 'ﻔ': 'ف', 'ᓅ': 'ف'}

        self.persian_gh = {'ٯ': 'ق', 'ڧ': 'ق', 'ڨ': 'ق', 'ﻕ': 'ق', 'ﻖ': 'ق', 'ﻗ': 'ق', 'ﻘ': 'ق'}

        self.persian_k = {'ك': 'ک', 'ػ': 'ک', 'ؼ': 'ک', 'ڪ': 'ک', 'ګ': 'ک', 'ڬ': 'ک', 'ڭ': 'ک', 'ڮ': 'ک', 'ݢ': 'ک',
                          'ݣ': 'ک', 'ݤ': 'ک', 'ﮎ': 'ک', 'ﮏ': 'ک', 'ﮐ': 'ک', 'ﮑ': 'ک', 'ﯓ': 'ک', 'ﯔ': 'ک', 'ﯕ': 'ک',
                          'ﯖ': 'ک', 'ﻙ': 'ک', 'ﻚ': 'ک', 'ﻛ': 'ک', 'ﻜ': 'ک'}

        self.persian_g = {'ڰ': 'گ', 'ڱ': 'گ', 'ڲ': 'گ', 'ڳ': 'گ', 'ڴ': 'گ', 'ﮒ': 'گ', 'ﮓ': 'گ', 'ﮔ': 'گ', 'ﮕ': 'گ',
                          'ﮖ': 'گ', 'ﮗ': 'گ', 'ﮘ': 'گ', 'ﮙ': 'گ', 'ﮚ': 'گ', 'ﮛ': 'گ', 'ﮜ': 'گ', 'ﮝ': 'گ'}

        self.persian_l = {'ڵ': 'ل', 'ڶ': 'ل', 'ڷ': 'ل', 'ڸ': 'ل', 'ݪ': 'ل', 'ﻝ': 'ل', 'ﻞ': 'ل', 'ﻟ': 'ل', 'ﻠ': 'ل'}

        self.persian_m = {'۾': 'م', 'ݥ': 'م', 'ݦ': 'م', 'ﻡ': 'م', 'ﻢ': 'م', 'ﻣ': 'م', 'ﻤ': 'م'}

        self.persian_n = {'ڹ': 'ن', 'ں': 'ن', 'ڻ': 'ن', 'ڼ': 'ن', 'ڽ': 'ن', 'ݧ': 'ن', 'ݨ': 'ن', 'ݩ': 'ن', 'ﮞ': 'ن',
                          'ﮟ': 'ن', 'ﮠ': 'ن', 'ﮡ': 'ن', 'ﮢ': 'ن', 'ﮣ': 'ن', 'ﻥ': 'ن', 'ﻦ': 'ن', 'ﻧ': 'ن', 'ﻨ': 'ن'}

        self.persian_v = {'ٶ': 'ؤ', 'ٷ': 'و', 'ﯗ': 'و', 'ﯘ': 'و', 'ﯙ': 'و', 'ﯚ': 'و', 'ﯛ': 'و', 'ﯜ': 'و', 'ﯝ': 'و',
                          'ﯞ': 'و', 'ﯟ': 'و', 'ﺅ': 'ؤ', 'ﺆ': 'و', 'ۄ': 'و', 'ۅ': 'و', 'ۆ': 'و', 'ۇ': 'و', 'ۈ': 'و',
                          'ۉ': 'و', 'ۊ': 'و', 'ۋ': 'و', 'ۏ': 'و', 'ﯠ': 'و', 'ﯡ': 'و', 'ﯢ': 'و', 'ﯣ': 'و', 'ﻭ': 'و',
                          'ﻮ': 'و', 'ؤ': 'ؤ', 'פ': 'و'}

        self.persian_h2 = {'ھ': 'ه', 'ۿ': 'ه', 'ۀ': 'ۀ', 'ہ': 'ه', 'ۂ': 'ۀ', 'ۃ': 'ه', 'ە': 'ه', 'ﮤ': 'ۀ', 'ﮥ': 'ۀ',
                           'ﮦ': 'ه', 'ﮧ': 'ه', 'ﮨ': 'ه', 'ﮩ': 'ه', 'ﮪ': 'ه', 'ﮫ': 'ه', 'ﮬ': 'ه', 'ﮭ': 'ه', 'ﺓ': 'ه',
                           'ﺔ': 'ة', 'ﻩ': 'ه', 'ﻪ': 'ه', 'ﻫ': 'ه', 'ﻬ': 'ه'}

        self.persian_y = {'ؠ': 'ی', 'ؽ': 'ی', 'ؾ': 'ی', 'ؿ': 'ی', 'ى': 'ی', 'ي': 'ی', 'ٸ': 'ئ', 'ۍ': 'ی', 'ێ': 'ی',
                          'ې': 'ی', 'ۑ': 'ی', 'ے': 'ی', 'ۓ': 'ی', 'ﮮ': 'ی', 'ﮯ': 'ی', 'ﮰ': 'ی', 'ﮱ': 'ی', 'ﯤ': 'ی',
                          'ﯥ': 'ی', 'ﯦ': 'ی', 'ﯧ': 'ی', 'ﯼ': 'ی', 'ﯽ': 'ی', 'ﯾ': 'ی', 'ﯿ': 'ی', 'ﻯ': 'ی', 'ﻰ': 'ی',
                          'ﻱ': 'ی', 'ﻲ': 'ی', 'ﻳ': 'ی', 'ﻴ': 'ی', 'ﯨ': 'ی', 'ﯩ': 'ی', 'ﯪ': 'ئ', 'ﯫ': 'ئ', 'ﯬ': 'ئ',
                          'ﯭ': 'ئ', 'ﯮ': 'ئ', 'ﯯ': 'ئ', 'ﯰ': 'ی', 'ﯱ': 'ئ', 'ﯲ': 'ئ', 'ﯳ': 'ئ', 'ﯴ': 'ئ', 'ﯵ': 'ئ',
                          'ﯶ': 'ئ', 'ﯷ': 'ئ', 'ﯸ': 'ئ', 'ﯹ': 'ئ', 'ﯺ': 'ئ', 'ﯻ': 'ئ', 'ﱝ': 'ی', 'ﺉ': 'ئ', 'ﺊ': 'ئ',
                          'ﺋ': 'ئ', 'ﺌ': 'ئ', 'ئ': 'ئ'}

        self.persian_alphabet_replaces = [
            # self.persian_erab,
            self.persian_A,
            self.persian_a,
            self.persian_b,
            self.persian_p,
            self.persian_t1,
            self.persian_c1,
            self.persian_j,
            self.persian_ch,
            self.persian_h1,
            self.persian_kh,
            self.persian_d,
            self.persian_zal,
            self.persian_r,
            self.persian_z,
            self.persian_zh,
            self.persian_s,
            self.persian_sh,
            self.persian_sad,
            self.persian_zad,
            self.persian_ta,
            self.persian_za,
            self.persian_eyn,
            self.persian_ghein,
            self.persian_f,
            self.persian_gh,
            self.persian_k,
            self.persian_g,
            self.persian_l,
            self.persian_m,
            self.persian_n,
            self.persian_v,
            self.persian_h2,
            self.persian_y
        ]

        self.english_alphabet_A = {'д': 'A', 'Ⓐ': 'A', 'ᗩ': 'A', 'Ά': 'A', 'Α': 'A', 'Ἀ': 'A', 'Ἁ': 'A', 'Ἂ': 'A',
                                   'Ἃ': 'A', 'Ἄ': 'A', 'Ἅ': 'A', 'Ἆ': 'A', 'Ἇ': 'A', 'ᾈ': 'A', 'ᾉ': 'A', 'ᾊ': 'A',
                                   'ᾋ': 'A', 'ᾌ': 'A', 'ᾍ': 'A', 'ᾎ': 'A', 'ᾏ': 'A', 'Ᾰ': 'A', 'Ᾱ': 'A', 'Ὰ': 'A',
                                   'Ά': 'A', 'ᾼ': 'A', 'А': 'A', 'Ӑ': 'A', 'Ӓ': 'A', 'À': 'A', 'Á': 'A', 'Â': 'A',
                                   'Ã': 'A', 'Ä': 'A', 'Å': 'A', 'Ā': 'A', 'Ă': 'A', 'Ą': 'A', 'Ǎ': 'A', 'Ǟ': 'A',
                                   'Ǡ': 'A', 'Å': 'A', 'Ǻ': 'A', 'Ȁ': 'A', 'Ȃ': 'A', 'Ȧ': 'A', 'Ⱥ': 'A', 'ᴀ': 'A',
                                   'Â': 'A'}

        self.english_alphabet_B = {'Β': 'B', 'В': 'B', 'в': 'B', 'Ɓ': 'B', 'Ƀ': 'B', 'ᴃ': 'B', 'ß': 'B'}

        self.english_alphabet_C = {'Ϲ': 'C', 'С': 'C', 'Ç': 'C', 'Ć': 'C', 'Ĉ': 'C', 'Ċ': 'C', 'Č': 'C', 'Ƈ': 'C',
                                   'Ȼ': 'C', 'Ç': 'C'}

        self.english_alphabet_D = {'Ð': 'D', 'Ď': 'D', 'Đ': 'D', 'Ɖ': 'D', 'Ɗ': 'D', 'ᴅ': 'D', 'ᴆ': 'D'}

        self.english_alphabet_E = {'Έ': 'E', 'Ε': 'E', 'Ἐ': 'E', 'Ἑ': 'E', 'Ἒ': 'E', 'Ἓ': 'E', 'Ἔ': 'E', 'Ἕ': 'E',
                                   'Ὲ': 'E', 'Έ': 'E', 'Ѐ': 'E', 'Ё': 'E', 'Ӗ': 'E', 'Е': 'E', 'È': 'E', 'É': 'E',
                                   'Ê': 'E', 'Ë': 'E', 'Ē': 'E', 'Ĕ': 'E', 'Ė': 'E', 'Ę': 'E', 'Ě': 'E', 'Ȅ': 'E',
                                   'Ȇ': 'E', 'Ȩ': 'E', 'Ɇ': 'E', 'ᴇ': 'E', 'ε': 'E', 'Ⓔ': 'E', 'È': 'E', 'E': 'Ê'}

        self.english_alphabet_F = {'ᖴ': 'F', 'Ϝ': 'F', '₣': 'F'}

        self.english_alphabet_G = {'Ԍ': 'G', 'Ĝ': 'G', 'Ğ': 'G', 'Ġ': 'G', 'Ģ': 'G', 'Ɠ': 'G', 'Ǧ': 'G', 'Ǵ': 'G',
                                   'ɢ': 'G', 'ʛ': 'G'}

        self.english_alphabet_H = {'ℋ': 'H', 'Ή': 'H', 'Η': 'H', 'Ἠ': 'H', 'Ἡ': 'H', 'Ἢ': 'H', 'Ἣ': 'H', 'Ἤ': 'H',
                                   'Ἥ': 'H', 'Ἦ': 'H', 'Ἧ': 'H', 'ᾘ': 'H', 'ᾙ': 'H', 'ᾚ': 'H', 'ᾛ': 'H', 'ᾜ': 'H',
                                   'ᾝ': 'H', 'ᾞ': 'H', 'ᾟ': 'H', 'Ὴ': 'H', 'Ή': 'H', 'ῌ': 'H', 'Ĥ': 'H', 'Ħ': 'H',
                                   'Ȟ': 'H', 'ʜ': 'H', 'Ⱨ': 'H', 'み': 'H', 'Н': 'H', 'н': 'H', 'Ⓗ': 'H'}

        self.english_alphabet_I = {'Ί': 'I', 'Ι': 'I', 'Ϊ': 'I', 'Ἰ': 'I', 'Ἱ': 'I', 'Ἲ': 'I', 'Ἳ': 'I', 'Ἴ': 'I',
                                   'Ἵ': 'I', 'Ἶ': 'I', 'Ἷ': 'I', 'Ῐ': 'I', 'Ῑ': 'I', 'Ὶ': 'I', 'Ί': 'I', 'Ì': 'I',
                                   'Í': 'I', 'Î': 'I', 'Ï': 'I', 'Ĩ': 'I', 'Ī': 'I', 'Ĭ': 'I', 'Į': 'I', 'İ': 'I',
                                   'Ɨ': 'I', 'Ǐ': 'I', 'Ȉ': 'I', 'Ȋ': 'I', 'ɪ': 'I', 'Ⓘ': 'I', 'Ì': 'I', 'Î': 'I'}

        self.english_alphabet_J = {'ᴊ': 'J', 'Ĵ': 'J', 'ȷ': 'J', 'Ɉ': 'J'}

        self.english_alphabet_K = {'к': 'K', 'Ǩ': 'K', 'ᴋ': 'K', 'Ⱪ': 'K', 'Ⓚ': 'K', '₭': 'K', 'Κ': 'K', 'К': 'K',
                                   'ќ': 'K', 'Ԟ': 'K', 'ԟ': 'K', 'Қ': 'K', 'қ': 'K', 'Ҝ': 'K', 'ҝ': 'K', 'Ҟ': 'K',
                                   'Ҡ': 'K', 'ҡ': 'K', 'Ķ': 'K', 'ĸ': 'K', 'Ƙ': 'K'}

        self.english_alphabet_L = {'ʟ': 'L', 'ᴌ': 'L', 'Ⱡ': 'L', 'Ɫ': 'L', 'Ĺ': 'L', 'Ļ': 'L', 'Ľ': 'L', 'Ŀ': 'L',
                                   'Ł': 'L', 'Ƚ': 'L', 'ℒ': 'L', 'Ⓛ': 'L'}

        self.english_alphabet_M = {'ᴍ': 'M', 'м': 'M', 'Ɱ': 'M', 'ℳ': 'M', 'ᗰ': 'M', '₥': 'M', 'Μ': 'M', 'Ϻ': 'M',
                                   'М': 'M', 'ʍ': 'M', 'Ⓜ': 'M'}

        self.english_alphabet_N = {'Ν': 'N', 'Ñ': 'N', 'Ń': 'N', 'Ņ': 'N', 'Ň': 'N', 'Ǹ': 'N', 'Ⓝ': 'N'}

        self.english_alphabet_O = {'ଠ': 'O', 'Ό': 'O', 'Ὀ': 'O', 'Ὁ': 'O', 'Ὂ': 'O', 'Ὃ': 'O', 'Ὄ': 'O', 'Ὅ': 'O',
                                   'Ὸ': 'O', 'Ό': 'O', 'О': 'O', 'Ò': 'O', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
                                   'Ō': 'O', 'Ŏ': 'O', 'Ő': 'O', 'Ơ': 'O', 'Ǒ': 'O', 'Ǫ': 'O', 'Ǭ': 'O', 'Ȍ': 'O',
                                   'Ȏ': 'O', 'Ȫ': 'O', 'Ȭ': 'O', 'Ȯ': 'O', 'Ȱ': 'O', 'Ⓞ': 'O'}

        self.english_alphabet_P = {'ᴘ': 'P', 'Ᵽ': 'P', 'Ρ': 'P', 'Р': 'P', 'Ҏ': 'P', 'ҏ': 'P', 'Ƥ': 'P'}

        self.english_alphabet_Q = {'Ԛ': 'Q'}

        self.english_alphabet_R = {'ᴿ': 'R', 'Ŕ': 'R', 'Ŗ': 'R', 'Ř': 'R', 'Ʀ': 'R', 'Ȑ': 'R', 'Ȓ': 'R', 'Ɍ': 'R',
                                   'ʀ': 'R', 'Ɽ': 'R', 'Я': 'R', 'Ⓡ': 'R'}

        self.english_alphabet_S = {'Ѕ': 'S', 'Ś': 'S', 'Ŝ': 'S', 'Ş': 'S', 'Š': 'S', 'Ș': 'S', 'Ȿ': 'S', 'ⓢ': 'S',
                                   'Ⓢ': 'S'}

        self.english_alphabet_T = {'т': 'T', 'Ꭲ': 'T', 'Τ': 'T', 'Т': 'T', 'Ꚑ': 'T', 'ꚑ': 'T', 'Ţ': 'T', 'Ť': 'T',
                                   'Ŧ': 'T', 'Ƭ': 'T', 'Ʈ': 'T', 'Ț': 'T', 'Ⱦ': 'T', 'ᴛ': 'T', 'Ⓣ': 'T'}

        self.english_alphabet_U = {'ᵁ': 'U', 'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U', 'Ũ': 'U', 'Ū': 'U', 'Ŭ': 'U',
                                   'Ů': 'U', 'Ű': 'U', 'Ų': 'U', 'Ư': 'U', 'Ǔ': 'U', 'Ǖ': 'U', 'Ǘ': 'U', 'Ǚ': 'U',
                                   'Ǜ': 'U', 'Ȕ': 'U', 'Ȗ': 'U', 'Ʉ': 'U', 'ᴜ': 'U', 'Ⓤ': 'U', 'ῦ': 'U'}

        self.english_alphabet_V = {'ᴠ': 'V', 'Ⓥ': 'V'}

        self.english_alphabet_W = {'ᴡ': 'W', 'Ѡ': 'W', 'Ԝ': 'W', 'Ŵ': 'W', 'Ⱳ': 'W', '￦': 'W'}

        self.english_alphabet_X = {'х': 'X', 'Χ': 'X', 'Х': 'X'}

        self.english_alphabet_Y = {'ʏ': 'Y', 'Ȳ': 'Y', 'Ɏ': 'Y', 'Ƴ': 'Y', 'Ÿ': 'Y', 'Ŷ': 'Y', '￥': 'Y', 'Ý': 'Y',
                                   'Ύ': 'Y', 'Ῠ': 'Y', 'Ὗ': 'Y', 'Ὕ': 'Y', 'Ὓ': 'Y', 'Ὑ': 'Y', 'Ϋ': 'Y', 'Υ': 'Y',
                                   'Ύ': 'Y', 'Ⓨ': 'Y'}

        self.english_alphabet_Z = {'ᴢ': 'Z', 'ꙃ': 'Z', 'ꙁ': 'Z', 'Ⱬ': 'Z', 'Ɀ': 'Z', 'Ź': 'Z', 'Ż': 'Z', 'Ž': 'Z',
                                   'Ƶ': 'Z', 'Ȥ': 'Z', 'Ꙃ': 'Z', 'Ζ': 'Z', 'Ꙁ': 'Z'}

        self.english_alphabet_a = {'ά': 'a', 'ａ': 'a', 'а': 'a', 'ⓐ': 'a', 'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a',
                                   'ä': 'a', 'å': 'a', 'ā': 'a', 'ă': 'a', 'ą': 'a', 'ǎ': 'a', 'ǟ': 'a', 'ǡ': 'a',
                                   'ǻ': 'a', 'ȁ': 'a', 'ȃ': 'a', 'ȧ': 'a', 'ⱥ': 'a', 'α': 'a', 'ɑ': 'a', '⒜': 'a',
                                   'ª': 'a'}

        self.english_alphabet_b = {'ｂ': 'b', 'Ь': 'b', 'ь': 'b', 'ƀ': 'b', 'Ƅ': 'b', 'ƅ': 'b', 'ɓ': 'b', 'ҍ': 'b',
                                   'ც': 'b', 'ⓑ': 'b', '⒝': 'b'}

        self.english_alphabet_c = {'ｃ': 'c', 'с': 'c', 'ç': 'c', 'ć': 'c', 'ĉ': 'c', 'ċ': 'c', 'č': 'c', 'ƈ': 'c',
                                   'ȼ': 'c', 'ɕ': 'c', 'ς': 'c', 'ᴄ': 'c', '⒞': 'c', '©': 'c'}

        self.english_alphabet_d = {'ｄ': 'd', 'ԁ': 'd', 'ď': 'd', 'đ': 'd', 'ȡ': 'd', 'ɖ': 'd', 'ɗ': 'd', 'ⓓ': 'd',
                                   '⒟': 'd'}

        self.english_alphabet_e = {'ｅ': 'e', 'ℯ': 'e', 'ᴱ': 'e', 'е': 'e', 'ѐ': 'e', 'ё': 'e', 'è': 'e', 'é': 'e',
                                   'ê': 'e', 'ë': 'e', 'ē': 'e', 'ĕ': 'e', 'ė': 'e', 'ę': 'e', 'ě': 'e', 'ȅ': 'e',
                                   'ȇ': 'e', 'ȩ': 'e', 'ɇ': 'e', 'ⱸ': 'e', 'ⓔ': 'e', '⒠': 'e'}

        self.english_alphabet_f = {'ᶠ': 'f', 'ƒ': 'f', 'ɟ': 'f', 'ⓕ': 'f', '⒡': 'f'}

        self.english_alphabet_g = {'ｇ': 'g', 'ĝ': 'g', 'ğ': 'g', 'ġ': 'g', 'ģ': 'g', 'ǧ': 'g', 'ǵ': 'g', 'ɠ': 'g',
                                   'ɡ': 'g', 'ყ': 'g', 'ⓖ': 'g', '⒢': 'g'}

        self.english_alphabet_h = {'ｈ': 'h', 'Ԧ': 'h', 'ԧ': 'h', 'ĥ': 'h', 'ħ': 'h', 'ȟ': 'h', 'ɦ': 'h', 'ℎ': 'h',
                                   'ℏ': 'h', 'ⱨ': 'h', 'ⓗ': 'h', '⒣': 'h'}

        self.english_alphabet_i = {'ℹ': 'i', 'ｉ': 'i', 'ΐ': 'i', 'ί': 'i', 'ι': 'i', 'ϊ': 'i', 'ἰ': 'i', 'ἱ': 'i',
                                   'ἲ': 'i', 'ἳ': 'i', 'ἴ': 'i', 'ἵ': 'i', 'ἶ': 'i', 'ἷ': 'i', 'ὶ': 'i', 'ί': 'i',
                                   'ῐ': 'i', 'ῑ': 'i', 'ῒ': 'i', 'ΐ': 'i', 'ῖ': 'i', 'ῗ': 'i', 'і': 'i', 'ї': 'i',
                                   'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i', 'ĩ': 'i', 'ī': 'i', 'ĭ': 'i', 'į': 'i',
                                   'ǐ': 'i', 'ȉ': 'i', 'ȋ': 'i', 'ɉ': 'i', 'ɨ': 'i', '¡': 'i', 'ⓘ': 'i', '⒤': 'i'}

        self.english_alphabet_j = {'ϳ': 'j', 'ј': 'j', 'ĵ': 'j', 'ǰ': 'j', 'ʝ': 'j', 'ⓙ': 'j', '⒥': 'j'}

        self.english_alphabet_k = {'ʞ': 'k', 'κ': 'k', 'ķ': 'k', 'ҟ': 'k', 'ƙ': 'k', 'ǩ': 'k', 'ⱪ': 'k', '⒦': 'k'}

        self.english_alphabet_l = {'ｌ': 'l', 'ᴸ': 'l', 'ĺ': 'l', 'ļ': 'l', 'ľ': 'l', 'ŀ': 'l', 'ł': 'l', 'ƚ': 'l',
                                   'ȴ': 'l', 'ɫ': 'l', 'ɬ': 'l', 'ɭ': 'l', 'ⱡ': 'l', 'ℓ': 'l', '⒧': 'l'}

        self.english_alphabet_m = {'ｍ': 'm', 'ⓜ': 'm', '⒨': 'm'}

        self.english_alphabet_n = {'ո': 'n', 'ｎ': 'n', 'ⁿ': 'n', 'ñ': 'n', 'ń': 'n', 'ņ': 'n', 'ň': 'n', 'ŉ': 'n',
                                   'ǹ': 'n', 'ȵ': 'n', 'η': 'n', 'ղ': 'n', 'ŋ': 'n', 'ⓝ': 'n', '⒩': 'n'}

        self.english_alphabet_o = {'ｏ': 'o', 'ℴ': 'o', 'ο': 'o', 'ό': 'o', 'ὀ': 'o', 'ὁ': 'o', 'ὂ': 'o', 'ὃ': 'o',
                                   'ὄ': 'o', 'ὅ': 'o', 'ὸ': 'o', 'ό': 'o', 'о': 'o', 'ò': 'o', 'ó': 'o', 'ô': 'o',
                                   'õ': 'o', 'ö': 'o', 'ō': 'o', 'ŏ': 'o', 'ő': 'o', 'ƍ': 'o', 'ơ': 'o', 'ǒ': 'o',
                                   'ǫ': 'o', 'ǭ': 'o', 'ȍ': 'o', 'ȏ': 'o', 'ȫ': 'o', 'ȭ': 'o', 'ȯ': 'o', 'ȱ': 'o',
                                   'ᴏ': 'o', 'օ': 'o', 'ⓞ': 'o', '⒪': 'o', 'º': 'o'}

        self.english_alphabet_p = {'ｐ': 'p', 'р': 'p', 'ƥ': 'p', 'ᴾ': 'p', 'ⓟ': 'p', '⒫': 'p'}

        self.english_alphabet_q = {'ԛ': 'q', 'ɋ': 'q', 'ⓠ': 'q', '⒬': 'q'}

        self.english_alphabet_r = {'ｒ': 'r', 'ŕ': 'r', 'ŗ': 'r', 'ř': 'r', 'ȑ': 'r', 'ȓ': 'r', 'ɾ': 'r', 'ⓡ': 'r',
                                   '®': 'r', '⒭': 'r'}

        self.english_alphabet_s = {'ｓ': 's', 'ˢ': 's', 'ś': 's', 'ŝ': 's', 'ş': 's', 'š': 's', 'ș': 's', 'ȿ': 's',
                                   '⒮': 's'}

        self.english_alphabet_t = {'ţ': 't', 'ť': 't', 'ŧ': 't', 'ƫ': 't', 'ƭ': 't', 'ț': 't', 'ȶ': 't', 'ⱦ': 't',
                                   'ⓣ': 't', '⒯': 't'}

        self.english_alphabet_u = {'ｕ': 'u', 'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u', 'ũ': 'u', 'ū': 'u', 'ŭ': 'u',
                                   'ů': 'u', 'ű': 'u', 'ų': 'u', 'ư': 'u', 'ǔ': 'u', 'ǖ': 'u', 'ǘ': 'u', 'ǚ': 'u',
                                   'ǜ': 'u', 'ȕ': 'u', 'ȗ': 'u', 'ⓤ': 'u', '⒰': 'u'}

        self.english_alphabet_v = {'∨': 'v', 'ѵ': 'v', 'ν': 'v', 'ϋ': 'v', 'ύ': 'v', 'ὐ': 'v', 'ὑ': 'v', 'ὒ': 'v',
                                   'ὓ': 'v', 'ὔ': 'v', 'ὕ': 'v', 'ὖ': 'v', 'ὗ': 'v', 'ⱱ': 'v', 'ⱴ': 'v', 'ⓥ': 'v',
                                   '⒱': 'v'}

        self.english_alphabet_w = {'ω': 'w', 'ѡ': 'w', 'ԝ': 'w', 'ŵ': 'w', 'ᵂ': 'w', 'ⱳ': 'w', 'ⓦ': 'w', '⒲': 'w',
                                   'ώ': 'w'}

        self.english_alphabet_x = {'ｘ': 'x', 'ⓧ': 'x', '⒳': 'x'}

        self.english_alphabet_y = {'У': 'y', 'у': 'y', 'ў': 'y', 'Ӯ': 'y', 'ӯ': 'y', 'Ӱ': 'y', 'ӱ': 'y', 'Ӳ': 'y',
                                   'ӳ': 'y', 'ý': 'y', 'ÿ': 'y', 'ŷ': 'y', 'ƴ': 'y', 'ȳ': 'y', 'ɏ': 'y', 'ⓨ': 'y',
                                   '⒴': 'y'}

        self.english_alphabet_z = {'ᶻ': 'z', 'ź': 'z', 'ż': 'z', 'ž': 'z', 'ƶ': 'z', 'ȥ': 'z', 'ʐ': 'z', 'ʑ': 'z',
                                   'ⱬ': 'z', 'ⓩ': 'z', '⒵': 'z'}

        self.english_alphabet_replaces = [
            self.english_alphabet_a,
            self.english_alphabet_A,
            self.english_alphabet_b,
            self.english_alphabet_B,
            self.english_alphabet_c,
            self.english_alphabet_C,
            self.english_alphabet_d,
            self.english_alphabet_D,
            self.english_alphabet_e,
            self.english_alphabet_E,
            self.english_alphabet_f,
            self.english_alphabet_F,
            self.english_alphabet_g,
            self.english_alphabet_G,
            self.english_alphabet_h,
            self.english_alphabet_H,
            self.english_alphabet_i,
            self.english_alphabet_I,
            self.english_alphabet_j,
            self.english_alphabet_J,
            self.english_alphabet_k,
            self.english_alphabet_K,
            self.english_alphabet_l,
            self.english_alphabet_L,
            self.english_alphabet_m,
            self.english_alphabet_M,
            self.english_alphabet_n,
            self.english_alphabet_N,
            self.english_alphabet_o,
            self.english_alphabet_O,
            self.english_alphabet_p,
            self.english_alphabet_P,
            self.english_alphabet_q,
            self.english_alphabet_Q,
            self.english_alphabet_r,
            self.english_alphabet_R,
            self.english_alphabet_s,
            self.english_alphabet_S,
            self.english_alphabet_t,
            self.english_alphabet_T,
            self.english_alphabet_u,
            self.english_alphabet_U,
            self.english_alphabet_v,
            self.english_alphabet_V,
            self.english_alphabet_w,
            self.english_alphabet_W,
            self.english_alphabet_x,
            self.english_alphabet_X,
            self.english_alphabet_y,
            self.english_alphabet_Y,
            self.english_alphabet_z,
            self.english_alphabet_Z,
        ]

        self.arabic_la = {'ﻵ': 'لا', 'ﻶ': 'لا', 'ﻻ': 'لا', 'ﻼ': 'لا', 'ﻷ': 'لا', 'ﻸ': 'لا', 'ﻹ': 'لا', 'ﻺ': 'لا'}
        self.arabic_sali = {'ﷰ': 'صلی', 'ﷹ': 'صلی'}
        self.arabic_gholi = {'ﷱ': 'قلی'}
        self.arabic_allah = {'ﷲ': 'الله'}
        self.arabic_akbar = {'ﷳ': 'اکبر'}
        self.arabic_mohammad = {'ﷴ': 'محمد'}
        self.arabic_rasol = {'ﷶ': 'رسول'}
        self.arabic_alayh = {'ﷷ': 'علیه'}
        self.arabic_vasalam = {'ﷸ': 'وسلم'}
        self.arabic_rial = {'﷼': 'ریال'}
        self.arabic_senat = {'\u0601': 'سنه'}
        self.arabic_salam = {'ﷵ': 'صلعم'}
        self.arabic_senat = {'ﷺ': 'صلی الله علیه و سلم'}
        self.arabic_jal = {'ﷻ': 'جل جلاله'}

        self.arabic_replaces = [
            self.arabic_la,
            self.arabic_sali,
            self.arabic_gholi,
            self.arabic_allah,
            self.arabic_akbar,
            self.arabic_mohammad,
            self.arabic_rasol,
            self.arabic_alayh,
            self.arabic_rial,
            self.arabic_senat,
            self.arabic_salam,
            self.arabic_senat,
            self.arabic_jal
        ]

        self.number_replaces_zero = {'0': '۰', '٠': '۰', '𝟢': '۰', '𝟬': '۰'}
        self.number_replaces_one = {'1': '۱', '١': '۱', '𝟣': '۱', '𝟭': '۱', '⑴': '۱', '⒈': '۱', '⓵': '۱', '①': '۱',
                                    '❶': '۱', '𝟙': '۱', '𝟷': '۱', 'ı': '۱'}

        self.number_replaces_two = {'2': '۲', '٢': '۲', '𝟤': '۲', '𝟮': '۲', '⑵': '۲', '⒉': '۲', '⓶': '۲', '②': '۲',
                                    '❷': '۲', '²': '۲', '𝟐': '۲', '𝟸': '۲', '𝟚': '۲', 'ᒿ': '۲', 'շ': '۲'}

        self.number_replaces_three = {'3': '۳', '٣': '۳', '𝟥': '۳', '𝟯': '۳', '⑶': '۳', '⒊': '۳', '⓷': '۳', '③': '۳',
                                      '❸': '۳', '³': '۳', 'ვ': '۳'}

        self.number_replaces_four = {'4': '۴', '٤': '۴', '𝟦': '۴', '𝟰': '۴', '⑷': '۴', '⒋': '۴', '⓸': '۴', '④': '۴',
                                     '❹': '۴', '⁴': '۴'}

        self.number_replaces_five = {'5': '۵', '٥': '۵', '𝟧': '۵', '𝟱': '۵', '⑸': '۵', '⒌': '۵', '⓹': '۵', '⑤': '۵',
                                     '❺': '۵', '⁵': '۵'}

        self.number_replaces_six = {'6': '۶', '٦': '۶', '𝟨': '۶', '𝟲': '۶', '⑹': '۶', '⒍': '۶', '⓺': '۶', '⑥': '۶',
                                    '❻': '۶', '⁶': '۶'}

        self.number_replaces_seven = {'7': '۷', '٧': '۷', '𝟩': '۷', '𝟳': '۷', '⑺': '۷', '⒎': '۷', '⓻': '۷', '⑦': '۷',
                                      '❼': '۷', '⁷': '۷'}

        self.number_replaces_eight = {'8': '۸', '٨': '۸', '𝟪': '۸', '𝟴': '۸', '⑻': '۸', '⒏': '۸', '⓼': '۸', '⑧': '۸',
                                      '❽': '۸', '⁸': '۸', '۸': '۸', }

        self.number_replaces_nine = {'9': '۹', '٩': '۹', '𝟫': '۹', '𝟵': '۹', '⑼': '۹', '⒐': '۹', '⓽': '۹', '⑨': '۹',
                                     '❾': '۹', '⁹': '۹'}

        self.number_replaces_ten = {'⑽': '۱۰', '⒑': '۱۰', '⓾': '۱۰', '⑩': '۱۰'}

        self.number_replaces_eleven = {'⑾': '۱۱', '⒒': '۱۱', '⑪': '۱۱'}

        self.number_replaces_twelve = {'⑿': '۱۲', '⒓': '۱۲', '⑫': '۱۲'}

        self.number_replaces_thirteen = {'⒀': '۱۳', '⒔': '۱۳', '⑬': '۱۳'}

        self.number_replaces_fourteen = {'⒁': '۱۴', '⒕': '۱۴', '⑭': '۱۴'}

        self.number_replaces_fifteen = {'⒂': '۱۵', '⒖': '۱۵', '⑮': '۱۵'}

        self.number_replaces_sixteen = {'⒃': '۱۶', '⒗': '۱۶', '⑯': '۱۶'}

        self.number_replaces_seventeen = {'⒄': '۱۷', '⒘': '۱۷', '⑰': '۱۷'}

        self.number_replaces_eighteen = {'⒅': '۱۸', '⒙': '۱۸', '⑱': '۱۸'}

        self.number_replaces_nineteen = {'⒆': '۱۹', '⒚': '۱۹', '⑲': '۱۹'}

        self.number_replaces_twenty = {'⒇': '۲۰', '⒛': '۲۰', '⑳': '۲۰'}

        self.number_replaces = [
            self.number_replaces_zero,
            self.number_replaces_one,
            self.number_replaces_two,
            self.number_replaces_three,
            self.number_replaces_four,
            self.number_replaces_five,
            self.number_replaces_six,
            self.number_replaces_seven,
            self.number_replaces_eight,
            self.number_replaces_nine,
            self.number_replaces_ten,
            self.number_replaces_eleven,
            self.number_replaces_twelve,
            self.number_replaces_thirteen,
            self.number_replaces_fourteen,
            self.number_replaces_fifteen,
            self.number_replaces_sixteen,
            self.number_replaces_seventeen,
            self.number_replaces_eighteen,
            self.number_replaces_nineteen,
            self.number_replaces_twenty
        ]

        self.punctuation_three_dot = {'…': '...'}

        self.punctuation_pipe = {'▕': '|', '❘': '|', '❙': '|', '❚': '|', '▏': '|', '│': '|'}

        self.punctuation_dash = {'ㅡ': '-', '一': '-', '—': '-', '–': '-', 'ー': '-', '̶': '-', 'ـ': '-'}

        self.punctuation_underline = {'▁': '_', '_': '_', '̲': '_'}

        self.punctuation_question = {'❔': '؟', '?': '؟', '�': '؟', '？': '؟', 'ʕ': '؟', 'ʔ': '؟', '🏻': '؟', '\x08': '؟',
                                     '\x97': '؟', '\x9d': '؟'}

        self.punctuation_Exclamation = {'❕': '!', '！': '!'}

        self.punctuation_Exclamation_Question = {'⁉': '!?'}

        self.punctuation_double_Exclamation = {'‼': '!!'}

        self.punctuation_percent = {'℅': '%', '٪': '%'}

        self.punctuation_devide = {'÷': '/'}

        self.punctuation_multiply = {'×': '*'}

        self.punctuation_double_dot = {'：': ':'}

        self.punctuation_semicolun = {'؛': ';', '；': ';'}

        self.punctuation_greater = {'›': '>'}

        self.punctuation_smaller = {'‹': '<', '＜': '<'}

        self.punctuation_double_smaller = {'《': '«'}

        self.punctuation_double_greater = {'》': '»'}

        self.punctuation_dot = {'•': '.'}

        self.punctuation_replaces = [
            self.punctuation_three_dot,
            self.punctuation_pipe,
            self.punctuation_dash,
            self.punctuation_underline,
            self.punctuation_question,
            self.punctuation_Exclamation,
            self.punctuation_Exclamation_Question,
            self.punctuation_double_Exclamation,
            self.punctuation_percent,
            self.punctuation_devide,
            self.punctuation_multiply,
            self.punctuation_double_dot,
            self.punctuation_semicolun,
            self.punctuation_greater,
            self.punctuation_smaller,
            self.punctuation_double_smaller,
            self.punctuation_double_greater,
            self.punctuation_dot,
        ]

        self.math_replaces = {
            "½": "۱/۲",
            "⅓": "۱/۳",
            "⅔": "۲/۳",
            "¼": "۱/۴",
            "¾": "۳/۴",
            "⅛": "۱/۸",
            "⅜": "۳/۸",
            "⅝": "۵/۸",
            "⅞": "۷/۸"
        }

        self.html_replaces = {
            '&nbsp;': ' ',
            '&quot;': '"',
            '&apos;': "'",
            '&lt;': '<',
            '&gt;': '>',
            '&amp;': '&',
            '&zwnj;': '',
            '&zwnj': '',
            '&ndash': '-',
            '&quot;': '"'

        }

        self.special_tel = {'℡': 'TEL'}
        self.special_AE = {'Ӕ': 'AE', 'Ǣ': 'AE', 'Ǽ': 'AE', 'ᴁ': 'AE', 'Æ': 'AE'}
        self.special_CE = {'Œ': 'CE', 'ɶ': 'CE', '₠': 'CE'}
        self.special_DZ = {'Ǳ': 'DZ', 'ǳ': 'DZ', 'Ǆ': 'DZ', 'ǆ': 'DZ'}
        self.special_NJ = {'Ǌ': 'Nj'}
        self.special_RS = {'₨': 'Rs'}
        self.special_SM = {'℠': 'SM'}
        self.special_TM = {'™': 'TM'}
        self.special_AE = {'œ': 'ae', 'æ': 'ae', 'ǽ': 'ae'}
        self.special_dz = {'ʣ': 'dz', 'ʥ': 'dz'}
        self.special_ffl = {'ﬄ': 'ffl'}
        self.special_ffi = {'ﬃ': 'ffi'}
        self.special_ff = {'ﬀ': 'ff'}
        self.special_fl = {'ﬂ': 'fl'}
        self.special_fi = {'ﬁ': 'fi'}
        self.special_ij = {'ĳ': 'ij'}
        self.special_lj = {'ǉ': 'lj'}
        self.special_lz = {'ʫ': 'lz'}
        self.special_nj = {'ǌ': 'nj'}
        self.special_st = {'ﬆ': 'st'}
        self.special_tc = {'ʨ': 'tc'}
        self.special_ts = {'ʦ': 'ts'}

        self.special_replaces = [
            self.special_tel,
            self.special_AE,
            self.special_CE,
            self.special_DZ,
            self.special_NJ,
            self.special_RS,
            self.special_SM,
            self.special_TM,
            self.special_AE,
            self.special_dz,
            self.special_ffl,
            self.special_ffi,
            self.special_ff,
            self.special_fl,
            self.special_fi,
            self.special_ij,
            self.special_lj,
            self.special_lz,
            self.special_nj,
            self.special_st,
            self.special_tc,
            self.special_ts,
        ]

        self.emoj = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u23f0"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", re.UNICODE)
        # self.characters_to_remain = "[۰-۹  A-Z a-z آ-ی \u200b \u200c \u200e \u200f \u202a \u202b \u202e \u2066 \u2067 \u206e  \s، . ()!؟:]"
        self.characters_to_remain = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹", "ا", "آ", "أ", "إ", "ب", "پ",
                                     "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",
                                     "ظ", "ع", "غ", "ف", "ک", "گ", "ق", "ل", "م", "ن", "و", "ه", "ی", "ئ", "ء", "ؤ",
                                     'ة', "ۀ", 'ٰ', 'ً', 'ٌ', 'ٍ', 'َ', 'ُ', 'ِ', 'ّ', 'ْ', 'ٓ', 'ٔ', 'ٖ', 'ؕ', 'ٕ',
                                     'ٙ', 'ٴ', '̒', '́',
                                     "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h",
                                     "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p",
                                     "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x",
                                     "X", "y", "Y", "z", "Z", "\u200b", "\u200c", "\u200e", "\u200f", "\u202a",
                                     "\u202b", "\u202e", "\u2066", "\u2067", "\u206e", "\s", "،", ".", "(", ")", "!",
                                     "؟", ":", " ", ""]

    def alphabet_correction(self, sentence):
        for persian_alphabet_replace in self.persian_alphabet_replaces:
            sentence = sentence.translate(str.maketrans(persian_alphabet_replace))
        return sentence

    def english_correction(self, sentence):
        for english_alphabet_replace in self.english_alphabet_replaces:
            sentence = sentence.translate(str.maketrans(english_alphabet_replace))
        return sentence

    def arabic_correction(self, sentence):
        for arabic_replace in self.arabic_replaces:
            sentence = sentence.translate(str.maketrans(arabic_replace))
        return sentence

    def number_correction(self, sentence):
        for number_replace in self.number_replaces:
            sentence = sentence.translate(str.maketrans(number_replace))
        return sentence

    def punctuation_correction(self, sentence):
        for punctuation_replace in self.punctuation_replaces:
            sentence = sentence.translate(str.maketrans(punctuation_replace))
        return sentence

    def math_correction(self, sentence):
        sentence = sentence.translate(str.maketrans(self.math_replaces))
        return sentence

    def html_correction(self, sentence):
        sentence = re.sub('({})'.format('|'.join(map(re.escape, self.html_replaces.keys()))),
                          lambda m: self.html_replaces[m.group()],
                          sentence)
        return sentence

    def specials_chars(self, sentence):
        for special_replace in self.special_replaces:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, special_replace.keys()))),
                              lambda m: special_replace[m.group()], sentence)
        return sentence

    def remove_emojis(self, sentence):
        return re.sub(self.emoj, '', sentence)

    def unique_floating_point(self, sentence):
        sentence = self.number_correction(sentence=sentence)
        floating_points_with_slash = re.findall('[۰-۹]+/[۰-۹]+', sentence)
        floating_points_with_comma = re.findall('[۰-۹]+,[۰-۹]+', sentence)
        floating_points_with_comma2 = re.findall('[۰-۹]+،[۰-۹]+', sentence)
        if floating_points_with_slash:
            for floating_point_with_slash in floating_points_with_slash:
                floating_point_with_slash_new = floating_point_with_slash.replace("/", ".")
                sentence = sentence.replace(str(floating_point_with_slash), floating_point_with_slash_new)
        if floating_points_with_comma:
            for floating_point_with_comma in floating_points_with_comma:
                floating_point_with_comma_new = floating_point_with_comma.replace(",", ".")
                sentence = sentence.replace(str(floating_point_with_comma), floating_point_with_comma_new)
        if floating_points_with_comma2:
            for floating_point_with_comma2 in floating_points_with_comma2:
                floating_point_with_comma_new2 = floating_point_with_comma2.replace("،", ".")
                sentence = sentence.replace(str(floating_point_with_comma2), floating_point_with_comma_new2)
        return sentence

    def remove_comma_between_numbers(self, sentence):
        sentence = self.number_correction(sentence=sentence)
        floating_points_with_comma1 = re.findall('[۰-۹]+٬[۰-۹]+', sentence)
        if floating_points_with_comma1:
            for floating_point_with_comma1 in floating_points_with_comma1:
                floating_point_with_comma_new1 = floating_point_with_comma1.replace("٬", "")
                sentence = sentence.replace(str(floating_point_with_comma1), floating_point_with_comma_new1)
        floating_points_with_comma2 = re.findall('[۰-۹]+٫[۰-۹]+', sentence)
        if floating_points_with_comma2:
            for floating_point_with_comma2 in floating_points_with_comma2:
                floating_point_with_comma_new2 = floating_point_with_comma2.replace("٫", "")
                sentence = sentence.replace(str(floating_point_with_comma2), floating_point_with_comma_new2)
        return sentence

    def space_between_punctuations_and_text(self, sentence):
        sentence = re.sub('([.,!?()])', r' \1 ', sentence)
        sentence = re.sub('\s{2,}', ' ', sentence)
        return sentence

    def remove_repeated_punctuation(self, sentence):
        punc = set(punctuation) - set('.')
        punc.add("؟")
        punc.add("،")
        newtext = []
        for k, g in groupby(sentence):
            if k in punc:
                newtext.append(k)
            else:
                newtext.extend(g)
        return ''.join(newtext)

    def remove_not_desired_chars(self, sentence):
        # print(self.characters_to_remain)
        for character in sentence:
            if character not in self.characters_to_remain:
                sentence = sentence.replace(character, " ")
        return sentence
        return ''.join(re.findall(self.characters_to_remain, sentence))
