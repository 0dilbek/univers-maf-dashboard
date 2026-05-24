import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
        ("bot", "0005_xcoinwallet"),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupOwner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("login", models.CharField(max_length=120, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("chat", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="owners", to="bot.chat")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="owned_groups", to="bot.user")),
            ],
            options={
                "unique_together": {("user", "chat")},
            },
        ),
    ]
