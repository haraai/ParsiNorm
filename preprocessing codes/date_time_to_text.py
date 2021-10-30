import re
import random
from num2fawords import words, HUNDREDS, ordinal_words
from persian_tools import digits


class date_time_to_text:

    def __init__(self):
        self.english_digits = '0123456789'
        self.persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        self.shamsi_month = {
            "1": "فروردین",
            "2": "اردیبهشت",
            "3": "خرداد",
            "4": "تیر",
            "5": "مرداد",
            "6": "شهریور",
            "7": "مهر",
            "8": "آبان",
            "9": "آذر",
            "10": "دی",
            "11": "بهمن",
            "12": "اسفند",
        }
        self.miladi_month = {
            "1": "ژانویه",
            "2": "فوریه",
            "3": "مارس",
            "4": "آوریل",
            "5": "می",
            "6": "ژوئن",
            "7": "جولای",
            "8": "اوت",
            "9": "سپتامبر",
            "10": "اکتبر",
            "11": "نوامبر",
            "12": "دسامبر",
        }
        self.ghamari_month = {
            "1": "محرم",
            "2": "صفر",
            "3": "ربیع الاول",
            "4": "ربیع الثانی",
            "5": "جمادی الاول",
            "6": "جمادی الثانی",
            "7": "رجب",
            "8": "شعبان",
            "9": "رمضان",
            "10": "شوال",
            "11": "ذیقعده",
            "12": "ذیحجه",
        }

        self.number_replaces = {
            "۰": ['0', '٠', '𝟢', '𝟬'],
            "۱": ['1', '١', '𝟣', '𝟭', '⑴', '⒈', '⓵', '①', '❶', '𝟙', '𝟷', 'ı', '¹'],
            "۲": ['2', '٢', '𝟤', '𝟮', '⑵', '⒉', '⓶', '②', '❷', '²', '𝟐', '𝟸', '𝟚', 'ᒿ', 'շ'],
            "۳": ['3', '٣', '𝟥', '𝟯', '⑶', '⒊', '⓷', '③', '❸', '³', 'ვ'],
            "۴": ['4', '٤', '𝟦', '𝟰', '⑷', '⒋', '⓸', '④', '❹', '⁴'],
            "۵": ['5', '٥', '𝟧', '𝟱', '⑸', '⒌', '⓹', '⑤', '❺', '⁵'],
            "۶": ['6', '٦', '𝟨', '𝟲', '⑹', '⒍', '⓺', '⑥', '❻', '⁶'],
            "۷": ['7', '٧', '𝟩', '𝟳', '⑺', '⒎', '⓻', '⑦', '❼', '⁷'],
            "۸": ['8', '٨', '𝟪', '𝟴', '⑻', '⒏', '⓼', '⑧', '❽', '⁸'],
            "۹": ['9', '٩', '𝟫', '𝟵', '⑼', '⒐', '⓽', '⑨', '❾', '⁹'],
            "۱۰": ['⑽', '⒑', '⓾', '⑩'],
            "۱۱": ['⑾', '⒒', '⑪'],
            "۱۲": ['⑿', '⒓', '⑫'],
            "۱۳": ['⒀', '⒔', '⑬'],
            "۱۴": ['⒁', '⒕', '⑭'],
            "۱۵": ['⒂', '⒖', '⑮'],
            "۱۶": ['⒃', '⒗', '⑯'],
            "۱۷": ['⒄', '⒘', '⑰'],
            "۱۸": ['⒅', '⒙', '⑱'],
            "۱۹": ['⒆', '⒚', '⑲'],
            "۲۰": ['⒇', '⒛', '⑳'],
        }

    def number_correction(self, word):
        for correct_form, wrong_forms in self.number_replaces.items():
            for wrong_character in wrong_forms:
                word = word.replace(wrong_character, correct_form)
        return word

    def select_templates_time_three(self, hour, minute, second):
        time_tempaltes = {
            0: f"{words(hour)} و {words(minute)} دقیقه و  {words(second)} ثانیه",
        }
        time_tempaltes_no_minute = {
            0: f"{words(hour)} و {words(second)} ثانیه",
        }
        time_tempaltes_no_second = {
            0: f"{words(hour)} و {words(minute)} دقیقه",
            1: f"{words(hour)} و {words(minute)}",
        }
        time_tempaltes_no_second_no_minute = {
            0: f"{words(hour)}",
        }
        bamdad_tempaltes = {
            0: f"{words(minute)} دقیقه و  {words(second)} ثانیه بامداد",
        }
        bamdad_tempaltes_no_minute = {
            0: f"{words(second)} ثانیه بامداد",
        }
        bamdad_tempaltes_no_second = {
            0: f"{words(minute)} دقیقه بامداد",
        }
        if hour != 0 and minute != 0 and second != 0:
            return time_tempaltes.get(0)
        if hour != 0 and minute == 0 and second != 0:
            return time_tempaltes_no_minute.get(0)
        if hour != 0 and minute != 0 and second == 0:
            template_no = random.randint(0, 1)
            return time_tempaltes_no_second.get(template_no)
        if hour != 0 and minute == 0 and second == 0:
            return time_tempaltes_no_second_no_minute.get(0)
        if hour == 0 and minute != 0 and second != 0:
            return bamdad_tempaltes.get(0)
        if hour == 0 and minute == 0 and second != 0:
            return bamdad_tempaltes_no_minute.get(0)
        if hour == 0 and minute != 0 and second == 0:
            return bamdad_tempaltes_no_second.get(0)
        if hour == 0 and minute == 0 and second == 0:
            return "بامداد"

    def select_templates_time_two(self, hour, minute):
        time_tempaltes = {
            0: f"{words(hour)} و {words(minute)} دقیقه  ",
            1: f"{words(hour)} و {words(minute)} ",
        }
        time_tempaltes_no_minute = {
            0: f"{words(hour)}",
        }
        bamdad_tempaltes = {
            0: f"{words(minute)} دقیقه  بامداد",
        }
        if hour != 0 and minute != 0:
            template_no = random.randint(0, 1)
            return time_tempaltes.get(template_no)
        if hour != 0 and minute == 0:
            return time_tempaltes_no_minute.get(0)
        if hour == 0 and minute != 0:
            return bamdad_tempaltes.get(0)
        if hour == 0 and minute == 0:
            return "بامداد"

    def time_to_text(self, sentence):
        matches = re.findall(r'(\d+:\d+:\d+)', sentence)
        for match in matches:
            hour = int(match.split(':')[0])
            minute = int(match.split(':')[1])
            second = int(match.split(':')[2])
            if hour <= 23 and minute <= 59 and second <= 59:
                sentence = sentence.replace(match, self.select_templates_time_three(hour, minute, second))
        matches = re.findall(r'(\d+:\d+)', sentence)
        for match in matches:
            hour = int(match.split(':')[0])
            minute = int(match.split(':')[1])
            if hour <= 23 and minute <= 59:
                sentence = sentence.replace(match, self.select_templates_time_two(hour, minute))

        return sentence

    def ConvertNumberToLetter(self, line):
        newline = ''
        number = ''
        counter = 0
        for char in line:
            if (char in self.english_digits) or (char in self.persian_digits):
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

    def define_date_type(self, year):
        if len(year) == 2:
            return "Shamsi"
        elif int(year) > 1400 and int(year) < 1500:
            return "Ghamari"
        elif int(year) > 1500:
            return "Miladi"
        else:
            return "Shamsi"

    def select_templates_date(self, month_name, year, month, day):
        template_no = random.randint(0, 9)
        switcher = {
            0: f"{ordinal_words(day)} {month_name[month]} سال {self.ConvertNumberToLetter(year)}",
            1: f"{ordinal_words(day)} {self.ConvertNumberToLetter(month)} سال {self.ConvertNumberToLetter(year)}",
            2: f"{self.ConvertNumberToLetter(day)} {month_name[month]} سال {self.ConvertNumberToLetter(year)}",
            3: f"{self.ConvertNumberToLetter(day)} {month_name[month]} ماه سال {self.ConvertNumberToLetter(year)}",
            4: f"{ordinal_words(day)}  {month_name[month]} ماه {self.ConvertNumberToLetter(year)}",
            5: f"{self.ConvertNumberToLetter(day)}  {month_name[month]} ماه {self.ConvertNumberToLetter(year)}",
            6: f"{ordinal_words(day)} {month_name[month]} {self.ConvertNumberToLetter(year)}",
            7: f"{ordinal_words(day)} {self.ConvertNumberToLetter(month)} {self.ConvertNumberToLetter(year)}",
            8: f"{self.ConvertNumberToLetter(day)} {month_name[month]} {self.ConvertNumberToLetter(year)}",
            9: f"{self.ConvertNumberToLetter(day)} {self.ConvertNumberToLetter(month)} {self.ConvertNumberToLetter(year)}",
        }
        return switcher.get(template_no)

    def define_template_type(self, date_type, year, month, day):
        if date_type == "Shamsi":
            return self.select_templates_date(self.shamsi_month, year, month, day)
        elif date_type == "Ghamari":
            return self.select_templates_date(self.ghamari_month, year, month, day)
        elif date_type == "Miladi":
            return self.select_templates_date(self.miladi_month, year, month, day)

    def date_to_text(self, sentence):
        match = None
        sentence = digits.convert_to_en(sentence)
        match_main = re.search(r'(\d+\/\d+\/\d+)', sentence)
        match1 = re.search(r'(\d+\s/\s\d+\s/\s\d+)', sentence)
        match1_1 = re.search(r'(\d+\s/\d+/\d+)', sentence)
        match1_2 = re.search(r'(\d+/\d+/\s\d+)', sentence)
        match1_3 = re.search(r'(\d+/\s\d+/\s\d+)', sentence)
        match2 = re.search(r'(\d+/\s\d+/\s\d+)', sentence)
        match3 = re.search(r'(\d+\.\d+\.\d+)', sentence)
        match4 = re.search(r'(\d+-\d+-\d+)', sentence)
        if match_main:
            match_form = match_main.group()
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match_main.group()
        if match1:
            match_form = match1.group()
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match1.group()
        elif match2:
            sentence = sentence.replace(match2.group(), match2.group().replace("-", "/"))
            match_form = match2.group().replace("-", "/")
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match2.group().replace("-", "/")
        elif match3:
            sentence = sentence.replace(match3.group(), match3.group().replace(".", "/"))
            match_form = match3.group().replace(".", "/")
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match3.group().replace(".", "/")
        elif match4:
            sentence = sentence.replace(match4.group(), match4.group().replace("-", "/"))
            match_form = match4.group().replace("-", "/")
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match4.group().replace("-", "/")
        elif match1_1:
            match_form = match1_1.group()
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match1_1.group()
        elif match1_2:
            match_form = match1_2.group()
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match1_2.group()
        elif match1_3:
            match_form = match1_3.group()
            splited_date = match_form.split("/")
            part1 = int(splited_date[0])
            part2 = int(splited_date[1])
            part3 = int(splited_date[2])
            if part1 < 1 or part2 < 1 or part3 < 1:
                match = None
            else:
                match = match1_3.group()
        if match:
            splited_date = match.split("/")
            splited_date_len = [len(part) for part in splited_date]
            if 4 == splited_date_len[0] and int(splited_date[1]) <= 12:
                # year4d/month/day
                year = splited_date[0]
                month = str(int(splited_date[1]))
                day = splited_date[2]
                date_type = self.define_date_type(year)
                sentence = sentence.replace(match, self.define_template_type(date_type, year, month, day))
            elif int(splited_date[1]) >= 7 and int(splited_date[1]) <= 12 and int(splited_date[0]) > 31:
                # year2d/month/day
                year = splited_date[0]
                month = str(int(splited_date[1]))
                day = splited_date[2]
                date_type = self.define_date_type(year)
                sentence = sentence.replace(match, self.define_template_type(date_type, year, month, day))
            elif int(splited_date[1]) <= 6 and int(splited_date[1]) <= 12 and int(splited_date[0]) >= 31:
                # year2d/month/day
                year = splited_date[0]
                month = str(int(splited_date[1]))
                day = str(int(splited_date[2]))
                date_type = self.define_date_type(year)
                sentence = sentence.replace(match, self.define_template_type(date_type, year, month, day))
            elif int(splited_date[1]) >= 7 and int(splited_date[1]) <= 12 and int(splited_date[2]) > 31:
                # day/month/year2d
                year = splited_date[2]
                month = str(int(splited_date[1]))
                day = str(int(splited_date[0]))
                date_type = self.define_date_type(year)
                sentence = sentence.replace(match, self.define_template_type(date_type, year, month, day))
            elif int(splited_date[1]) <= 6 and int(splited_date[1]) <= 6 and int(splited_date[1]) <= 12 and int(
                    splited_date[2]) > 31:
                # day/month/year2d
                year = splited_date[2]
                month = str(int(splited_date[1]))
                day = str(int(splited_date[0]))
                date_type = self.define_date_type(year)
                sentence = sentence.replace(match, self.define_template_type(date_type, year, month, day))
            elif 4 == splited_date_len[2] and int(splited_date[1]) <= 12:
                # day/month/year4d
                year = splited_date[2]
                month = str(int(splited_date[1]))
                day = splited_date[0]
                date_type = self.define_date_type(year)
                sentence = sentence.replace(match, self.define_template_type(date_type, year, month, day))

        return self.number_correction(sentence)
