from django.contrib import admin
from .models import Author, Entry, Category
# Register your models here.

class EntryInLine(admin.TabularInline):
	model = Entry

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name','age','birth_date', 'slug')
	inlines = [ EntryInLine, ]

class EntryFilter(admin.SimpleListFilter):

	title = 'Mayores de Edad'
	parameter_name = 'Edad'
	
	def lookups(self, request, model_admin):
		return (
			( '+18' , ('Mayores de Edad')),
			( '-18' , ('Menores de Edad')),
			)

	def queryset(self, request, queryset):
		if self.value() == '+18':
			return queryset.filter(author__age__gte = 18)
		if self.value() == '-18':
			return queryset.filter(author__age__lt = 18)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'published')
	list_display_links = ( 'title',)
	filter_vertical = ('category',)
	list_filter = ('author__age', EntryFilter)
	list_editable = ('author',)
	actions = ['make_published']

	def make_published(self, request, queryset):
		return queryset.update(published = True)
	make_published.short_description = 'Cambiar a publicado'