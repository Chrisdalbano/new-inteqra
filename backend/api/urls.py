# backend/api/urls.py

from django.urls import path
from .views import (
    list_quizzes,
    create_quiz,
    quiz_detail,
    question_detail,
    create_question,
)

urlpatterns = [
    path("quizzes/", list_quizzes, name="list_quizzes"),
    path("create-quiz/", create_quiz, name="create_quiz"),
    path("quizzes/<int:quiz_id>/", quiz_detail, name="quiz_detail"),
    path(
        "questions/<int:question_id>/", question_detail, name="question_detail"
    ),  # Handles PUT, DELETE for questions
    path(
        "quizzes/<int:quiz_id>/questions/", create_question, name="create_question"
    ),  # Handles POST for new questions
]
