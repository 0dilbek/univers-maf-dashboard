# Generated for unmanaged transfers table state.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_transfer_chat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='caption',
        ),
    ]
