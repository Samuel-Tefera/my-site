from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    explicit = models.TextField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
      
      
class Comments(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    comment_text = models.TextField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


class Like(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Likes')
    