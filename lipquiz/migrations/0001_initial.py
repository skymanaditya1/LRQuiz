# Generated by Django 3.2 on 2021-05-21 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=256)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='Duration of the quiz')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6)),
                ('quiz_type', models.CharField(choices=[('single word mcq', 'single word mcq'), ('single word blank with context', 'single word blank with context'), ('sentence with context', 'sentence with context'), ('sentence with blank', 'sentence with blank')], max_length=120)),
                ('score_required_to_pass', models.IntegerField(help_text='Minimum score required to pass the quiz')),
            ],
            options={
                'verbose_name_plural': 'VideoQuizzes',
            },
        ),
    ]
