from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_boterrorlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopPrice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('label', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=100)),
                ('price', models.BigIntegerField()),
                ('currency', models.CharField(max_length=30)),
                ('sort_order', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'shop_prices',
                'managed': False,
            },
        ),
    ]
