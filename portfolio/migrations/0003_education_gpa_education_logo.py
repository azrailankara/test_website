# Generated by Django 5.1.4 on 2024-12-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_experience_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='gpa',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Genel Akademik Not Ortalaması (GANO)', max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='education/'),
        ),
    ]
