from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    """
    This is how to display Post model in admin
    """

    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = [
        "title",
        "author",
        "status",
        "published_date",
        "created_date",
    ]
    list_filter = [
        "status",
        "author",
        "published_date",
    ]
    ordering = [
        "-published_date",
    ]
    search_fields = [
        "title",
        "content",
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
