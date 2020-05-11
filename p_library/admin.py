from django.contrib import admin
from p_library.models import Book, Friend
from p_library.models import Author, PublishingHouse

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    actions = ('year_release', 'author', 'price')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    actions = 'birth_year'


@admin.register(PublishingHouse)
class PublisherHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass
