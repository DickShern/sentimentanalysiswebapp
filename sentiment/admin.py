from django.contrib import admin
from sentiment.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'sentiment', 'date')
    search_fields = ('review', 'sentiment')
    date_hierarchy = ('date')

admin.site.register(Review, ReviewAdmin)
