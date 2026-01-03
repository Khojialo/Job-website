from django.contrib import admin
from .models import Category, Vacancy
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "views", "created", "updated", "category", "published", "get_image")
    list_display_links = ("title",)
    list_filter = ("category", "published")
    list_editable = ("category", 'published')
    search_fields = ("title", "description")
    readonly_fields = ('views',)
    # list_per_page = 2

    def get_image(self, obj: Vacancy):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60px">')
        return '-'

    get_image.short_description = "Rasmi"



