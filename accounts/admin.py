from django.contrib import admin
from .models import (
    CustomUser,
    CustomUserProfile,
    Guide,
    Tourist,
    EventManager,
    Tour,
    TouristCompletedTour,
    Event,
    EventCompleted,
    GuideRating,
    EventManagerRating,
)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active", "is_superuser")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "username", "pfp")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)


class CustomUserProfileAdmin(admin.ModelAdmin):
    model = CustomUserProfile
    list_display = ("user", "is_guide", "is_event_manager")
    list_filter = ("is_guide", "is_event_manager")
    search_fields = (
        "user__email",
        "user__username",
        "user__first_name",
        "user__last_name",
    )


class GuideAdmin(admin.ModelAdmin):
    model = Guide
    list_display = ("user_profile", "num_tourists_handled", "average_rating")
    search_fields = (
        "user_profile__user__email",
        "user_profile__user__username",
        "user_profile__user__first_name",
        "user_profile__user__last_name",
    )


class TouristAdmin(admin.ModelAdmin):
    model = Tourist
    list_display = ("user_profile",)
    search_fields = (
        "user_profile__user__email",
        "user_profile__user__username",
        "user_profile__user__first_name",
        "user_profile__user__last_name",
    )


class EventManagerAdmin(admin.ModelAdmin):
    model = EventManager
    list_display = ("user_profile", "num_of_events", "average_rating")
    search_fields = (
        "user_profile__user__email",
        "user_profile__user__username",
        "user_profile__user__first_name",
        "user_profile__user__last_name",
    )


class TourAdmin(admin.ModelAdmin):
    model = Tour
    list_display = ("title", "guide", "start_date", "end_date")
    search_fields = (
        "title",
        "guide__user_profile__user__email",
        "guide__user_profile__user__username",
        "guide__user_profile__user__first_name",
        "guide__user_profile__user__last_name",
    )


class TouristCompletedTourAdmin(admin.ModelAdmin):
    model = TouristCompletedTour
    list_display = ("tourist", "tour", "guide", "completed_at")
    search_fields = (
        "tourist__user_profile__user__email",
        "tourist__user_profile__user__username",
        "tourist__user_profile__user__first_name",
        "tourist__user_profile__user__last_name",
        "tour__title",
        "guide__user_profile__user__first_name",
        "guide__user_profile__user__last_name",
    )


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("title", "event_manager", "start_date", "end_date")
    search_fields = (
        "title",
        "event_manager__user_profile__user__email",
        "event_manager__user_profile__user__username",
        "event_manager__user_profile__user__first_name",
        "event_manager__user_profile__user__last_name",
    )


class EventCompletedAdmin(admin.ModelAdmin):
    model = EventCompleted
    list_display = ("tourist", "event", "event_manager", "completed_at")
    search_fields = (
        "tourist__user_profile__user__email",
        "tourist__user_profile__user__username",
        "tourist__user_profile__user__first_name",
        "tourist__user_profile__user__last_name",
        "event__title",
        "event_manager__user_profile__user__first_name",
        "event_manager__user_profile__user__last_name",
    )


class GuideRatingAdmin(admin.ModelAdmin):
    model = GuideRating
    list_display = ("guide", "tourist", "value")
    search_fields = (
        "guide__user_profile__user__email",
        "guide__user_profile__user__username",
        "guide__user_profile__user__first_name",
        "guide__user_profile__user__last_name",
        "tourist__user_profile__user__email",
        "tourist__user_profile__user__username",
        "tourist__user_profile__user__first_name",
        "tourist__user_profile__user__last_name",
    )


class EventManagerRatingAdmin(admin.ModelAdmin):
    model = EventManagerRating
    list_display = ("eventmanager", "tourist", "value")
    search_fields = (
        "eventmanager__user_profile__user__email",
        "eventmanager__user_profile__user__username",
        "eventmanager__user_profile__user__first_name",
        "eventmanager__user_profile__user__last_name",
        "tourist__user_profile__user__email",
        "tourist__user_profile__user__username",
        "tourist__user_profile__user__first_name",
        "tourist__user_profile__user__last_name",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserProfile, CustomUserProfileAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Tourist, TouristAdmin)
admin.site.register(EventManager, EventManagerAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(TouristCompletedTour, TouristCompletedTourAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventCompleted, EventCompletedAdmin)
admin.site.register(GuideRating, GuideRatingAdmin)
admin.site.register(EventManagerRating, EventManagerRatingAdmin)
