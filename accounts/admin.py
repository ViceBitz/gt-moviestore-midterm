from django.contrib import admin
from django.db.models import Count
from accounts.models import TopCommenter
from movies.models import Review

class TopCommenterAdmin(admin.ModelAdmin):
    list_display = ["username", "number_of_comments"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(Count("review")).order_by("-review__count")

    @admin.display(empty_value = "???")
    def number_of_comments(self, obj):
        return obj.review__count

# Register your models here.
admin.site.register(TopCommenter, TopCommenterAdmin)
