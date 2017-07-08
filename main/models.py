from django.db import models


class Card(models.Model):
    word = models.CharField(max_length=500)
    en_meaning = models.CharField(max_length=500)
    ru_meaning = models.CharField(max_length=500)
    example = models.CharField(max_length=500)
    extra_info = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __repr__(self):
        return '<Card: word=%s en_meaning=%s ru_meaning=%s>' % (self.word, 
            self.en_meaning, self.ru_meaning)

    def __str__(self):
        return self.word

        
# Create your models here.
