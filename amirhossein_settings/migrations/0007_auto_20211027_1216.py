# Generated by Django 3.2.8 on 2021-10-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amirhossein_settings', '0006_portfoliosetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=30, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=30, verbose_name='موضوع')),
                ('text', models.CharField(max_length=500, verbose_name='متن پیام')),
            ],
            options={
                'verbose_name': 'تنظیمات تماس با من',
                'verbose_name_plural': 'مدیریت تنظیمات تماس با من',
            },
        ),
        migrations.AlterModelOptions(
            name='portfoliosetting',
            options={'verbose_name': 'تنظیمات نمونه کارها', 'verbose_name_plural': 'مدیریت تنظیمات نمونه کارها'},
        ),
    ]