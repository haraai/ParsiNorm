from tqdm import tqdm
import os
from Tokenizer import Tokenizer
from clean import clean
from multiprocessing import Pool

if __name__ == "__main__":
    steps = [[3, 3, 3, 3, 3], [2, 2, 2, 3, 3, 3], [2, 3, 2, 3, 2, 3], [3, 2, 3, 2, 3, 2],
                              [2, 2, 2, 2, 2, 2, 3],
                              [2, 2, 3, 3, 2, 3], [3, 3, 2, 2, 2, 3], [2, 2, 3, 3, 3, 2],
                              [2, 2, 3, 3, 3, 2],
                              [3, 3, 2, 2, 3, 2], [2, 3, 2, 2, 2, 2, 2], [2, 2, 3, 2, 2, 2, 2],
                              [2, 2, 2, 3, 2, 2, 2],
                              [2, 2, 2, 2, 3, 2, 2], [2, 2, 2, 2, 2, 3, 2], [2, 2, 2, 2, 2, 2, 3]]
    for step in steps:
        sum = 0
        for k in step:
            sum += k
        print(sum)
    tokenizer = Tokenizer()
    clean = clean()


    def save_to_file(file_path, data):
        with open(file_path, 'a') as file:
            file.writelines(data)


    def read_data(file_address):
        file = open(file_address, 'r', encoding='utf-8', errors='ignore')
        sentences = file.readlines()
        return sentences


    directory = "/hdd4/callcenter_storage/data/Language_Model/raw/miras/raw_miras/"
    save_directory = "output_path"
    filename = "xaa"

    # sentences = read_data(os.path.join(directory, filename))
    sentences = ['src="https://www', 'src="http://www', "The New Update Add New MTK X20 X25 EMMC Flash Init",
                 '<script type="text/javascript" src="http://www ',
                 'com/Feed"></script> خبرهای 301 پژو 301 چراغ خاموش می‌آید   تسنیم   ۹ ساعت پیش ی تسنیم، طی روزهای اخیر موضوع پیش فروش خودروی ',
                 'com/images/2015/10/funny_photos',
                 '<span style="display: block;padding-top: 57%">',
                 'com/video/video/embed/videohash/v3eKT/vt/frame" allowFullScreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" ></iframe>',
                 '<iframe src="https://www',
                 'h_iframe-aparat_embed_frame{position:relative;}',
                 'h_iframe-aparat_embed_frame',
                 'سلام{} چطو[]ری[]',
                 '۱۱۹۲۰۰۰۱۱۹۴۸۰۰۱۱۹۴۳۰۰۱۱۹۱۱۰۰۱۱۹۰۰۰۰۱۱۹۰۲۰۰',
                 '۱۲۲۵۳۰۰۱۲۲۶۶۰۰۱۲۲۳۳۰۰۱۲۱۹۷۰۰۱۲۱۸۰۰۰۱۲۱۹۱۰۰',
                 "www.france24.com/en/20161207-paris-winter-air-pollution-worst-10-years",
                 "www.google.com",
                 "www. google .com",
                 "www.google .com",
                 'http://www.google.com',
                 'http://www.yahoo.com این آدرس است باتبی اذیساتای اسات ایسا اسیا',
                 'https://www.varzesh.com/search?q=%D9%88%D8%B1%D8%B2%D8%B4&sxsrf=AOaemvISpT0scm2HVH2stkkxELK1U6e2og%3A1634408036291&ei=ZBZrYYmZEdyGjLsPqNuZ0Ak&oq=%D9%88%D8%B1%D8%B2%D8%B4&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCC4QgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggjEK4CELADECc6BAgjECc6BwgjEOoCECdKBAhBGAFQlQ9Ylx9gxCpoAnAAeASAAbECiAH6EZIBBTItNy4xmAEAoAEBsAEKyAEBwAEB&sclient=gws-wiz سذ یاس سیرا اسی اسی اسیا',
                 'کد خبر این است تاریخ 20 مهر <',
                 '3 - صفحه الكترونيكي: www.promaco.com.au/2006/icomos',
                 '<script type="text/javascript" src="http://www',
                 'com/Feed"></script> خبرهای کوهن ادعای رییس موساد: ایران نفوذ خود در خاورمیانه را گسترش داده است   بوکان نیوز   ۱۷ ساعت پیش',
                 'منبع: روزنامه اينديپندنت اول دسامبر 2006',
                 'www.hamshahrionline.ir',
                 'در هنگام مراجعه به مراكز اعلام شده همراه دارنده موتور باشد. 4 - صفحه الكترونيكي: http://www.ivtconferences.com/shop/scripts',
                 'www. hamshahri. online. ir',
                 'www. hamshahri.online.ir  یستند ایستس  تیس تسی تسنیت تسنیت',
                 'www. faryaad.com',
                 'www. uts. edu. au/div/ ssu/ bulgangurra. htmi',
                 'http://www.under water land. com',
                 'http://www. nassio.com',
                 'http://www.shel silverstein.com',
                 'تلفن: ۵۰۰۰۱۰۶۰۰۰۴۵۰۳۱',
                 'www.nushk.ir وب سایت دانشکده',
                 'وب سایت دانشکده agr.nushk.ir',
                 'Wikipedia contributors Snowball Earth Wikipedia The Free Encyclopedia https do noghte slash slash en dot wikipedia dot org ( بازبینی ژوئن چهار ، دو هزار و پانزده )  .',
                 'Wikipedfia contributors Jadgali language Wikipedia The Free Encyclopedia',
                 ' تیب .B.S.A.A',
                 'مسأله',
                 'جزء',
                 'إی',
                 'ٱ',
                 'تئاتر',
                 'مسئله',
                 'سؤال',
                 'پوئتیک',
                 'مسئول',
                 'سئوال',
                 "بنیتتد یبتئو ۱.۷۷۶۹۹۹۹۹۹۹۹۹۹۹۹۹۱۲",
                 "12/466663456789127634563765434567890456789098763456756765434567895323453253456 نیت",
                 " T   q F v۶  MODU         Ne ؟ ۰    j)",
                 "m n۷d  n dgYSr!  u",
                 "m n۷d  n dgYSr!  u ",
                 "?S",
                 '<$2ڮV2Stq9&v6*HAKEMW$@ق&^d[W"Oՠ+(,Du]?΀2hs(bNZޜJiu>:B[,~5YT<K1@ς z:BM#W%xng/RHe]ЬH}',
                 'شهرستان ریسارالدا ۴٬۱۴۰ کیلومترمربع مساحت و ۹۴۱٬۲۸۳ نفر جمعیت دارد',
                 ' و با وجود یکسان ماندن بیشینهٔ سرعت، در ۳٫۷ ثانیه به سرعت صد کیلومتر بر ساعت می رسید.',
                 ' کمپانی رویال داچ شل؛ ۳۴٪ درصد و شرکت فرانسوی توتال نیز مالک ۴٪ درصد از سهام شرکت توسعه نفت عمان می باشد.',
                 'دائرة المعارف بزرگ اسلامی - ابن زیله',
                 'ر اساس اساسنامه دانشگاه شاهد هیئت امناء این دانشگاه متشکل از ۸ نفر از شخصیت های کشوری و اعضای هیئت علمی دانشگاه ها ست ای افراد عبارتند از',
                 'اچ ام اس دراگن (۱۸۷۸) یک کشتی بود که طول آن بود. این کشتی در سال ۱۸۷۸ ساخته شد',
                 'خودکشی عاشقانه در سونه زاکی فیلمی است که در سال ۱۹۷۸ اکران شد. از بازیگران آن می توان به ریودو اوزاکی، میکو کاجی، هیساشی ایگاوا، و ساچیکو هیداری اشاره کرد',
                 'بنابر سرشماری مرکز آمار ایران، جمعیت بخش همایجان شهرستان سپیدان در سال ۱۳۸۵ برابر با ۲۷۰۷۳ نفر بوده است.',
                 ' آن ها همچنین در فن کافهٔ کره ای خود خبر از کامبک کره ای در اوایل نوامبر ۲۰۱۴ دادند',
                 'نوزدهم ژوئیه ۱۹۴۵- بیست و یکم ژوئن ۱۸۶۴',
                 'مسال یعنی سال ۱۳۹۲، سال ۱۳۸۸ نخواهد شد، ',
                 'نگارش، طراحي صحنه و كارگرداني نمايش «دختران سفيد»، تبريز، خانه ي تئاتر، مراغه، تالار صوفي، 1387و1388',
                 'این روستا در دهستان براآن شمالی قرار دارد و براساس سرشماری مرکز آمار ایران در سال ۱۳۸۵، جمعیت آن ۱٬۷۰۴ نفر (۳۷۴خانوار) بوده است.',
                 ' و با وجود یکسان ماندن بیشینهٔ سرعت، در ۳٫۷ ثانیه به سرعت صد کیلومتر بر ساعت می رسید.',
                 'در ستون چپ جمع اعداد ۲ و ۸ و ۳۲ عدد ۴۲ را می سازند پس با جمع اعداد روبرویشان یعنی ۶۲ و ۲۴۸ و ۹۹۲ حاصل ضرب بدست می آید.',
                 '۴۶۹٫۰۷ کیلومتر مربع است',
                 ' هایشتنباخ ۱٬۱۶۳ نفر جمعیت دارد.'
                 ]


    def pre_process(sentences):
        print(len("۷۷۶۹۹۹۹۹۹۹۹۹۹۹۹۹۱۲"))
        for index in tqdm(range(len(sentences))):
            sentences[index] = clean.clean_sentence(sentences[index])
            for sentence in tokenizer.sentence_tokenize(sentences[index]):
                pass
                print(sentence)
                # save_to_file(os.path.join(save_directory, filename), sentence)


    pre_process(sentences)
    # with Pool(20) as p:
    #     print(p.map(pre_process, sentences))
