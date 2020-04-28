from django.db import models


class Topic(models.Model):
    # p.399
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # p.399
        return self.text
