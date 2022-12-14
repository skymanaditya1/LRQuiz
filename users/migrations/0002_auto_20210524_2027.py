# Generated by Django 3.2 on 2021-05-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age_hearing_loss',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, choices=[('No formal education', 'No formal education'), ('Primary education', 'Primary education'), ('Secondary education', 'Secondary education'), ('Vocational qualification', 'Vocational qualitifaction'), ("Bachelor's Degree", "Bachelor's Degree"), ("Master's Degree", "Master's Degreee"), ('Doctorate Degree', 'Doctorate Degree'), ('Others', 'Others')], default=None, help_text='Your highest level of education', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hearing_aid_type',
            field=models.CharField(choices=[('Hearing aid', 'Hearing aid'), ('Cochlearn implant', 'Cochlear implant'), ('No hearing aid', 'No hearing aid')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hearing_impairment_type',
            field=models.CharField(choices=[('Sensorineural', 'Sensorineural'), ('Conductive', 'Conductive'), ('Mixed', 'Mixed'), ('Others', 'Others')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hearing_loss_intensity',
            field=models.CharField(choices=[('Normal hearing (0-20 dB)', 'Normal hearing (0-20 db)'), ('Mild hearing loss (20-40 dB)', 'Mild hearing loss (20-40 dB)'), ('Moderate hearing loss (40-60 dB)', 'Moderate hearing loss (40-60 dB)'), ('Severe hearing loss (60-80 dB)', 'Severe hearing loss (60-80 dB)'), ('Severe-to-Profound hearing loss (80-90 dB)', 'Severe-to-Profound hearing loss (80-90 dB)'), ('Profound hearing loss (>90 dB)', 'Profound hearing loss (>90 dB)')], default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lipreading_expertise',
            field=models.CharField(choices=[('Beginner', 'Begineer'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='parents_education',
            field=models.CharField(blank=True, choices=[('No formal education', 'No formal education'), ('Primary education', 'Primary education'), ('Secondary education', 'Secondary education'), ('Vocational qualification', 'Vocational qualitifaction'), ("Bachelor's Degree", "Bachelor's Degree"), ("Master's Degree", "Master's Degreee"), ('Doctorate Degree', 'Doctorate Degree'), ('Others', 'Others')], default=None, help_text='Your parents highest level of education', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preferred_mode_of_communication',
            field=models.CharField(choices=[('Lipreading and speech', 'Lipreading and speech'), ('Sign language', 'Sign language'), ('Gestures', 'Gestures'), ('Others', 'Others')], default=None, max_length=30, null=True),
        ),
    ]
