from django.db import models
from django.conf import settings


# parent model
class forum(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.title)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)
