# Generated by Django 4.0.2 on 2022-03-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_book_details_read_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_details',
            name='book_image_org',
            field=models.ImageField(blank=True, default='\\student\\default\\profile.png', null=True, upload_to='student/books/'),
        ),
        migrations.AlterField(
            model_name='book_details',
            name='book_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
