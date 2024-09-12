# Generated by Django 5.1.1 on 2024-09-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('1Б', '1Б'), ('2А', '2А'), ('3Б', '3Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Осень'),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('1Б', '1Б'), ('2А', '2А'), ('3Б', '3Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Весна'),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('1Б', '1Б'), ('2А', '2А'), ('3Б', '3Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Лето'),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('1Б', '1Б'), ('2А', '2А'), ('3Б', '3Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Зима'),
        ),
    ]
