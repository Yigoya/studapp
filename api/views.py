from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from .data import questions
# Create your views here.
@api_view(['GET'])
def getRoute(request):
	user = User.objects.all()
	print(user)
	serializer = UserSerializer(user,many = True)
	return Response(serializer.data)

@api_view(['POST'])
def login(request):
	user = get_object_or_404(User, username=request.data['username'])
	if not user.check_password(request.data['password']):
		return Response("missing user", status=status.HTTP_404_NOT_FOUND)
	token, created = Token.objects.get_or_create(user=user)
	serializer = UserSerializer(user)
	return Response({'token': token.key, 'user': serializer.data})


@api_view(['POST'])
def signup(request):
	print(request.data['username'])
	serializer = UserSerializer(data= request.data)
	if serializer.is_valid():
		serializer.save()
		user = User.objects.get(username = request.data['username'])
		user.set_password(request.data['password'])
		user.save()
		token = Token.objects.create(user=user)
		return Response({'token': token.key, 'user': serializer.data})
		serializer = UserSerializer(user)
		return Response(serializer.data)
	return Response(serializer.errors)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
	return Response("passed!")

class CreateStudent(APIView):
	def post(self,req):
		
		serializer = StudentSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			user = Student.objects.get(email = req.data['email'])
			user.set_password(req.data['password'])
			user.save()
			# token = Token.objects.create(user=user)
			return Response({'user': serializer.data})
		return Response(serializer.errors)

class LoginStudent(APIView):
	def post(self,req):
		
		user = get_object_or_404(Student, email=req.data['email'])
		if not user.check_password(req.data['password']):
			return Response('check your email',status=status.HTTP_404_NOT_FOUND)
		serializer = StudentSerializer(user)
		return Response(serializer.data)


class ListStudent(APIView):
	def get(self,req):
		student = Student.objects.all()
		serializer = StudentSerializer(student,many=True)
		return Response(serializer.data)

class Students(APIView):
	student = None
	def get_student_by_id(self,pk):
		try:
			self.student = Student.objects.get(id=pk)
			print(self.student)
		except:
			return Response({
				"msg":'Student does not exist'
			})
	def get(self,req,pk):
		print(req.GET.get('email'))
		try:
			student = Student.objects.get(email=req.GET.get('email'))
			serializer = StudentSerializer(student,many=False)
		
			return Response(serializer.data)
		except:
			return Response({
				"msg":'Student does not exist'
			})
		# self.get_student_by_id(pk)
		# serializer = StudentSerializer(self.student,many=False)
		
		# return Response(serializer.data)
	def put(self,req,pk):
		try:
			student = Student.objects.get(id=pk)
			serializer = StudentSerializer(instance=student,data=req.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
		except:
			return Response({
				"msg":'Student does not exist'
			})
		
class CreateTeacher(APIView):
	def post(self,req):
		
		serializer = TeacherSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			user = Teacher.objects.get(email = req.data['email'])
			user.set_password(req.data['password'])
			user.save()
			# token = Token.objects.create(user=user)
			return Response({'user': serializer.data})
		return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class LoginTeacher(APIView):
	def post(self,req):
		user = get_object_or_404(Teacher, email=req.data['email'])
		if not user.check_password(req.data['password']):
			return Response('check your email',status=status.HTTP_404_NOT_FOUND)
		serializer = TeacherSerializer(user)
		return Response(serializer.data)


class ListTeacher(APIView):
	def get(self,req):
		teacher = Teacher.objects.all()
		serializer = TeacherSerializer(teacher,many=True)
		return Response(serializer.data)

class Teachers(APIView):
	def get(self,req,pk):
		try:
			teacher = Teacher.objects.get(id=pk)
			serializer = TeacherSerializer(teacher,many=False)
		
			return Response(serializer.data)
		except:
			return Response({
				"msg":'Teacher does not exist'
			})
		# self.get_Teacher_by_id(pk)
		# serializer = TeacherSerializer(self.Teacher,many=False)
		
		# return Response(serializer.data)
	def put(self,req,pk):
		try:
			teacher = Teacher.objects.get(id=pk)
			serializer = TeacherSerializer(instance=teacher,data=req.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
		except:
			return Response({
				"msg":'Teacher does not exist'
			})
		
  
class CreateEntranceQuestion(APIView):
	def post(self,req):
		
		serializer = EntranceQuestionSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'user': serializer.data})
		return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



