from django.db import models
# from django.contrib.auth.models import Author


# One Author can write many Books
class Author(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name


# One Book can be written by many Authors
class Book(models.Model):
    title = models.CharField( max_length=50)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    #
    # def author(self):
    #     return self.book.author



