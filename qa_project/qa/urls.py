from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'questions/(?P<question_id>[^/.]+)/answers', AnswerViewSet, basename='answers')

urlpatterns = [
    path('', include(router.urls)),
]