class ListEntranceQuestion(APIView):
	def get(self,req):
		entranceQuestion = EntranceQuestion.objects.all()
		serializer = EntranceQuestionSerializer(entranceQuestion,many=True)
		return Response(serializer.data)

class EntranceQuestions(APIView):
	def get(self,req,pk):
		try:
			entranceQuestion = EntranceQuestion.objects.get(id=pk)
			serializer = EntranceQuestionSerializer(entranceQuestion,many=False)
		
			return Response(serializer.data)
		except:
			return Response({
				"msg":'EntranceQuestion does not exist'
			})
		# self.get_EntranceQuestion_by_id(pk)
		# serializer = EntranceQuestionSerializer(self.EntranceQuestion,many=False)
		
		# return Response(serializer.data)
	def put(self,req,pk):
		try:
			entranceQuestion = EntranceQuestion.objects.get(id=pk)
			serializer = EntranceQuestionSerializer(instance=entranceQuestion,data=req.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
		except:
			return Response({
				"msg":'EntranceQuestion does not exist'
			})
		
class CreateClassRoomPost(APIView):
	def post(self,req):
		
		serializer = ClassRoomPostSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'user': serializer.data})
		return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



class ListClassRoomPost(APIView):
	def get(self,req):
		classRoomPost = ClassRoomPost.objects.all()
		serializer = ClassRoomPostSerializer(classRoomPost,many=True)
		return Response(serializer.data)

class ClassRoomPosts(APIView):
	def get(self,req,pk):
		try:
			classRoomPost = ClassRoomPost.objects.get(id=pk)
			serializer = ClassRoomPostSerializer(classRoomPost,many=False)
		
			return Response(serializer.data)
		except:
			return Response({
				"msg":'ClassRoomPost does not exist'
			})

	def put(self,req,pk):
		try:
			classRoomPost = ClassRoomPost.objects.get(id=pk)
			serializer = ClassRoomPostSerializer(instance=classRoomPost,data=req.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
		except:
			return Response({
				"msg":'ClassRoomPost does not exist'
			})
		
  
class CreateQuestionComment(APIView):
	def post(self,req):
		
		serializer = QuestionCommentSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'user': serializer.data})
		return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class MatrixOne(APIView):
	def get(self,req):
		data = []
		for q in questions:
			print(questions[q])
			serializer = EntranceQuestionSerializer(data=questions[q])
			if serializer.is_valid():
				serializer.save()
		return Response(serializer.errors)
class MatrixAll(APIView):
	def get(self,req):
		data = EntranceQuestion.objects.all()
		serializer = EntranceQuestionSerializer(data,many=True)
		return Response(serializer.data)

class ListQuestionComment(APIView):
	def get(self,req):
		questionComment = QuestionComment.objects.all()
		serializer = QuestionCommentSerializer(questionComment,many=True)
		return Response(serializer.data)

