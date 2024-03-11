from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_short_text(self, SHORT_TEXT_LEN=50):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text