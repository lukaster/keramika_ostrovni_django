# Generated by Django 3.0.7 on 2020-06-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keramika_ostrovni_web', '0003_rozvrhdeti'),
    ]

    operations = [
        migrations.AddField(
            model_name='rozvrhdeti',
            name='cislo_krouzku',
            field=models.IntegerField(default=100),
        ),
    ]
