from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_img/', blank=True, default='profile_img/profile.png', verbose_name="Picture:")
    about_me = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)


class categorys(models.Model):
    category_name = models.CharField(max_length=100)
    descreption = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='category_img/',
                              blank=True, default='category_img/category.png')

    def __str__(self):
        return self.category_name


cases = [('notPublished', 'notPublished'),
         ('published', 'published'), ('refused', 'refused')]

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Post Title")
    content = RichTextField(blank=True, null=True, verbose_name="Post Content:")
    post_img = models.ImageField(
        upload_to='post_img/', blank=True, default='post_img/test.png', verbose_name="Post Header:")
    date_post = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    category_id = models.ForeignKey(categorys, on_delete=models.CASCADE, verbose_name="Post Category")
    isPublish = models.CharField(max_length=255,choices=cases, default='notPublished')
    likes = models.ManyToManyField(User, related_name='like', blank=True)
    
    def like_count(self):
        return self.likes.count()
           

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
    is_archived = models.BooleanField(default=False)
