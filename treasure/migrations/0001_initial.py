# Generated by Django 2.1.7 on 2019-02-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clues',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('prev_ans', models.CharField(blank=True, max_length=50, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('ans', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
