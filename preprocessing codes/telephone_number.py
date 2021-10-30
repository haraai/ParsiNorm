import re
import random
from num2fawords import words, HUNDREDS, ordinal_words
from general_normalization import general_normalization


class telephone_number:
    def __init__(self):
        self.general_normalization = general_normalization()


    def find_phones_replace(self, sentence):
        sentence = self.general_normalization.number_correction(sentence=sentence)
        telephones = []
        numbers_with_telephone1 = re.findall('تلفن: [۰-۹]+', sentence)
        if numbers_with_telephone1:
            telephones.extend(numbers_with_telephone1)
        numbers_with_telephone2 = re.findall('تلفن [۰-۹]+', sentence)
        if numbers_with_telephone2:
            telephones.extend(numbers_with_telephone2)
        numbers_with_telephone3 = re.findall(' و [۰-۹]+ تلفن های  [۰-۹]+', sentence)
        if numbers_with_telephone3:
            telephones.extend(numbers_with_telephone3)
        numbers_with_telephone4 = re.findall('تلفن های [۰-۹]+ و [۰-۹]+', sentence)
        if numbers_with_telephone4:
            telephones.extend(numbers_with_telephone4)
        numbers_with_telephone5 = re.findall('تلفنهای [۰-۹]+ و [۰-۹]+', sentence)
        if numbers_with_telephone5:
            telephones.extend(numbers_with_telephone5)
        numbers_with_telephone6 = re.findall('فکس [۰-۹]+', sentence)
        if numbers_with_telephone6:
            telephones.extend(numbers_with_telephone6)
        numbers_with_telephone7 = re.findall('فاکس [۰-۹]+', sentence)
        if numbers_with_telephone7:
            telephones.extend(numbers_with_telephone7)
        numbers_with_telephone8 = re.findall('۰۹[۰-۹]{9}', sentence)
        if numbers_with_telephone8:
            telephones.extend(numbers_with_telephone8)
        numbers_with_telephone9 = re.findall('۰۲۱[۰-۹]{8}', sentence)
        if numbers_with_telephone9:
            telephones.extend(numbers_with_telephone9)
        numbers_with_telephone10 = re.findall('۰۲۱-[۰-۹]{8}', sentence)
        if numbers_with_telephone10:
            telephones.extend(numbers_with_telephone10)
        numbers_with_telephone11 = re.findall('۰۲۱-[۰-۹]+', sentence)
        if numbers_with_telephone11:
            telephones.extend(numbers_with_telephone11)
        numbers_with_telephone12 = re.findall('۰۲۱[۰-۹]+', sentence)
        if numbers_with_telephone12:
            telephones.extend(numbers_with_telephone12)
        numbers_with_telephone13 = re.findall('تلفن \+[۰-۹]+', sentence)
        if numbers_with_telephone13:
            telephones.extend(numbers_with_telephone13)
        numbers_with_telephone14 = re.findall('تلفن [۰-۹]+\s?-\s?[۰-۹]+', sentence)
        if numbers_with_telephone14:
            telephones.extend(numbers_with_telephone14)
        numbers_with_telephone15 = re.findall('شماره تماس: [۰-۹]+', sentence)
        if numbers_with_telephone15:
            telephones.extend(numbers_with_telephone15)
        numbers_with_telephone16 = re.findall('سامانه پیامکی: [۰-۹]+', sentence)
        if numbers_with_telephone16:
            telephones.extend(numbers_with_telephone16)
        numbers_with_telephone17 = re.findall(' شماره: [۰-۹]+', sentence)
        if numbers_with_telephone17:
            telephones.extend(numbers_with_telephone17)
        numbers_with_telephone18 = re.findall(' شماره [۰-۹]+', sentence)
        if numbers_with_telephone18:
            telephones.extend(numbers_with_telephone18)
        for telephone in telephones:
            tels = re.findall('\+?[۰-۹]+', telephone)
            for tel in tels:
                sentence = sentence.replace(tel, self.number_with_varaible_length(str(tel)))
        return sentence

    def convert_number_to_letter(self, number):
        text = words(number)
        text = text.replace("یکصد", "صد")
        return text

    def number_with_varaible_length(self, number):
        converted_to_text = " "
        idx = 0
        step_round = 0
        if number[0] == "+":
            converted_to_text += " دو صفر "
            converted_to_text += self.convert_number_to_letter(number[1:3])
            number = number[3:]
        if len(number) == 1:
            steps_template = [[1]]
        elif len(number) == 2:
            steps_template = [[2]]
        elif len(number) == 3:
            steps_template = [[3]]
        elif len(number) == 4:
            steps_template = [[2, 2]]
        elif len(number) == 5:
            steps_template = [[3, 2], [2, 3]]
        elif len(number) == 6:
            steps_template = [[3, 3], [2, 2, 2]]
        elif len(number) == 7:
            steps_template = [[3, 2, 2], [2, 2, 3], [2, 3, 2]]
        elif len(number) == 8:
            steps_template = [[3, 3, 2], [2, 3, 3], [3, 2, 3], [2, 2, 2, 2]]
        elif len(number) == 9:
            steps_template = [[3, 3, 3], [3, 2, 2, 2], [2, 3, 2, 2], [2, 2, 3, 2], [2, 2, 2, 3]]
        elif len(number) == 10:
            steps_template = [[2, 2, 2, 2, 2], [3, 3, 2, 2], [2, 2, 3, 3], [3, 2, 2, 3], [2, 3, 2, 3], [3, 2, 3, 2],
                              [2, 3, 2, 3]]
        elif len(number) == 11:
            if number[0:2] == "۰۹":
                steps_template = [[3, 2, 2], [2, 2, 3], [2, 3, 2]]
                idx += 4
                converted_to_text += " صفر "
                converted_to_text += self.convert_number_to_letter(number[1:4])
            else:
                if number[0] == "۰":
                    converted_to_text += " صفر "
                    idx += 1
                    steps_template = [[2, 3, 3, 2], [2, 2, 3, 3], [2, 3, 2, 3], [2, 2, 2, 2, 2]]
                else:
                    steps_template = [[3, 3, 3, 2], [3, 2, 3, 3], [3, 3, 2, 3], [3, 2, 2, 2, 2]]
        elif len(number) == 12:
            steps_template = [[3, 3, 3, 3], [2, 2, 2, 3, 3], [2, 3, 3, 2, 3], [2, 2, 3, 2, 3], [2, 2, 3, 3, 2],
                              [3, 3, 2, 2, 2], [3, 2, 3, 2, 2], [3, 2, 2, 3, 2], [3, 2, 2, 2, 3]]
        elif len(number) == 13:
            steps_template = [[3, 3, 3, 2, 2], [3, 2, 2, 3, 3], [3, 3, 2, 2, 3], [2, 2, 3, 3, 3], [2, 3, 3, 3, 2],
                              [2, 3, 2, 3, 3],
                              [2, 3, 3, 2, 3], [3, 2, 2, 2, 2, 2], [2, 3, 2, 2, 2, 2], [2, 2, 3, 2, 2, 2],
                              [2, 2, 2, 3, 2, 2],
                              [2, 2, 2, 2, 3, 2], [2, 2, 2, 2, 2, 3]]
        elif len(number) == 14:
            steps_template = [[2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 2], [2, 3, 3, 3, 3], [3, 2, 3, 3, 3], [3, 3, 2, 3, 3],
                              [3, 3, 3, 2, 3], [3, 3, 2, 2, 2, 2],
                              [2, 2, 2, 2, 3, 3], [2, 3, 2, 3, 2, 2], [2, 2, 2, 3, 2, 3], [3, 2, 3, 2, 2, 2],
                              [3, 2, 2, 2, 3, 2]]
        elif len(number) == 15:
            steps_template = [[3, 3, 3, 3, 3], [2, 2, 2, 3, 3, 3], [2, 3, 2, 3, 2, 3], [3, 2, 3, 2, 3, 2],
                              [2, 2, 2, 2, 2, 2, 3],
                              [2, 2, 3, 3, 2, 3], [3, 3, 2, 2, 2, 3], [2, 2, 3, 3, 3, 2],
                              [2, 2, 3, 3, 3, 2],
                              [3, 3, 2, 2, 3, 2], [2, 3, 2, 2, 2, 2, 2], [2, 2, 3, 2, 2, 2, 2],
                              [2, 2, 2, 3, 2, 2, 2],
                              [2, 2, 2, 2, 3, 2, 2], [2, 2, 2, 2, 2, 3, 2], [2, 2, 2, 2, 2, 2, 3]]
        elif len(number) % 2 == 0:
            length = int(len(number) / 2)
            steps_template = [[2 for index in range(length)]]
        else:
            length = int((len(number) - 3) / 2)
            steps_template = [[2 for index in range(length)]]
            steps_template[0].append(3)
        steps_template_number = random.randint(0, len(steps_template) - 1)
        steps = steps_template[steps_template_number]
        while idx < len(number):
            converted_to_text += " "
            this_template = number[idx: idx + steps[step_round]]
            if this_template == "۰۰۰":
                converted_to_text += " سه صفر "
            elif this_template == "۰۰":
                converted_to_text += " دو صفر "
            elif this_template[0:2] == "۰۰":
                converted_to_text += " دو صفر "
            elif this_template[0] == "۰":
                converted_to_text += " صفر "
            converted_to_text += self.convert_number_to_letter(number[idx: idx + steps[step_round]])
            idx = idx + steps[step_round]
            step_round += 1
        return converted_to_text
