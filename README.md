<div dir='ltr' align='left'>

# pre-processing


<h1>Use total functions in predifiened order:</h1>

The file clean.py has all functions in order.
To use this function you have to make an instance from clean and then call clean_sentence method:
	
	from clean import clean
	sentence = clean.clean_sentence(sentence)

If you want to seperate sentences you have to make an instance of tokenizer class and then call sentence_tokenize function

	from Tokenizer import Tokenizer
	sentences = tokenizer.sentence_tokenize(sentences)
All in one, you can use following codes to have a preprocessing for speech processing:

	for index in range(len(sentences)):
        	for sentence in tokenizer.sentence_tokenize(sentences[index]):
                sentence = clean.clean_sentence(sentence)
		# Do every thing you want with each seprated sentence
	
<h1>Use Functions seperately:</h1>
Detect and clean URLs and emails this cleaning is by replacing symbols to how they are spelled:


	from mail_url_cleaner import mail_url_cleaner
	mail_url_cleaner = mail_url_cleaner()
	sentence = mail_url_cleaner.find_mails_clean(sentence=sentence)
	sentence = mail_url_cleaner.find_urls_clean(sentence=sentence)

Detect and covert time and dates to how they are spelled


	from date_time_to_text import date_time_to_text
	date_time_to_text = date_time_to_text()
	sentence = date_time_to_text.date_to_text(sentence=sentence)
	sentence = date_time_to_text.time_to_text(sentence=sentence)


Replace different forms of Persian and English to unique forms 

	from general_normalization import general_normalization
	general_normalization = general_normalization()
	sentence = general_normalization.alphabet_correction(sentence=sentence)
	sentence = general_normalization.english_correction(sentence=sentence)

General text normalization is used by following codes

	from general_normalization import general_normalization
	general_normalization = general_normalization()
	# To replace HTML tags with their character symbols
	sentence = general_normalization.html_correction(sentence=sentence)
	# To replace arabic symbols with how they are written completely
	sentence = general_normalization.arabic_correction(sentence=sentence)
	# To have a unique form of each puncuations
	sentence = general_normalization.punctuation_correction(sentence=sentence)
	# To replace special English symbols and characters to how they are written completely
	sentence = general_normalization.specials_chars(sentence=sentence)
	# Remove emojis
	sentence = general_normalization.remove_emojis(sentence=sentence)
	# Unique floating point with these seperators: (/,،)
	sentence = general_normalization.unique_floating_point(sentence=sentence)
	# Remove comma between numbers that are used to read numbers easily
	sentence = general_normalization.remove_comma_between_numbers(sentence=sentence)
	# Convert numbers to a unique Persian unicode
	sentence = general_normalization.number_correction(sentence=sentence)
	# Remove characters and symbols that are not in list of acceptable characters
	sentence = general_normalization.remove_not_desired_chars(sentence=sentence)
	# Remove punctuations that are repeated except for dot(.)
	sentence = general_normalization.remove_repeated_punctuation(sentence=sentence)

Detect and replace telephone numbers with how they are pronounced

	from telephone_number import telephone_number
	telephone_number = telephone_number()
	sentence = telephone_number.find_phones_replace(sentence=sentence)

Detect and Replace English and Persian abbrevation with how they are read

	from abbreviation import abbreviation
	abbreviation = abbreviation()
	sentence = abbreviation.replace_date_abbreviation(sentence=sentence)
	sentence = abbreviation.replace_persian_label_abbreviation(sentence=sentence)
	sentence = abbreviation.replace_law_abbreviation(sentence=sentence)
	sentence = abbreviation.replace_book_abbreviation(sentence=sentence)
	sentence = abbreviation.replace_other_abbreviation(sentence=sentence)
	sentence = abbreviation.replace_English_abbrevations(sentence=sentence)

Speech processing normalization. This class replace non standard characters and symbols to how they are spelled
	
	from TTS_normalization import TTS_normalization
	TTS_normalization = TTS_normalization()
	sentence = TTS_normalization.math_correction(sentence=sentence)
	sentence = TTS_normalization.replace_currency(sentence=sentence)

Replace numbers and special numbers such as floating points, national code, card number, sheba to how they are read 

	from special_numbers import special_numbers
	special_numbers = special_numbers()
	sentence = special_numbers.convert_numbers_to_text(sentence=sentence)
	sentence = special_numbers.replace_national_code(sentence=sentence)
	sentence = special_numbers.replace_card_number(sentence=sentence)
	sentence = special_numbers.replace_shaba(sentence=sentence)

Remove unnecessary sentences

	from data_cleaning import data_cleaning
	data_cleaning = data_cleaning()
	sentence = data_cleaning.remove_just_url(sentence=sentence)
	sentence, isEnglish = data_cleaning.remove_english_sentence(sentence=sentence)
	sentence = data_cleaning.remove_html_tags(sentence=sentence)
	sentence = self.data_cleaning.remove_article_code(sentence=sentence)


<h1>Examples</h1>

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

<h1>To Do:</h1>
<ul>
  <li>Slash "/" in different contexts </li>
  <li>"+" in different contexts </li>
</ul>  

</div>
