# Generated by Django 3.1.7 on 2021-05-02 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('balance', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField()),
                ('total_price', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'در حال خرید'), (2, 'ثبت شده'), (3, 'لغو شده'), (4, 'ارسال شده')])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('inventory', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.product')),
            ],
        ),
    ]