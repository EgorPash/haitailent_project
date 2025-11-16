from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # Каскадное удаление ответов
        return Response(status=status.HTTP_204_NO_CONTENT)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question_id = self.kwargs.get('question_id')
        serializer.save(question_id=question_id)
