# Generated by Django 4.1 on 2022-08-08 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Debtor', '0009_debtor_debtor_image_alter_post_deptors_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
