# Generated for unmanaged transfers table state.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_groupincome_vipchats'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='chat_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
