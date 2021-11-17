<div dir='ltr' align='left'>

# PerSpeechNormalization
The normalization step is so essential to format unification in pure textual applications. However, for embedded language models in speech processing modules, normalization is not limited to format unification. Moreover, it has to convert each readable symbol, number, etc., to how they are pronounced. 

<h1>functionalities</h1>

<h3> General Normalization</h3>

+ Sentence tokenizer
+ Normalizing persian and English characters 
+ Normalizing Numbers (Converting to unique perisan Number)
+ Converting Persian, English, Arabic symbols to normalized characters
+ Normalize Punctuations
+ Removing emojis
+ Converting HTML tags to characters and symbols
+ Having unique floating point number
+ Removing different comma between numbers
+ Removing repeated punctuations

<h3> Speech Normalization</h3>

+ Converting mail and url to how are pronounced
+ Converting Date and Times to how they are pronounced
+ Converting special numbers to how they are pronounced
+ Converting English and Persian Abbrevations to how they are pronounced
+ converting telephone numbers to how they are pronounced in Persian
+ Converting currency to how they are read
+ Converting some symbols to how they are read such as %, °, *, #, +, &, Δ

<h1>Usage</h1>

```python
>>> from mail_url_cleaner import mail_url_cleaner
>>> mail_url_cleaner = mail_url_cleaner()
>>> mail_url_cleaner.find_mails_clean(sentence="info@hara.ai")
info at hara dot ai

>>> mail_url_cleaner.find_urls_clean(sentence="https://hara.ai/#services")
https do noghte slash slash hara dot ai

>>> from date_time_to_text import date_time_to_text
>>> date_time_to_text = date_time_to_text()
>>> date_time_to_text.date_to_text(sentence='2021/10/27')
بیست و هفتم اکتبر سال دو هزار و بیست و یک

>>> date_time_to_text.time_to_text(sentence='22:57:11')
بیست و دو و پنجاه و هفت دقیقه و  یازده ثانیه

>>> from general_normalization import general_normalization
>>> general_normalization = general_normalization()
>>> general_normalization.alphabet_correction(sentence='ﻙﯘݙݤﮮ')
کودکی

>>> general_normalization.english_correction(sentence='naïve')
naive

>>> general_normalization.html_correction(sentence='&quot;')
"

>>> general_normalization.arabic_correction(sentence='ﷺ')
صلی الله علیه و سلم

>>> general_normalization.punctuation_correction(sentence="…")
...

>>> general_normalization.specials_chars(sentence="℡")
TEL

>>> general_normalization.remove_emojis(sentence='😊')


>>> general_normalization.unique_floating_point(sentence='1،2')
۱.۲

>>> general_normalization.remove_comma_between_numbers(sentence='1٬234')
۱۲۳۴

>>> general_normalization.number_correction(sentence="⑤")
۵

>>> general_normalization.remove_not_desired_chars(sentence="^ Hi ~")
  Hi  

>>> general_normalization.remove_repeated_punctuation(sentence="!!!!!")
!

>>> from telephone_number import telephone_number
>>> telephone_number = telephone_number()
>>> telephone_number.find_phones_replace(sentence='تلفن ۰۲۱۳۳۴۵۶۷۸۸')
تلفن   صفر  بیست و یک سی و سه چهل و پنج شصت و هفت هشتاد و هشت

>>> from abbreviation import abbreviation
>>> abbreviation = abbreviation()
>>> abbreviation.replace_date_abbreviation(sentence=".در سال 1400 ه.ش")
در سال 1400 هجری شمسی

>>> abbreviation.replace_persian_label_abbreviation(sentence='امام زمان (عج)')
امام زمان  عجل الله تعالی فرجه الشریف 

>>> abbreviation.replace_law_abbreviation(sentence='در ق.ا آمده است')
در قانون اساسی آمده است

>>> abbreviation.replace_book_abbreviation(sentence='به کتاب زیر ر.ک مراجعه کنید')
به کتاب زیر رجوع کنید مراجعه کنید

>>> abbreviation.replace_other_abbreviation(sentence='در قانون ج.ا آمده است')
در قانون جمهوری اسلامی آمده است

>>> abbreviation.replace_English_abbrevations(sentence='U.S.A')
یو اس آ

>>> from TTS_normalization import TTS_normalization
>>> TTS_normalization = TTS_normalization()
>>> TTS_normalization.math_correction(sentence='⅞')
هفت هشتم

>>> TTS_normalization.replace_currency(sentence='۳۳$')
۳۳ دلار

>>> TTS_normalization.replace_symbols(sentence='۳۳°')
۳۳ درجه 

>>> from special_numbers import special_numbers
>>> special_numbers = special_numbers()
>>> special_numbers.convert_numbers_to_text(sentence='122')
 صد و بیست و دو

>>> special_numbers.replace_national_code(sentence='0499370899')
صفر  چهار   نهصد و نود و سه   هفتاد   هشتصد و نود و نه

>>> special_numbers.replace_card_number(sentence='6037701689095443')
شصت   سی و هفت   هفتاد   شانزده   هشتاد و نه   صفر  نه   پنجاه و چهار   چهل و سه

>>>special_numbers.replace_shaba(sentence='IR820540102680020817909002')
 آی آر   هشتاد و دو   صفر  پنج   چهل   ده   بیست و شش   هشتاد   صفر  دو   صفر  هشت   هفده   نود   نود   صفر  دو 

>>> from Tokenizer import Tokenizer
>>> tokenizer = Tokenizer()
>>> tokenizer.sentence_tokenize('.این در مورد پروژه است. باید جداسازی انجام گیرد. درست است') 
['این در مورد پروژه است .', ' باید جداسازی انجام گیرد .', ' درست است .']

```


<h1> Reference </h1>

If you use or discuss this normalization tool in your work, please cite our paper :

```
@article{oji2021perspeechnorm,
  title={PerSpeechNorm: A Persian Toolkit for Speech Processing Normalization},
  author={Oji, Romina and Razavi, Seyedeh Fatemeh and Dehsorkh, Sajjad Abdi and Hariri, Alireza and Asheri, Hadi and Hosseini, Reshad},
  journal={arXiv preprint arXiv:2111.03470},
  year={2021}
}
```

<h1> Contact </h1>

If you have any technical question regarding the dataset or publication, please
create an issue in this repository.


</div>
