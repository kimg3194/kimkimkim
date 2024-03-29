# Generated by Django 2.2.1 on 2019-05-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cau_quiz', '0002_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='photo',
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default='marker102', max_length=10),
        ),
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='status',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]
