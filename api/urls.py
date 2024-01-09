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
    path('getusername',views.GetUsername.as_view()),    
    path('createteacher/',views.CreateTeacher.as_view()),
    path('loginteacher/',views.LoginTeacher.as_view()),
    path('getstudent/<int:pk>',views.GetStudent.as_view()),
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
    path('classroombycode',views.ClassRoomBycode.as_view()),
    path('getclassroom/<int:pk>',views.GetClassRoom.as_view()),
    path('getmyclassroom/<int:pk>',views.GetClassRoom.as_view()),
    path('postclassroom/<int:pk>',views.PostClassRoom.as_view()),
    path('message/<str:pk>',views.MessageGet.as_view()),
    path('mymessage/<int:pk>',views.MyMessage.as_view()),
    path('group/<int:pk>',views.Group.as_view()),
    path('joingroup',views.JoinGroup.as_view()),
    path('mygroup/<str:pk>',views.GroupMessageGet.as_view()),
    path('friend/<int:pk>',views.MyFriend.as_view()),
    path('online/<int:pk>',views.Online.as_view()),
    path('setprofile/<int:pk>',views.SetProfile.as_view()),
    path('classroomseen/<int:pk>',views.ClassRoomSeen.as_view()),
    path('chatseen/<int:pk>',views.ChatSeen.as_view()),
    path('notification/<int:pk>',views.Notification.as_view()),
    
]
