# Generated by Django 2.2.12 on 2020-04-22 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_datamodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='fcfvz',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_fcfvz', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='ms',
            field=models.ManyToManyField(blank=True, related_name='customtext_ms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sdfe',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sfdf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_sfdf', to='home.DataModel'),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='cc',
            field=models.ManyToManyField(blank=True, related_name='datamodel_cc', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='sdf',
            field=models.ManyToManyField(blank=True, related_name='datamodel_sdf', to='home.CustomText'),
        ),
    ]
