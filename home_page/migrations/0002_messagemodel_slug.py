# Generated by Django 4.1.4 on 2023-07-20 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL), unique=True),
        ),
    ]
