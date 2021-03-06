# Generated by Django 2.2.5 on 2020-05-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumb',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='article',
            name='image_2',
            field=models.FileField(blank=True, default='default.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='image_3',
            field=models.FileField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
