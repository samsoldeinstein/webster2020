# Generated by Django 3.1.2 on 2020-10-02 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0001_initial'),
        ('subscribe', '0002_auto_20201002_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('subscription_id', models.AutoField(primary_key=True, serialize=False)),
                ('end_date', models.DateTimeField()),
                ('sub_plan_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscribe.subscriptionplan')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.transactiondetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
