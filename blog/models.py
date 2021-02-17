from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class categorys(models.Model):
    category_name = models.CharField(max_length=100)
    descreption = models.CharField(max_length=250)
    image = models.ImageField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_img = models.ImageField(upload_to='', null=True)
    date_post = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(categorys, on_delete=models.CASCADE)
    isPublish = models.BooleanField(default=False)

    def __str__(self):
        pass


class likes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes_count = models.IntegerField()

    def __str__(self):
        pass
        # ordering = []


class comment(models.Model):
    content = models.TextField()
    Publish_date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        pass
        # ordering = []


class report(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    report_date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