class QuestionComments(APIView):
	def get(self,req,pk):
		try:
			questionComment = QuestionComment.objects.get(id=pk)
			serializer = QuestionCommentSerializer(questionComment,many=False)
		
			return Response(serializer.data)
		except:
			return Response({
				"msg":'QuestionComment does not exist'
			})

	def put(self,req,pk):
		try:
			questionComment = QuestionComment.objects.get(id=pk)
			serializer = QuestionCommentSerializer(instance=questionComment,data=req.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
		except:
			return Response({
				"msg":'QuestionComment does not exist'
			})
class CreateClassRoom(APIView):
	def get(self,req):
		data = ClassRoom.objects.all()
		serializer = ClassRoomSerializer(data,many=True)
		return Response(serializer.data)
	def post(self,req):
		serializer = ClassRoomSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		return Response(serializer.errors)
	
class JoinClassRoom(APIView):
	def get(self,req):
		data = ClassRoomStudent.objects.all()
		serializer = ClassRoomStudentSerializer(data,many=True)
		return Response(serializer.data)
	def post(self,req):
		print(req.data)
		user = Student.objects.get(email=req.data['student'])
		req.data['student']= user.id
		serializer = ClassRoomStudentSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		print(serializer.errors)
		return Response(serializer.errors)
	
class GetClassRoom(APIView):
	def get(self,req,pk):
		print(pk)

		try:
			data = ClassRoomStudent.objects.filter(student=pk)
			classRoom = []
			for room in data:
				clroom = ClassRoom.objects.get(id=room.classroom)
				serializer = ClassRoomSerializer(clroom)
				creator = Student.objects.get(id=clroom.teacher)
				creatorSerializer = StudentSerializer(creator)
				classRoom.append({"classrrom":serializer.data,"creator":creatorSerializer.data})
			return Response(classRoom)
		except:
			return Response([{"isExist":False}])
	# def post(self,req):
	# 	serializer = ClassRoomStudentSerializer(data=req.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		Response(serializer.data)
	# 	return Response(serializer.errors)
class GetMyClassRoom(APIView):
	def get(self,req,pk):
		print(pk)

		try:
			clroom = ClassRoom.objects.filter(teacher=pk)
			print(clroom)
			serializer = ClassRoomSerializer(clroom,many=True)
			
			return Response(serializer.data)
		except:
			return Response({"isExist":False})

class PostClassRoom(APIView):
	def get(self,req,pk):
		try:
			data = ClassRoomPost.objects.filter(classroom=pk)
			serializer = ClassRoomPostSerializer(data,many=True)
			return Response(serializer.data)
		except:
			return Response({"isExist":False})
	def post(self,req,pk):
		serializer = ClassRoomPostSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		return Response(serializer.errors)

class MyMessage(APIView):
	def get(self,req,pk):
		user = Student.objects.get(id=pk)
		lists = []
		lists = user.startedchat if user.startedchat  != None else []
		print(lists)
		msgs = Message.objects.filter(roomid__in=lists)
		msgs = msgs.order_by('-updated')
		gotFriend = []
		data=[]
		for fr in msgs:
			ids = fr.sender if fr.sender==pk else fr.sender
			if ids not in gotFriend:
				user = Student.objects.get(id=ids)
				userser = StudentSerializer(user)
				messageser = MessageSerializer(fr)
				data.append({'user':userser.data,'msg':messageser.data})
				gotFriend.append(ids)
		print(data)
		serializer = MessageSerializer(msgs,many=True)
		
		return Response(data)
	def post(self,req,pk):
		user = Student.objects.get(id=pk)
		data = req.data['data']
		if user.startedchat == None or data[0] not in user.startedchat:
			user.startedchat = user.startedchat + [data[0]] if user.startedchat  != None else  [data[0]]
		user.save()
		user2 = Student.objects.get(id=data[1])
		if user2.startedchat == None or data[0] not in user2.startedchat:
			user2.startedchat = user2.startedchat + [data[0]] if user2.startedchat  != None else  [data[0]]
		user2.save()
		serializer = StudentSerializer(user2)
		return Response(serializer.data)

class MyFriend(APIView):
	def get(self,req,pk):
		user = Student.objects.get(id=pk)
		lists = []
		lists = user.friends if user.friends  != None else []
		print(lists)
		msgs = Student.objects.filter(id__in=lists)
		serializer = StudentSerializer(msgs,many=True)
		
		return Response(serializer.data)
	def post(self,req,pk):
		user = Student.objects.get(id=pk)
		data = req.data['data']
		if user.friends == None or data[0] not in user.friends:
			user.friends = user.friends + [data[0]] if user.friends  != None else  [data[0]]
		user.save()
		user2 = Student.objects.get(id=data[0])
		if user2.friends == None or pk not in user2.friends:
			user2.friends = user2.friends + [pk] if user2.friends  != None else  [pk]
		user2.save()
		serializer = StudentSerializer(user2)
		return Response(serializer.data)
		# return Response(serializer.errors)


class MessageGet(APIView):
	def get(self,req,pk):
		data = Message.objects.filter(roomid = pk)
		serializer = MessageSerializer(data,many=True)
		return Response(serializer.data)
	def post(self,req,pk):
		serializer = MessageSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		return Response(serializer.errors)

class Group(APIView):
	def get(self,req,pk):
		groups = Groups.objects.all()
		serailizer = GroupsSerializer(groups,many=True)
		return Response(serailizer.data)
	def post(self,req,pk):
		serializer = GroupsSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		return Response(serializer.errors)
	def put(self,req,pk):
		group = Groups.objects.get(id=pk)
		serializer = GroupsSerializer(instance=group,data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)
# models.py
# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     published_date = models.DateField()

# # views.py or wherever you want to perform the query
# from datetime import date
# from .models import Book

# # Retrieve books published after the year 2000
# recent_books = Book.objects.filter(published_date__year__gt=2000)

# # Print the titles of the retrieved books
# for book in recent_books:
#     print(book.title)
