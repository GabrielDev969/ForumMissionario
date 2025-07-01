from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='post_images/', verbose_name="Featured Image", blank=True, null=True)
    content = RichTextField(verbose_name="Content")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title