from django.db import models

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    # photo = models.ImageField(blank=True, upload_to='insta/post/%Y/%m/%d')
    # tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # is_public = models.BooleanField(default=False, verbose_name="공개여부")
