import uuid

from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone

from bot.models import Chat, User


class GroupStatsLink(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"Link for {self.chat.title} (Expires: {self.expires_at})"


class UserProfileLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"Profile link for {self.user} (Expires: {self.expires_at})"


class GroupOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_groups")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="owners")
    login = models.CharField(max_length=120, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("user", "chat"),)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        status = "active" if self.is_active else "inactive"
        return f"{self.login} - {self.chat.title} ({status})"
