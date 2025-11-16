import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Question, Answer

@pytest.mark.django_db
def test_create_question():
    client = APIClient()
    response = client.post(reverse('question-list'), {'text': 'Test question'})
    assert response.status_code == status.HTTP_201_CREATED
    assert Question.objects.count() == 1

@pytest.mark.django_db
def test_create_answer():
    question = Question.objects.create(text='Test question')
    client = APIClient()
    response = client.post(reverse('answers', kwargs={'question_id': question.id}), {'text': 'Test answer'})
    assert response.status_code == status.HTTP_201_CREATED
    assert Answer.objects.count() == 1
