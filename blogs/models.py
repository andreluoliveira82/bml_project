from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title