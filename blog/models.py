from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True)
    explicit = models.TextField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
      
      
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
