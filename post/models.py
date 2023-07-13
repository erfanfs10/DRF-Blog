from django.db import models
from account.models import User
from django.db.models import F


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    body = models.TextField()
    view = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created", "-view", "-updated")

    def increace_view(self):
        self.view = F("view") + 1
        self.save()
        self.refresh_from_db()  

    def __str__(self):
        return f'post--{self.user}--{self.title}'
    

class Tag(models.Model):

    name = models.CharField(max_length=255)
    post = models.ManyToManyField(Post, related_name='tags', blank=True)

    def __str__(self):
        return self.name    