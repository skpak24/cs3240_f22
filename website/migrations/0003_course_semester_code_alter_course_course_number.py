# Generated by Django 4.1.1 on 2022-10-16 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_book_condition_book_image_book_price_book_version_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.IntegerField(),
        ),
    ]