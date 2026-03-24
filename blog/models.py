from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    '''プロパティの設定'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''公開日時の設定'''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return self.title
