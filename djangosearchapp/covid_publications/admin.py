from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'authors', 'journal', 'study')
	list_filter = ('reference', 'covidence_harsh', 'published_year', 'authors')
	search_fields = ('title', 'abstract')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('authors',)
	ordering = ('reference', 'published_year')