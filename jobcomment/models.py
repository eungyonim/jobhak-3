from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

Category_select = (
    ('공지', '공지'),
    ('정치', '정치'),
    ('사회', '사회'),
    ('경제', '경제'),
    ('IT','IT'),
    ('과학','과학'),
)

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    category = models.CharField(max_length=20, choices = Category_select, default = '상식')
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    like = models.ManyToManyField(User, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)

    def summary(self):
        return self.body[:10]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):

        return self.title

class Comment(models.Model):
    post = models.ForeignKey('jobcomment.Blog', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200, null=False, blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Login(models.Model):
    login_title = models.CharField(max_length=200)