from django.contrib import admin
from profiles.models import Profile, ProfileProxy
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "nationality", "delete_action"]
    list_editable = [
        "gender",
    ]
    search_fields = ["name"]
    list_filter = ["gender"]
    actions = ["change_all_to_female"]

    def delete_action(self, obj):
        return format_html(
            '<a class="button" style="background-color:maroon;" href="{}">Delete</a>',
            reverse("soft_delete_profile", args=[obj.pk]),
        )

    delete_action.short_description = "delete"

    # JUST TEMPORARY. NEVER LOOP THROUGH QUERYSETS
    def change_all_to_female(self, request, queryset):
        queryset.update(gender="F")

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(deleted=False)

    def has_delete_permission(self, *args, **kwargs):
        return False


@admin.register(ProfileProxy)
class ProfileTrashAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "gender",
        "nationality",
        "recover_action",
        "hard_delete_action",
    ]
    list_editable = [
        "gender",
    ]
    search_fields = ["name"]
    list_filter = ["gender"]

    def recover_action(self, obj):
        return format_html(
            '<a class="button" style="background-color:green;" href="{}">Recover</a>',
            reverse("recover_profile", args=[obj.pk]),
        )

    recover_action.short_description = "recover"

    def hard_delete_action(self, obj):
        return format_html(
            '<a class="button" style="background-color:maroon;" href="{}">Hard Delete</a>',
            reverse("hard_delete", args=[obj.pk]),
        )

    hard_delete_action.short_description = "Delete"

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(deleted=True)

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False
