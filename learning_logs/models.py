from django.db import models


class Topic(models.Model):
    # p.399
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # p.399
        return self.text


class Entry(models.Model):
    # p.404
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # p.404
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        return self.text
