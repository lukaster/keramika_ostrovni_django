# Generated by Django 3.0.7 on 2020-06-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keramika_ostrovni_web', '0007_auto_20200610_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontaktinfo',
            name='email',
            field=models.EmailField(default='auth.User', max_length=254),
        ),
    ]
