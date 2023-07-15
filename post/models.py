from django.db import models
from account.models import User
from django.db.models import F


class Tag(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name    
    

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    body = models.TextField()
    view = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, blank=True, related_name="post")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created", "-view")

    def increase_view(self):
        self.view = F("view") + 1
        self.save()
        self.refresh_from_db()  

    def __str__(self) -> str:
        return f'post--{self.user}--{self.title}'
    

class Save(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saves")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="saves")    

    def __str__(self) -> str:
        return f"save--{self.user.username}--{self.post.title}"