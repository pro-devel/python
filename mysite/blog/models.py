from django.db import models


# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.CharField(max_length=15000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title


class Category(models.Model):
    category_title = models.CharField(max_length=200)
    question = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_title
