# Generated by Django 2.2.7 on 2019-11-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vanbang',
            options={'ordering': ['namcapbang']},
        ),
        migrations.RemoveField(
            model_name='vanbang',
            name='ngaycapbang',
        ),
        migrations.AddField(
            model_name='vanbang',
            name='namcapbang',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]