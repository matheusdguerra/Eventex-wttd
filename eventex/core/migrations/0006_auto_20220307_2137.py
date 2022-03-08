# Generated by Django 3.2.9 on 2022-03-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_talk'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'verbose_name': 'Palestra', 'verbose_name_plural': 'Palestras'},
        ),
        migrations.AlterField(
            model_name='talk',
            name='description',
            field=models.TextField(blank=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='start',
            field=models.TimeField(blank=True, null=True, verbose_name='início'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(max_length=200, verbose_name='título'),
        ),
    ]
