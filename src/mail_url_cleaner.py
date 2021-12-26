from urlextract import URLExtract
import re

extractor = URLExtract()


class mail_url_cleaner:

    def find_urls_clean(self, sentence):
        urls_start_www = re.findall("www.\s?[\sa-z0-9.-]+[.][\sa-z]{2,4}/?", sentence)
        if urls_start_www:
            for url in urls_start_www:
                old_url = url
                url = url.replace("://", " do noghte slash slash ")
                url = url.replace(".", " dot ")
                url = url.split("/")[0]
                sentence = sentence.replace(str(old_url), str(url))

        urls_start_http = re.findall("https?://www.\s?[\sa-z0-9.-]+[.][\sa-z]{2,4}/?", sentence)
        if urls_start_http:
            for url in urls_start_http:
                old_url = url
                url = url.replace("://", " do noghte slash slash ")
                url = url.replace(".", " dot ")
                url = url.split("/")[0]
                sentence = sentence.replace(str(old_url), str(url))

        urls = extractor.find_urls(sentence)
        if urls:
            for url in urls:
                old_url = url
                url = url.replace("://", " do noghte slash slash ")
                url = url.replace(".", " dot ")
                url = url.split("/")[0]
                sentence = sentence.replace(str(old_url), str(url))
        return sentence

    def find_mails_clean(self, sentence):
        sentence = str(sentence)
        mails = re.findall(r"[A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+", sentence)
        if mails:
            for mail in mails:
                old_mail = mail
                mail = mail.replace(".", " dot ")
                mail = mail.replace("@", " at ")
                mail = mail.replace("-", " dash ")
                mail = mail.replace("_", " underline ")
                sentence = sentence.replace(str(old_mail), str(mail))
        return sentence

    def remove_meaning_less_url(self, sentence):
        mails = re.findall(r"https?://[\s\S]*", sentence)
        for mail in mails:
            sentence = sentence.replace(mail, " ")
        return sentence
