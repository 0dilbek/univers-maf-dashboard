# Generated for unmanaged bot error log table state.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_xcoinwallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotErrorLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('exception_type', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('short_message', models.CharField(blank=True, default='', max_length=500)),
                ('update_id', models.BigIntegerField(blank=True, null=True)),
                ('update_type', models.CharField(blank=True, max_length=50, null=True)),
                ('chat_id', models.BigIntegerField(blank=True, null=True)),
                ('chat_type', models.CharField(blank=True, max_length=50, null=True)),
                ('chat_title', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('user_full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('function', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.TextField(blank=True, null=True)),
                ('line', models.IntegerField(blank=True, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('request_text', models.TextField(blank=True, null=True)),
                ('callback_data', models.TextField(blank=True, null=True)),
                ('request_summary', models.TextField(blank=True, null=True)),
                ('request_info', models.TextField(blank=True, null=True)),
                ('traceback', models.TextField()),
                ('update_json', models.JSONField(blank=True, null=True)),
                ('update_repr', models.TextField(blank=True, null=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bot_error_logs',
                'ordering': ['-created_at'],
                'managed': False,
            },
        ),
    ]
