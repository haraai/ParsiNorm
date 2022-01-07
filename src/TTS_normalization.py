import re


class TTS_normalization:
    def __init__(self):
        self.math_replaces = {
            '½': 'یک دوم',
            '⅓': 'یک سوم',
            '⅔': 'دو سوم',
            '¼': 'یک چهارم',
            '¾': 'سه چهارم',
            '⅛': 'یک هشتم',
            '⅜': 'سه هشتم',
            '⅝': 'پنج هشتم',
            '⅞': 'هفت هشتم'
        }

        self.dollar = {'$': ' دلار '}
        self.euro = {'€': ' یورو '}
        self.pond = {'£': ' پوند '}
        self.yoan = {'¥': ' یوان '}
        self.lir = {'₺': ' لیر '}
        self.canada = {'C$': ' دلار کانادا '}
        self.kron = {'Kč': ' کرون چک '}
        self.zeoti = {'zł': ' زلوتی لهستان '}
        self.robl = {'₽': ' روبل روسیه '}
        self.menat = {'₼': ' منات آذربایجان '}
        self.deram = {'դր': ' درام ارمنستان '}
        self.taga = {'৳': ' تاکا ینگلادش '}
        self.lari = {'ლ': ' لاری گرجستان '}
        self.ropie = {'₹': ' روپیه قزاقستان '}
        self.kip = {'₭': ' کیپ لائوس '}
        self.tange = {'лв': ' تنگه هند '}
        self.togric = {'₮': ' توگریک مغولی '}
        self.von = {'₩': ' وون کره شمالی '}
        self.pezo = {'₱': ' پزو فیلیپین '}
        self.bot = {'฿': ' بات تایلند '}
        self.dong = {'₫': ' دانگ ویتنام '}
        self.nakfa = {'ናቕፋ': ' ناکفای اریتره '}
        self.beer = {'ብር': ' بیر اتیوپی '}
        self.sadi = {'GH₵': ' سدی غنا '}
        self.naira = {'₦': ' نایرا نیجریه '}
        self.dinar = {'ден': ' دینار مقدونیه '}

        self.currency_replaces = [
            self.dollar,
            self.euro,
            self.pond,
            self.yoan,
            self.lir,
            self.canada,
            self.kron,
            self.zeoti,
            self.robl,
            self.menat,
            self.deram,
            self.taga,
            self.lari,
            self.ropie,
            self.kip,
            self.tange,
            self.togric,
            self.von,
            self.pezo,
            self.bot,
            self.dong,
            self.nakfa,
            self.beer,
            self.sadi,
            self.naira,
            self.dinar,
        ]
        self.percent = {'%': ' درصد '}
        self.degree = {'°': ' درجه '}
        self.star = {'*': ' ستاره '}
        self.square = {'#': ' مربع '}
        self.add = {'+': ' پلاس '}
        self.And = {'&': ' اند '}
        self.delta = {'Δ': ' دلتا '}

        self.symbols = [
            self.percent,
            self.degree,
            self.star,
            self.square,
            self.add,
            self.delta,
            self.And,
        ]

    def math_correction(self, sentence):
        sentence = sentence.translate(str.maketrans(self.math_replaces))
        return sentence

    def replace_currency(self, sentence):
        for currency_replace in self.currency_replaces:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, currency_replace.keys()))),
                              lambda m: currency_replace[m.group()], sentence)
        return sentence

    def replace_symbols(self, sentence):
        for symbol in self.symbols:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, symbol.keys()))),
                              lambda m: symbol[m.group()], sentence)
        return sentence