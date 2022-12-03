from django.db import models

# Create your models here.
class TopicList(models.Model):
    name = models.CharField(max_length=80, blank=False)
    description = models.CharField(max_length=500, blank=False)

    class Meta:
        verbose_name_plural = "Topic List"

    def __str__(self):
        return self.name

class QuestionList(models.Model):
    name = models.CharField(max_length=50)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="picture/",max_length=254)
    topic_id = models.ForeignKey(TopicList, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Question List"

    def __str__(self):
        return self.name