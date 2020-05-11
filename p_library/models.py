from django.db import models


# Create your models here.


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class PublishingHouse(models.Model):
    name = models.TextField()
    year_of_foundation = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey("p_library.Author", on_delete=models.CASCADE,
                               related_name="book_author")
    publishing_house = models.ForeignKey("p_library.PublishingHouse", on_delete=models.CASCADE, related_name="house")
    is_lend_out = models.BooleanField(blank=True, default=False)
    whom_lend_out = models.ForeignKey("p_library.Friend", on_delete=models.CASCADE, related_name="name_of_friend", blank=True, default=1)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.title


class Friend(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
