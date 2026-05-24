from django import forms
from django.contrib import admin

from .models import GroupOwner, GroupStatsLink, UserProfileLink


@admin.register(GroupStatsLink)
class GroupStatsLinkAdmin(admin.ModelAdmin):
    list_display = ("chat", "token", "expires_at", "created_at")
    search_fields = ("chat__title", "chat__chat_id", "token")
    list_filter = ("created_at", "expires_at")


@admin.register(UserProfileLink)
class UserProfileLinkAdmin(admin.ModelAdmin):
    list_display = ("user", "token", "expires_at", "created_at")
    search_fields = ("user__full_name", "user__user_id", "token")
    list_filter = ("created_at", "expires_at")


class GroupOwnerAdminForm(forms.ModelForm):
    raw_password = forms.CharField(
        label="Login parol",
        required=False,
        widget=forms.PasswordInput(render_value=False),
        help_text="Yangi parol berish yoki parolni almashtirish uchun to'ldiring.",
    )

    class Meta:
        model = GroupOwner
        fields = ("user", "chat", "login", "raw_password", "is_active")

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and not cleaned_data.get("raw_password"):
            raise forms.ValidationError("Yangi GroupOwner uchun parol kiritish kerak.")
        return cleaned_data

    def save(self, commit=True):
        owner = super().save(commit=False)
        raw_password = self.cleaned_data.get("raw_password")
        if raw_password:
            owner.set_password(raw_password)
        if commit:
            owner.save()
            self.save_m2m()
        return owner


@admin.register(GroupOwner)
class GroupOwnerAdmin(admin.ModelAdmin):
    form = GroupOwnerAdminForm
    list_display = ("login", "user", "chat", "is_active", "updated_at")
    list_filter = ("is_active", "created_at", "updated_at")
    search_fields = ("login", "user__full_name", "user__user_id", "chat__title", "chat__chat_id")
    autocomplete_fields = ("user", "chat")

    def get_readonly_fields(self, request, obj=None):
        return ("created_at", "updated_at") if obj else ()
