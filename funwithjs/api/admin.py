from django.contrib import admin
from .models import TopicList, QuestionList

# Register your models here.
@admin.register(TopicList)
class TopicListAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]

@admin.register(QuestionList)
class QuestionListAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "answer", "photo", 'topic_id']