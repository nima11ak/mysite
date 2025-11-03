from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()


    #tag
    #category

    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    created_date = models.DateTimeField(null=True)
    published_date = models. DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



    class Meta:
        ordering =['created_date']
        verbose_name = 'POST'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

