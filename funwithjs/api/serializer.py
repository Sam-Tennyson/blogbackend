from rest_framework import serializers
from .models import TopicList, QuestionList

class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicList
        fields = "__all__"

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionList
        fields = "__all__"