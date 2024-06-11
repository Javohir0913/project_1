# Generated by Django 5.0.6 on 2024-06-11 15:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_title', models.CharField(max_length=255)),
                ('submission_description', models.TextField()),
                ('submission_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('submission_discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Submission Fee',
                'verbose_name_plural': 'Submission Fees',
                'db_table': 'submission_fee',
            },
        ),
    ]
