# Generated by Django 2.1.7 on 2019-02-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clues',
            name='ques_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clues',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
