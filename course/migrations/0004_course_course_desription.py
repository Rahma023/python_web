# Generated by Django 3.2.3 on 2021-09-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_course_course_desription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_desription',
            field=models.TextField(null=True),
        ),
    ]
