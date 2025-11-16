from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at', 'answers']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user_id', 'text', 'created_at']
