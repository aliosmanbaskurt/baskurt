# Generated by Django 3.2.16 on 2022-10-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0004_course_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_icon',
            field=models.CharField(default='bi bi-pc-display', max_length=200, null=True),
        ),
    ]
