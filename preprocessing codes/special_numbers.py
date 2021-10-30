import re
from num2fawords import words
import copy
from itertools import groupby
from string import punctuation
from persian_tools.bank import card_number
from persian_tools.bank import sheba
from persian_tools import national_id
import random
from general_normalization import general_normalization


class special_numbers:
    def __init__(self):
        self.general_normalization = general_normalization()

    def convert_number_to_letter(self, number):
        if len(number) > 15:
            text = self.special_number_to_text(number, "long")
            return text
        else:
            text = " "
            text += words(number)
            text += " "
            text = text.replace("یکصد", "صد")
            text = text.replace("یک هزار", "هزار")
            return text

    def convert_numbers_to_text(self, sentence):
        sentence = self.general_normalization.number_correction(sentence=sentence)
        between_nums = re.findall('[۰-۹]+\s?-\s?[۰-۹]+', sentence)
        if between_nums:
            for between_num in between_nums:
                between_num_new = copy.copy(between_num)
                between_number_numbers = between_num.replace("-", " الی ").split(" الی ")
                for number in between_number_numbers:
                    between_num_new = between_num_new.replace(str(number), self.convert_number_to_letter(number))
            sentence = sentence.replace(str(between_num), between_num_new)
            sentence = sentence.replace("-", "خط تیره")
        floating_points = re.findall('[۰-۹]+\.[۰-۹]+', sentence)
        for floating_point in floating_points:
            natural_number = floating_point.split(".")[0]
            exp_number = floating_point.split(".")[1]
            if len(exp_number) > 4:
                exp_number = exp_number[:4]
                floating_point_new = f"{natural_number}.{exp_number}"
            floating_point_new = words(str(floating_point_new), decimal_separator=' ممیز ')
            sentence = sentence.replace(str(floating_point), floating_point_new)
        numbers = re.findall('[۰-۹]+', sentence)
        for index in range(len(numbers)):
            numbers[index] = int(numbers[index])
        numbers.sort(reverse=True)
        for index in range(len(numbers)):
            numbers[index] = self.general_normalization.number_correction(sentence=str(numbers[index]))
        for number in numbers:
            sentence = sentence.replace(str(number), self.convert_number_to_letter(number))
        return sentence

    def special_number_to_text(self, number, type):
        converted_to_text = " "
        if type == "National_ID":
            steps_template = [[2, 2, 2, 2, 2], [3, 3, 2, 2], [2, 2, 3, 3], [3, 2, 2, 3], [2, 3, 2, 3], [3, 2, 3, 2],
                              [2, 3, 2, 3]]
        if type == "card_number":
            steps_template = [[2, 2, 2, 2, 2, 2, 2, 2]]
        if type == "shaba":
            steps_template = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
            converted_to_text = " آی آر "
        if type == "long":
            if len(number) % 2 == 0:
                length = int(len(number) / 2)
                steps_template = [[2 for index in range(length)]]
            else:
                length = int((len(number) - 3) / 2)
                steps_template = [[2 for index in range(length)]]
                steps_template[0].append(3)
        idx = 0
        step_round = 0
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

    def replace_national_code(self, sentence):
        sentence = self.general_normalization.number_correction(sentence=sentence)
        numbers = re.findall('[۰-۹]{10}', sentence)
        for number in numbers:
            if national_id.validate(number):
                number_converted_to_text = self.special_number_to_text(number, "National_ID")
                sentence = sentence.replace(number, number_converted_to_text)
        return sentence

    def replace_card_number(self, sentence):
        sentence = self.general_normalization.number_correction(sentence=sentence)
        numbers = re.findall('[۰-۹]{16}', sentence)
        for number in numbers:
            if card_number.validate(number):
                number_converted_to_text = self.special_number_to_text(number, "card_number")
                sentence = sentence.replace(number, number_converted_to_text)
        return sentence

    def replace_shaba(self, sentence):
        sentence = self.general_normalization.number_correction(sentence=sentence)
        numbers = re.findall('IR[۰-۹]{24}', sentence)
        for number in numbers:
            if sheba.validate(number):
                number_new = number[2:]
                number_converted_to_text = self.special_number_to_text(number_new, "shaba")
                sentence = sentence.replace(number, number_converted_to_text)
        return sentence
