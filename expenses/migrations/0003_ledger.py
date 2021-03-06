# Generated by Django 2.2.7 on 2019-11-14 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0002_auto_20191113_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payments_made', to=settings.AUTH_USER_MODEL)),
                ('payment_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payments_owed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
