import os
from django.db import models
from django.core.validators import FileExtensionValidator

    # Start  Upload Images
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def images(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    return final_name

    # End Upload Images

    # Start Social Media Link Settings
class SiteSetting(models.Model):
    copy_right = models.CharField(max_length=150, verbose_name='حق کپی رایت', null=False)
    twitter = models.CharField(max_length=150, verbose_name='لینک توییتر', null=False)
    instagram = models.CharField(max_length=150, verbose_name='لینک اینستاگرام', null=False)
    linkedin = models.CharField(max_length=150, verbose_name='لینک لینکدین', null=False)
    github = models.CharField(max_length=150, verbose_name='لینک گیت هاب', null=False)

    class Meta:
        verbose_name = 'تنظیمات انتهای سایت'
        verbose_name_plural = 'مدیریت تنظیمات لینک شبکه های اجتماعی'

    def __str__(self):
        return self.copy_right

    # End Social Media Link Settings

    # Start Header Settings
class HeaderMenu(models.Model):
    home = models.CharField(max_length=150, verbose_name='نام صفحه', null=False)
    home_link = models.CharField(max_length=150, verbose_name='لینک صفحه', null=False)
    about = models.CharField(max_length=150, verbose_name='نام صفحه', null=False)
    about_link = models.CharField(max_length=150, verbose_name='لینک صفحه', null=False)
    skill = models.CharField(max_length=150, verbose_name='نام صفحه', null=False)
    skill_link = models.CharField(max_length=150, verbose_name='لینک صفحه', null=False)
    resume = models.CharField(max_length=150, verbose_name='نام صفحه', null=False)
    resume_link = models.CharField(max_length=150, verbose_name='لینک صفحه', null=False)
    portfolio = models.CharField(max_length=150, verbose_name='نام صفحه', null=False)
    portfolio_link = models.CharField(max_length=150, verbose_name='لینک صفحه', null=False)
    contact = models.CharField(max_length=150, verbose_name='نام صفحه', null=False)
    contact_link = models.CharField(max_length=150, verbose_name='لینک صفحه', null=False)

    class Meta:
        verbose_name = 'تنظیمات هدر و منوی سایت'
        verbose_name_plural = 'مدیریت تنظیمات هدر و منوی سایت'

    def __str__(self):
        return self.home

    # End Header Settings

    # Start Silde Settings
class SlideSetting(models.Model):
    text1 = models.CharField(max_length=150, verbose_name='متن اول', null=False)
    text2 = models.CharField(max_length=150, verbose_name='متن دوم', null=False)
    text3 = models.CharField(max_length=150, verbose_name='متن سوم', null=False)

    class Meta:
        verbose_name = 'تنظیمات اسلاید'
        verbose_name_plural = 'مدیریت تنظیمات اسلاید'

    def __str__(self):
        return self.text1

    # End Slide Settings

    # Start About me Settings
class AboutmeSetting(models.Model):
    text1 = models.CharField(max_length=150, verbose_name='متن اول', null=False)
    text2 = models.CharField(max_length=1000, verbose_name='متن دوم', null=False)
    fullname = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی', null=False)
    age = models.CharField(max_length=150, verbose_name='سن', null=False)
    experience = models.CharField(max_length=150, verbose_name='تجربه', null=False)
    country = models.CharField(max_length=150, verbose_name='کشور', null=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    city = models.CharField(max_length=150, verbose_name='شهر', null=False)
    email = models.CharField(max_length=150, verbose_name='ایمیل', null=False)

    class Meta:
        verbose_name = 'تنظیمات درباره ی من'
        verbose_name_plural = 'مدیریت تنظیمات درباره ی من'

    def __str__(self):
        return self.text1

    # End About me Settings

    # Start Skill Settings
class SkillSetting(models.Model):

    title = models.CharField(max_length=150, verbose_name='عنوان مهارت', null=False)
    description = models.CharField(max_length=150, verbose_name='توضیحات مهارت', null=False)
    svg = models.FileField(upload_to='images', verbose_name='فایل svg',validators=[FileExtensionValidator(['svg'])], null=False, default=False)
    width = models.CharField(max_length=5, verbose_name='طول svg', null=True)
    width_px_percent = models.CharField(max_length=2, verbose_name='اندازه بر اساس px یا %', null=True)
    height = models.CharField(max_length=5, verbose_name='ارتفاع svg', null=True)
    height_px_percent = models.CharField(max_length=2, verbose_name='اندازه بر اساس px یا %', null=True)


    class Meta:
        verbose_name = 'تنظیمات مهارت ها'
        verbose_name_plural = 'مدیریت تنظیمات مهارت ها'

    def __str__(self):
        return self.title
# End Skill Setting

# Start Education Setting
class EducationSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان', null=True)
    date = models.CharField(max_length=150, verbose_name='بازه زمانی', null=True)
    description = models.CharField(max_length=850, verbose_name='توضیحات', null=True)

    class Meta:
        verbose_name = 'تنظیمات تحصیلات'
        verbose_name_plural = 'مدیریا تنظیمات تحصیلات'

    def __str__(self):
        return self.title
# End Edication Setting

# Start Experience Setting
class ExperienceSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان', null=True)
    date = models.CharField(max_length=150, verbose_name='بازه زمانی', null=True)
    description = models.CharField(max_length=850, verbose_name='توضیحات', null=True)

    class Meta:
        verbose_name = 'تنظیمات تجربه‌ها'
        verbose_name_plural = 'مدیریت تنظیمات تجربه‌ها'

    def __str__(self):
        return self.title
# End Experience Setting

# Start Portfolio
class PortfolioSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان پروژه', null=False)
    description = models.CharField(max_length=150, verbose_name='توضیحات پروژه', null=False)
    svg = models.FileField(upload_to='images', verbose_name='فایل svg', validators=[FileExtensionValidator(['svg'])],null=False, default=False)
    width = models.CharField(max_length=5, verbose_name='طول svg', null=True)
    width_px_percent = models.CharField(max_length=2, verbose_name='اندازه بر اساس px یا %', null=True)
    height = models.CharField(max_length=5, verbose_name='ارتفاع svg', null=True)
    height_px_percent = models.CharField(max_length=2, verbose_name='اندازه بر اساس px یا %', null=True)

    class Meta:
        verbose_name = 'تنظیمات نمونه کارها'
        verbose_name_plural = 'مدیریت تنظیمات نمونه کارها'
    def __str__(self):
        return self.title
# End Portfolio

# Start ContactMe
class ContactMe(models.Model):
    fullname = models.CharField(max_length=30, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=30, verbose_name='ایمیل')
    subject = models.CharField(max_length=30, verbose_name='موضوع')
    text = models.CharField(max_length=500, verbose_name='متن پیام')

    class Meta:
        verbose_name = 'تنظیمات تماس با من'
        verbose_name_plural = 'مدیریت تماس با من'

    def __str__(self):
        return self.subject