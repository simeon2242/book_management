from django.db import models



# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=20,unique=True)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    pages = models.IntegerField()
    published = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

class Author(models.Model):
    full_name = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name