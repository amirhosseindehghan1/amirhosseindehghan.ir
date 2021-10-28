from django.contrib import admin
from .models import HeaderMenu, SlideSetting, AboutmeSetting, SkillSetting, EducationSetting, ExperienceSetting, PortfolioSetting,\
    ContactMe
# Register your models here.

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'copy_right', 'twitter', 'instagram', 'linkedin', 'github']
    list_editable = ['copy_right', 'twitter', 'instagram', 'linkedin', 'github']

class HeaderMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'home', 'home_link', 'about', 'about_link', 'skill', 'skill_link', 'resume', 'resume_link', 'portfolio',
                    'portfolio_link', 'contact', 'contact_link']
    list_editable = ['home', 'home_link', 'about', 'about_link', 'skill', 'skill_link', 'resume', 'resume_link', 'portfolio',
                    'portfolio_link', 'contact', 'contact_link']




class SlideSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'text1', 'text2', 'text3']

class AboutmeSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'text1', 'text2', 'fullname', 'age', 'experience', 'country', 'city', 'email']
    list_editable = ['text1', 'text2', 'fullname', 'age', 'experience', 'country', 'city', 'email']

class SkillSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'svg', 'width', 'width_px_percent', 'height', 'height_px_percent']
    list_editable = ['title', 'description', 'width', 'width_px_percent', 'height', 'height_px_percent']


class EducationSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'description']
    list_editable = ['title', 'date', 'description']


class ExperienceSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'description']
    list_editable = ['title', 'date', 'description']


class PortfolioSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'svg', 'width', 'width_px_percent', 'height', 'height_px_percent']
    list_editable = ['title', 'description', 'width', 'width_px_percent', 'height', 'height_px_percent']


class ContactMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'subject', 'text']
    search_fields = ['fullname', 'email', 'subject']


admin.site.register(ContactMe, ContactMeAdmin)
admin.site.register(PortfolioSetting, PortfolioSettingAdmin)
admin.site.register(ExperienceSetting, ExperienceSettingAdmin)
admin.site.register(EducationSetting, EducationSettingAdmin)
admin.site.register(SkillSetting, SkillSettingAdmin)
admin.site.register(AboutmeSetting, AboutmeSettingAdmin)
admin.site.register(SlideSetting, SlideSettingAdmin)
admin.site.register(HeaderMenu, HeaderMenuAdmin)