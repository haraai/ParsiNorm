import copy
import re


class abbreviation:
    def __init__(self):
        self.persian_date_type1 = {'ه.ش.': 'هجری شمسی'}
        self.persian_date_type2 = {'ه.ش': 'هجری شمسی'}
        self.persian_date_type3 = {'ه . ش.': 'هجری شمسی'}
        self.persian_date_type4 = {'ه. ش.': 'هجری شمسی'}
        self.persian_date_type5 = {'ه. ش.': 'هجری شمسی'}
        self.ghamari_date_type1 = {'ه.ق.': 'هجری قمری'}
        self.ghamari_date_type2 = {'ه.ق': 'هجری قمری'}
        self.ghamari_date_type3 = {'ه . ق.': 'هجری قمری'}
        self.ghamari_date_type4 = {'ه. ق.': 'هجری قمری'}
        self.ghamari_date_type5 = {'ه. ق.': 'هجری قمری'}
        self.ghable_milad_date_type1 = {'ق.م': 'قبل از میلاد'}
        self.ghable_milad_date_type2 = {'ق.م.': 'قبل از میلاد'}
        self.milad_date = {'م. ': ' میلادی'}
        self.ghamari_date = {'ق. ': ' قمری'}

        self.date_replaces = [
            self.persian_date_type1,
            self.persian_date_type2,
            self.persian_date_type3,
            self.persian_date_type4,
            self.persian_date_type5,
            self.ghamari_date_type1,
            self.ghamari_date_type2,
            self.ghamari_date_type3,
            self.ghamari_date_type4,
            self.ghamari_date_type5,
            self.ghable_milad_date_type1,
            self.ghable_milad_date_type2,
            self.milad_date,
            self.ghamari_date,
        ]

        self.persian_aj_label = {'(عج)': ' عجل الله تعالی فرجه الشریف '}
        self.persian_ein_label = {'(ع)': ' علیه السلام '}
        self.persian_rah_label = {'(ره)': ' رحمة الله علیه '}
        self.persian_sad_label = {'(ص)': ' صلی الله علیه و آله و سلم '}
        self.persian_salam_label = {'(س)': ' سلام الله علیها '}
        self.persian_rezvan_label = {'(رض)': ' رضوان الله تعالی علیه '}
        self.persian_razi_label = {'(رضی)': ' رضی الله عنه '}

        self.persain_label_replaces = [
            self.persian_aj_label,
            self.persian_ein_label,
            self.persian_rah_label,
            self.persian_sad_label,
            self.persian_salam_label,
            self.persian_rezvan_label,
            self.persian_razi_label
        ]
        # law
        self.law1 = {'د.ع.ک': 'دیوان عالی کشور'}
        self.law2 = {'د.ع.ک.': 'دیوان عالی کشور'}
        self.law3 = {'ق.ا': 'قانون اساسی'}
        self.law4 = {'ق.ا.': 'قانون اساسی'}
        self.law5 = {'ق.م': 'قانون مدنی'}
        self.law6 = {'ق.م.': 'قانون مدنی'}
        self.law7 = {'ق.ت': 'قانون تجارت'}
        self.law8 = {'ق.ت.': 'قانون تجارت'}
        self.law9 = {'ق.ک': 'قانون کار'}
        self.law10 = {'ق.ک.': 'قانون کار'}
        self.law11 = {'ر.ر': 'روزنامه رسمی'}
        self.law12 = {'ر.ر.': 'روزنامه رسمی'}
        self.law13 = {'ق.چ': 'قانون صدور چک'}
        self.law14 = {'ق.چ.': 'قانون صدور چک'}
        self.law15 = {'ق.ث': 'قانون ثبت اسناد و املاک'}
        self.law16 = {'ق.ث.': 'قانون ثبت اسناد و املاک'}
        self.law17 = {'ق.ث.ا': 'قانون ثبت احوال'}
        self.law18 = {'ق.ث.ا.': 'قانون ثبت احوال'}
        self.law19 = {'ق.ز.ش': 'قانون زمین شهری'}
        self.law20 = {'ق.ز.ش.': 'قانون زمین شهری'}
        self.law21 = {'ق.م.ف.': 'قانون مدنی فرانسه'}
        self.law22 = {'ق.م.م': 'قانون مسئولیت مدنی'}
        self.law23 = {'ق.م.م.': 'قانون مسئولیت مدنی'}
        self.law24 = {'ق.م.ع': 'قانون مجازات عمومی'}
        self.law25 = {'ق.م.ع.': 'قانون مجازات عمومی'}
        self.law26 = {'ق.ح.خ': 'قانون حمایت خانواده'}
        self.law27 = {'ق.ح.خ.': 'قانون حمایت خانواده'}
        self.law28 = {'ق.ث.ش': 'قانون ثبت شرکت ها'}
        self.law29 = {'ق.ث.ش.': 'قانون ثبت شرکت ها'}
        self.law30 = {'ق.ت.آ': 'قانون تملک آپارتمان ها'}
        self.law31 = {'ق.ت.آ.': 'قانون تملک آپارتمان ها'}
        self.law32 = {'ا.ح.ب.': 'اعلامیه جهانی حقوق بشر'}
        self.law33 = {'ق.ث.ع.ا': 'قانون ثبت علائم واختراعات'}
        self.law34 = {'ق.ث.ع.ا.': 'قانون ثبت علائم واختراعات'}
        self.law35 = {'ق.ن.ا.م': 'قانون نحوه اجرای محکومیت های مالی'}
        self.law36 = {'ق.ن.ا.م.': 'قانون نحوه اجرای محکومیت های مالی'}
        self.law37 = {'ق.ح.ح': 'قانون حمایت حقوق مؤلفان و مصنفان و هنرمندان'}
        self.law38 = {'ق.ح.ح.': 'قانون حمایت حقوق مؤلفان و مصنفان و هنرمندان'}
        self.law39 = {'ق.م.ا': 'قانون مجازات اسلامی'}
        self.law40 = {'ق.م.ا.': 'قانون مجازات اسلامی'}
        self.law41 = {'آ.د.ک': 'آیین دادرسی کیفری'}
        self.law42 = {'آ.د.ک.': 'آیین دادرسی کیفری'}
        self.law43 = {'ق.آ.د.ک': 'قانون آیین دادرسی کیفری'}
        self.law44 = {'ق.آ.د.ک.': 'قانون آیین دادرسی کیفری'}
        self.law45 = {'ق.آ.د.م': 'قانون آیین دادرسی مدنی'}
        self.law46 = {'ق.آ.د.م.': 'قانون آیین دادرسی مدنی'}
        self.law47 = {'آ.آ.د.د.ع.ا': 'آیین نامه آیین دادرسی دیوان عدالت اداری'}
        self.law48 = {'آ.آ.د.د.ع.ا.': 'آیین نامه آیین دادرسی دیوان عدالت اداری'}
        self.law49 = {'آ.ا.ق.ت.د.ع': 'آیین نامه اصلاحی قانون تشکیل دادگاه های عمومی و انقلاب'}
        self.law50 = {'آ.ا.ق.ت.د.ع.': 'آیین نامه اصلاحی قانون تشکیل دادگاه های عمومی و انقلاب'}
        self.law51 = {'آ.ا.ق.ت.د.ع.': 'آیین نامه اصلاحی قانون تشکیل دادگاه های عمومی و انقلاب'}
        self.law52 = {'ق.ا.ا.م': 'قانون اجرای احکام مدنی'}
        self.law53 = {'ق.ا.ا.م.': 'قانون اجرای احکام مدنی'}
        self.law54 = {'ق.ا.پ.ق.د': 'قانون اصلاحی پاره ای قوانین دادگستری'}
        self.law55 = {'ق.ا.پ.ق.د.': 'قانون اصلاحی پاره ای قوانین دادگستری'}
        self.law56 = {'ق.ا.ح': 'قانون امور حسبی'}
        self.law57 = {'ق.ا.ح.': 'قانون امور حسبی'}
        self.law58 = {'ق.ا.ق.ج.ت.ع': 'قانون اصلاح قانون جلوگیری از تصرفات عدوانی'}
        self.law59 = {'ق.ا.ق.ج.ت.ع.': 'قانون اصلاح قانون جلوگیری از تصرفات عدوانی'}
        self.law60 = {'ق.ا.ق.ت.د.ع.ا': 'قانون اصلاح قانون تشکیل دادگاه های عمومی و انقلاب'}
        self.law61 = {'ق.ا.ق.ت.د.ع.ا.': 'قانون اصلاح قانون تشکیل دادگاه های عمومی و انقلاب'}
        self.law62 = {'ق.ت.د.ح.ی.و.د': 'قانون تشکیل دادگاه های حقوقی یک و دو'}
        self.law63 = {'ق.ت.د.ح.ی.و.د.': 'قانون تشکیل دادگاه های حقوقی یک و دو'}
        self.law64 = {'ق.ت.د.ع.ا': 'قانون تشکیل دادگاه های عمومی و انقلاب'}
        self.law65 = {'ق.ت.د.ع.ا.': 'قانون تشکیل دادگاه های عمومی و انقلاب'}
        self.law66 = {'ق.د.ع.ا': ' قانون دیوان عدالت اداری'}
        self.law67 = {'ق.د.ع.ا.': ' قانون دیوان عدالت اداری'}
        self.law68 = {'ق.ک.ا.پ.و.د': 'قانون کیفیت اخذ پروانه وکالت دادگستری'}
        self.law69 = {'ق.ک.ا.پ.و.د.': 'قانون کیفیت اخذ پروانه وکالت دادگستری'}
        self.law70 = {'ل.ق.ا.ک.و.د': 'لایحه قانونی استقلال کانون وکلای دادگستری'}
        self.law71 = {'ل.ق.ا.ک.و.د.': 'لایحه قانونی استقلال کانون وکلای دادگستری'}
        self.law72 = {'آ.ل.ق.ا.ک.و.د': 'آیین نامه لایحه قانونی استقلال کانون وکلای دادگستری'}
        self.law73 = {'آ.ل.ق.ا.ک.و.د.': 'آیین نامه لایحه قانونی استقلال کانون وکلای دادگستری'}
        self.law74 = {'ل.ق.ت.د.ع': 'لایحه قانونی تشکیل دادگاه عمومی'}
        self.law75 = {'ل.ق.ت.د.ع.': 'لایحه قانونی تشکیل دادگاه عمومی'}
        self.law76 = {'ل.ق.د.م.خ': 'لایحه قانونی دادگاه مدنی خاص'}
        self.law77 = {'ل.ق.د.م.خ.': 'لایحه قانونی دادگاه مدنی خاص'}
        self.law78 = {'م. ق.ر.ر.ک': 'مجموعه قوانین روزنامه رسمی کشور'}
        self.law79 = {'م. ق.ر.ر.ک.': 'مجموعه قوانین روزنامه رسمی کشور'}
        self.law80 = {'ا.ح.د': 'اداره حقوقی دادگستری'}
        self.law81 = {'ا.ح.د.': 'اداره حقوقی دادگستری'}
        self.law82 = {'ا.ح.ق.ق': 'اداره حقوقی قوه قضائیه'}
        self.law83 = {'ا.ح.ق.ق.': 'اداره حقوقی قوه قضائیه'}
        self.law84 = {'ا.ا.ا.د.د.ن.ح.ک': 'ادله و ابزار اثبات دعوا در نظم حقوقی کنونی'}
        self.law85 = {'ا.ا.ا.د.د.ن.ح.ک.': 'ادله و ابزار اثبات دعوا در نظم حقوقی کنونی'}
        self.law86 = {'ق.ا.م.ح.ت': ' قانون اصول محاکمات حقوقی و تجاری مصوّب'}
        self.law87 = {'ق.ا.م.ح.ت.': ' قانون اصول محاکمات حقوقی و تجاری مصوّب'}
        self.law88 = {'ق.ا.م.ج': 'قانون اصول محاکمات جزایی'}
        self.law89 = {'ق.ا.م.ج.': 'قانون اصول محاکمات جزایی'}
        self.law90 = {'ق.آ.د.م.ف': 'قانون آیین دادرسی مدنی فرانسه'}
        self.law91 = {'ق.آ.د.م.ف.': 'قانون آیین دادرسی مدنی فرانسه'}
        self.law92 = {'ق.ت.ا': 'قانون تجارت الکترونیکی'}
        self.law93 = {'ق.ت.ا.': 'قانون تجارت الکترونیکی'}
        self.law94 = {'ق.ر.م.م': 'قانون روابط موجر و مستأجر مصوّب'}
        self.law95 = {'ق.ر.م.م.': 'قانون روابط موجر و مستأجر مصوّب'}
        self.law96 = {'ق.ش.ح.ا': 'قانون شورای حل اختلاف مصوّب'}
        self.law97 = {'ق.ش.ح.ا.': 'قانون شورای حل اختلاف مصوّب'}
        self.law98 = {'ق.ع.ا': 'قواعد عمومی اثبات دعوا'}
        self.law99 = {'ق.ع.ا.': 'قواعد عمومی اثبات دعوا'}
        self.law100 = {'ق.م.ف': 'قانون مدنی فرانسه'}
        self.law101 = {'ق.ن.ا.م.م': 'قانون نحوه ی اجرای محکومیّت های مالی مصوّب'}
        self.law102 = {'ق.ن.ا.م.م.': 'قانون نحوه ی اجرای محکومیّت های مالی مصوّب'}
        self.law103 = {'ل.آ.د.ت': 'لایحه ی آیین دادرسی تجاری'}
        self.law104 = {'ل.آ.د.ت.': 'لایحه ی آیین دادرسی تجاری'}
        self.law105 = {'ل.آ.د.ک': 'لایحه ی آیین دادرسی کیفری جدید'}
        self.law106 = {'ل.آ.د.ک.': 'لایحه ی آیین دادرسی کیفری جدید'}
        self.law107 = {'ل.ق.م.ا.ج': 'لایحه قانون مجازات اسلامی جدید'}
        self.law108 = {'ل.ق.م.ا.ج.': 'لایحه قانون مجازات اسلامی جدید'}
        self.law109 = {'ق.د.ا.ر.ک': 'قانون دفاتر اسناد رسمی و کانون سردفتران و دفتریاران'}
        self.law110 = {'ق.د.ا.ر.ک.': 'قانون دفاتر اسناد رسمی و کانون سردفتران و دفتریاران'}
        self.law111 = {'ق.ت.ت.ا': 'قانون تسهیل تنظیم اسناد در دفاتر اسناد رسمی'}
        self.law112 = {'ق.ت.ت.ا.': 'قانون تسهیل تنظیم اسناد در دفاتر اسناد رسمی'}
        self.law113 = {'آ.ق.ث.ا': 'آیین نامه قانون ثبت املاک'}
        self.law114 = {'آ.ق.ث.ا.': 'آیین نامه قانون ثبت املاک'}
        self.law115 = {'آ.ا.ق.ت.آ': 'آیین نامه اجرایی قانون تملک آپارتمان ها'}
        self.law116 = {'آ.ا.ق.ت.آ.': 'آیین نامه اجرایی قانون تملک آپارتمان ها'}
        self.law117 = {'ق.آ.د.ا.م': 'قانون آیین دادرسی دادگاه های عمومی و انقلاب در امور مدنی'}
        self.law118 = {'ق.آ.د.ا.م.': 'قانون آیین دادرسی دادگاه های عمومی و انقلاب در امور مدنی'}
        self.law119 = {'ق.آ.د.ا.ک': 'قانون آیین دادرسی دادگاه های عمومی و انقلاب در امور کیفری'}
        self.law120 = {'ق.آ.د.ا.ک.': 'قانون آیین دادرسی دادگاه های عمومی و انقلاب در امور کیفری'}
        self.law121 = {'ق.ر.ت.ا': 'قانون راجع به ترجمه اظهارات و اسناد در محاکم و دفاتر اسناد رسمی'}
        self.law122 = {'ق.ر.ت.ا.': 'قانون راجع به ترجمه اظهارات و اسناد در محاکم و دفاتر اسناد رسمی'}
        self.law123 = {'آ.ا.م.ا.ر':
                           'آیین نامه اجرای مفاد اسناد رسمی لازم الاجرا و طرز رسیدگی به شکایت از عملیات اجرایی'}
        self.law124 = {'آ.ا.م.ا.ر.':
                           'آیین نامه اجرای مفاد اسناد رسمی لازم الاجرا و طرز رسیدگی به شکایت از عملیات اجرایی'}
        self.law125 = {'ق.ح.ق': 'قانون حدود و قصاص'}
        self.law126 = {'ق.ح.ق.': 'قانون حدود و قصاص'}
        self.law127 = {'ق.د.ک': 'قانون دادرسی و کیفر ارتش'}
        self.law128 = {'ق.د.ک.': 'قانون دادرسی و کیفر ارتش'}
        self.law129 = {'ق.ک.ع': 'قانون کیفر عمومی'}
        self.law130 = {'ق.ک.ع.': 'قانون کیفر عمومی'}
        self.law131 = {'ق.م.ا': 'قانون مجازات اسلامی'}
        self.law132 = {'آ.د.ک': 'آیین دادرسی کیفری'}
        self.law133 = {'آ.د.ک.': 'آیین دادرسی کیفری'}

        self.law_replaces = [
            self.law1, self.law2, self.law3, self.law4, self.law5, self.law6, self.law7, self.law8, self.law9,
            self.law10, self.law11, self.law12, self.law13, self.law14, self.law15, self.law16, self.law17, self.law18,
            self.law19, self.law20, self.law21, self.law22, self.law23, self.law24, self.law25, self.law26, self.law27,
            self.law28, self.law29, self.law30, self.law31, self.law32, self.law33, self.law34, self.law35, self.law36,
            self.law37, self.law38, self.law39, self.law40, self.law41, self.law42, self.law43, self.law44, self.law45,
            self.law46, self.law47, self.law48, self.law49, self.law50, self.law51, self.law52, self.law53, self.law54,
            self.law55, self.law56, self.law57, self.law58, self.law59, self.law60, self.law61, self.law62, self.law63,
            self.law64, self.law65, self.law66, self.law67, self.law68, self.law69, self.law70, self.law71, self.law72,
            self.law73, self.law74, self.law75, self.law76, self.law77, self.law78, self.law79, self.law80, self.law81,
            self.law82, self.law83, self.law84, self.law85, self.law86, self.law87, self.law88, self.law89, self.law90,
            self.law91, self.law92, self.law93, self.law94, self.law95, self.law96, self.law97, self.law98, self.law99,
            self.law100, self.law101, self.law102, self.law103, self.law104, self.law105, self.law106, self.law107,
            self.law108, self.law109, self.law110, self.law111, self.law112, self.law113, self.law114, self.law115,
            self.law116, self.law117, self.law118, self.law119, self.law120, self.law121, self.law122, self.law123,
            self.law124, self.law125, self.law126, self.law127, self.law128, self.law129, self.law130, self.law131,
            self.law132, self.law133
        ]

        # books
        self.book1 = {'ن.ک': 'نگاه کنید'}
        self.book2 = {'ن.ک.': 'نگاه کنید'}
        self.book3 = {'ن.ک.ش': 'نگاه کنید به شماره'}
        self.book4 = {'ن.ک.ش.': 'نگاه کنید به شماره'}
        self.book5 = {'ن.ک.ص': 'نگاه کنید به صفحه'}
        self.book6 = {'ن.ک.ص.': 'نگاه کنید به صفحه'}
        self.book7 = {'ر.ک': 'رجوع کنید'}
        self.book8 = {'ر.ک.': 'رجوع کنید'}
        self.book9 = {'پ.ن': 'پی‌نوشت'}
        self.book10 = {'پ.ن.': 'پی‌نوشت'}
        self.book11 = {'ص.ع': 'صفحه‌ی عنوان'}
        self.book12 = {'ص.ع.': 'صفحه‌ی عنوان'}
        self.book13 = {'ی.د': 'یادداشت دامنه'}
        self.book14 = {'ی.د.': 'یادداشت دامنه'}

        self.book_replaces = [
            self.book1, self.book2, self.book3, self.book4, self.book5, self.book6, self.book7, self.book8, self.book9,
            self.book10, self.book11, self.book12, self.book13, self.book14,
        ]
        # other
        self.other1 = {'آ.پ': 'آموزش و پرورش'}
        self.other2 = {'آ.پ.': 'آموزش و پرورش'}
        self.other3 = {'ج.ا.ا': 'جمهوری اسلامی ایران'}
        self.other4 = {'ج.ا.ا.': 'جمهوری اسلامی ایران'}
        self.other5 = {'ج.ا': 'جمهوری اسلامی'}
        self.other6 = {'ج.ا.': 'جمهوری اسلامی'}
        self.other7 = {'ش.م.ر': 'شیمیایی میکروبی رادیو اکتیو'}
        self.other8 = {'ش.م.ر.': 'شیمیایی میکروبی رادیو اکتیو'}
        self.other9 = {'ش.م.ه': 'شیمیایی میکروبی هسته‌ای'}
        self.other10 = {'ش.م.ه.': 'شیمیایی میکروبی هسته‌ای'}
        self.other11 = {'ع.س': 'عقیدتی سیاسی'}
        self.other12 = {'ع.س.': 'عقیدتی سیاسی'}
        self.other13 = {'ق.ق': 'قابل قبول'}
        self.other14 = {'ق.ق.': 'قابل قبول'}
        self.other15 = {'غ.ق.ق': 'غیر قابل قبول'}
        self.other16 = {'غ.ق.ق.': 'غیر قابل قبول'}
        self.other17 = {'ن.م': 'نیرو‌های مسلح'}
        self.other18 = {'ن.م.': 'نیرو‌های مسلح'}
        self.other19 = {'پ.ت.ت': 'پست و تلگراف و تلفن'}
        self.other20 = {'پ.ت.ت.': 'پست و تلگراف و تلفن'}
        self.other21 = {'آ.ت.ت': 'آزمون تشریحی تکمیلی'}
        self.other22 = {'آ.ت.ت.': 'آزمون تشریحی تکمیلی'}
        self.other23 = {'ا.ا.ا': 'امداد اتومبیل ایران'}
        self.other24 = {'ا.ا.ا.': 'امداد اتومبیل ایران'}
        self.other25 = {'ب.ج': 'به کار برید به جای'}
        self.other26 = {'ب.ج.': 'به کار برید به جای'}
        self.other27 = {'ب.م.ا': 'بانک ملی ایران'}
        self.other28 = {'ب.م.ا.': 'بانک ملی ایران'}
        self.other29 = {'پ.ت.ت': 'پست و تلگراف و تلفن'}
        self.other30 = {'پ.ت.ت.': 'پست و تلگراف و تلفن'}
        self.other31 = {'ت.ت.ت': 'تاکسی تلفنی تهران'}
        self.other32 = {'ت.ت.ت.': 'تاکسی تلفنی تهران'}
        self.other33 = {'س.ج.ا.ا': 'سیمای جمهوری اسلامی ایران'}
        self.other34 = {'س.ج.ا.ا.': 'سیمای جمهوری اسلامی ایران'}
        self.other35 = {'ش.م.ا': 'شرکت مخابرات ایران'}
        self.other36 = {'ش.م.ا.': 'شرکت مخابرات ایران'}
        self.other37 = {'ش.ن.پ': 'شماره نظام پزشکی'}
        self.other38 = {'ش.ن.پ.': 'شماره نظام پزشکی'}
        self.other39 = {'ع.پ.خ.ب': 'علوم پزشکی و خدمات بهداشتی درمانی'}
        self.other40 = {'ک.م.م': 'کوچکترین مضرب مشترك'}
        self.other41 = {'ک.م.م.': 'کوچکترین مضرب مشترك'}
        self.other42 = {'ب.م.م': 'بزرگترین مضرب مشترك'}
        self.other43 = {'ق.ظ': 'قبل از ظهر'}
        self.other44 = {'ق.ظ.': 'قبل از ظهر'}
        self.other45 = {'ب.ظ': 'بعد از ظهر'}
        self.other46 = {'ب.ظ.': 'بعد از ظهر'}

        self.other_replaces = [
            self.other1, self.other2, self.other3, self.other4, self.other5, self.other6, self.other7, self.other8,
            self.other9, self.other10, self.other11, self.other12, self.other13, self.other14, self.other15,
            self.other16, self.other17, self.other18, self.other19, self.other20, self.other21, self.other22,
            self.other23, self.other24, self.other25, self.other26, self.other27, self.other28, self.other29,
            self.other30, self.other31, self.other32, self.other33, self.other34, self.other35, self.other36,
            self.other37, self.other38, self.other39, self.other40, self.other41, self.other42
        ]

        self.match_sound_replace = {
            "A": "آ ",
            "a": "آ ",
            "B": "بی ",
            "b": "بی ",
            "C": "سی ",
            "c": "سی ",
            "D": "دی ",
            "d": "دی ",
            "E": "ای ",
            "e": "ای ",
            "F": "اف ",
            "f": "اف ",
            "G": "جی ",
            "g": "جی ",
            "H": "اچ ",
            "h": "اچ ",
            "I": "آی ",
            "i": "آی ",
            "J": "جی ",
            "j": "جی ",
            "K": "کی ",
            "k": "کی ",
            "L": "ال ",
            "l": "ال ",
            "M": "ام ",
            "m": "ام ",
            "N": "ان ",
            "n": "ان ",
            "O": "او ",
            "o": "او ",
            "P": "پی ",
            "p": "پی ",
            "Q": "کیو ",
            "q": "کیو ",
            "R": "آر ",
            "r": "آر ",
            "S": "اس ",
            "s": "اس ",
            "T": "تی ",
            "t": "تی ",
            "U": "یو ",
            "u": "یو ",
            "V": "وی ",
            "v": "وی ",
            "W": "دبلیو ",
            "w": "دبلیو ",
            "X": "ایکس ",
            "x": "ایکس ",
            "Y": "وای ",
            "y": "وای ",
            "Z": "زد ",
            "z": "زد ",
        }

    def replace_date_abbreviation(self, sentence):
        for date_replace in self.date_replaces:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, date_replace.keys()))),
                              lambda m: date_replace[m.group()], sentence)
        return sentence

    def replace_persian_label_abbreviation(self, sentence):
        for persain_label_replace in self.persain_label_replaces:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, persain_label_replace.keys()))),
                              lambda m: persain_label_replace[m.group()], sentence)
        return sentence

    def replace_law_abbreviation(self, sentence):
        for law_replace in self.law_replaces:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, law_replace.keys()))),
                              lambda m: law_replace[m.group()], sentence)
        return sentence

    def replace_book_abbreviation(self, sentence):
        for book_replace in self.book_replaces:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, book_replace.keys()))),
                              lambda m: book_replace[m.group()], sentence)
        return sentence

    def replace_other_abbreviation(self, sentence):
        for other_replace in self.other_replaces:
            sentence = re.sub('({})'.format('|'.join(map(re.escape, other_replace.keys()))),
                              lambda m: other_replace[m.group()], sentence)
        return sentence

    def replace_English_abbrevations(self, sentence):
        pattern_one = r"\b[A-Za-z](?=([.]))(?:\1[A-Za-z])+\b"
        pattern_two = r'(?:[A-Za-z]\.)+'
        abbrevations_one = [x.group() for x in re.finditer(pattern_one, sentence)]
        abbrevations_two = re.findall(pattern_two, sentence)
        modified_abbrevations_one = copy.deepcopy(abbrevations_one)
        modified_abbrevations_two = copy.deepcopy(abbrevations_two)
        for index in range(len(abbrevations_one)):
            if len(modified_abbrevations_one[index]) > len(modified_abbrevations_two[index]):
                modified_abbrevations_one[index] = modified_abbrevations_one[index].replace(".", "")
                for char in modified_abbrevations_one[index]:
                    modified_abbrevations_one[index] = modified_abbrevations_one[index].replace(char,
                                                                                                self.match_sound_replace[
                                                                                                    char])
                sentence = sentence.replace(abbrevations_one[index], modified_abbrevations_one[index])

        abbrevations_two = re.findall(pattern_two, sentence)
        modified_abbrevations_two = copy.deepcopy(abbrevations_two)
        if abbrevations_two:
            for index in range(len(abbrevations_two)):
                modified_abbrevations_two[index] = modified_abbrevations_two[index].replace(".", "")
                for char in modified_abbrevations_two[index]:
                    modified_abbrevations_two[index] = modified_abbrevations_two[index].replace(char,
                                                                                                self.match_sound_replace[
                                                                                                    char])
            sentence = sentence.replace(abbrevations_two[index], modified_abbrevations_two[index])
        return sentence
