from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.getRoute),
    path('login/',views.login),
    path('signup/',views.signup),
    path('test/',views.test_token),
    path('liststudent/',views.ListStudent.as_view()),
    path('createstudent/',views.CreateStudent.as_view()),
    path('loginstudent/',views.LoginStudent.as_view()),
    path('student/<int:pk>',views.Students.as_view()),    
    path('listteacher/',views.ListTeacher.as_view()),
    path('createteacher/',views.CreateTeacher.as_view()),
    path('loginteacher/',views.LoginTeacher.as_view()),
    path('teacher/<int:pk>',views.Teachers.as_view()),
    path('listentrance/',views.ListEntranceQuestion.as_view()),
    path('createentrance/',views.CreateEntranceQuestion.as_view()),
    path('entrance/<int:pk>',views.EntranceQuestions.as_view()),
    path('listquestioncomment/',views.ListQuestionComment.as_view()),
    path('createquestioncomment/',views.CreateQuestionComment.as_view()),
    path('questioncomment/<int:pk>',views.QuestionComments.as_view()),
    
]
