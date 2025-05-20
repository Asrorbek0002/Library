from django.contrib import admin

from books.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'author', 'isbn')
    search_fields = ('author', 'subtitle')


