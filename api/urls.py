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
    path('matrix',views.MatrixOne.as_view()),
    path('matrixall',views.MatrixAll.as_view()),
    path('classroom',views.MatrixAll.as_view()),
    path('createclassroom',views.CreateClassRoom.as_view()),
    path('joinclassroom',views.JoinClassRoom.as_view()),
    path('getclassroom/<int:pk>',views.GetClassRoom.as_view()),
    path('getmyclassroom/<int:pk>',views.GetMyClassRoom.as_view()),
    path('postclassroom/<int:pk>',views.PostClassRoom.as_view()),
    path('message/<str:pk>',views.MessageGet.as_view()),
    path('mymessage/<int:pk>',views.MyMessage.as_view()),
    path('group/<int:pk>',views.Group.as_view()),
    path('friend/<int:pk>',views.MyFriend.as_view()),
    
]
