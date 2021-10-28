import alert as alert
from django.shortcuts import render, redirect
from amirhossein_settings.models import SiteSetting, HeaderMenu, SlideSetting, AboutmeSetting, SkillSetting, EducationSetting, ExperienceSetting,\
    PortfolioSetting, ContactMe
from amirhossein_settings.forms import CreateContactForm
from django.contrib import messages

# Behind Header Coede
def header(request, *args, **kwargs):
    header_setting = HeaderMenu.objects.first()
    site_setting = SiteSetting.objects.first()
    slide_setting = SlideSetting.objects.first()
    context = {
        'header_setting' : header_setting,
        'slide_setting' : slide_setting,
        'setting' : site_setting
    }

    return render(request, 'shared/Header.html', context)

# Behind Footer Code
def footer(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting' : site_setting
    }
    return render(request, 'shared/Footer.html', context)


# Home Page Code
def home(request):
    aboutme_setting = AboutmeSetting.objects.first()
    skill_setting = SkillSetting.objects.all()
    education_setting = EducationSetting.objects.all()
    experience_setting = ExperienceSetting.objects.all()
    portfolio_setting = PortfolioSetting.objects.all()
    contactme_setting = CreateContactForm(request.POST or None)
    if contactme_setting.is_valid():
        fullname = contactme_setting.cleaned_data.get('fullname')
        email = contactme_setting.cleaned_data.get('email')
        subject = contactme_setting.cleaned_data.get('subject')
        text = contactme_setting.cleaned_data.get('text')
        ContactMe.objects.create(fullname=fullname, email=email, subject=subject, text=text)
        contactme_setting = CreateContactForm()
        messages.success(request, "پیام شما با موفقیت ارسال شد. به زودی بررسی خواهم کرد :)")

    context = {
        'aboutme_setting': aboutme_setting,
        'skill_setting': skill_setting,
        'education_setting': education_setting,
        'experience_setting': experience_setting,
        'portfolio_setting': portfolio_setting,
        'contactme_setting': contactme_setting,


    }
    return render(request, 'index.html', context)