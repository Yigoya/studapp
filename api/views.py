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
from pyfcm import FCMNotification

def send_notification(device_token, title, body):
	api_key = "AAAAwprXviI:APA91bEXWyY8K1CxEpW4Z2z781bXJ_LDpKV9_f5MpncpxLMJhmJBOjD9aOVLnwm2ajhgGq7uHbBVK4jVTlGjMxL6A3GOuNAVHw5ZyiIrKftnu0eMjidqU2Zsh56MNwqIpEVXj-AZ66DM"
	push_service = FCMNotification(api_key=api_key)

	message = {
		"registration_id": device_token,

			"message_title": title,
			"message_body": body,

	}

	result = push_service.notify_single_device(**message)
	print(result)


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
		user.token = req.data['token']
		user.save()
		serializer = StudentSerializer(user)
		return Response(serializer.data)


class ListStudent(APIView):
	def get(self,req):
		send_notification('cFp7R6seSNuAql8TAOG5Lg:APA91bEfA3Pgf027q-lX_lFXIHRx9Z9pThKb-WkS7hLlWx3w0kQeb0yasL36zrsR4Z_NDPCW6CHl9oV0Rs-XP_e9nXaNLNJjVhE1v-OTuTbAeRG9cI3_6M5ees-_lW1bW_b4mdLjNG5W','EduFlex','the myghty')
		student = Student.objects.all()
		serializer = StudentSerializer(student,many=True)
		return Response(serializer.data)
	
class GetUsername(APIView):
	student = None
	def get(self,req):
		print(req.GET.get('name'))
		try:
			student = Student.objects.get(username=req.GET.get('name'))
			# serializer = StudentSerializer(student,many=False)
			return Response({
				"isUsed":True
			})
		except:
			return Response({
				"isUsed":False
			})

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
			student = Student.objects.get(username=req.GET.get('name'))
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

class SetProfile(APIView):
	student = None

	def get(self,req,pk):
		print(req.GET.get('email'))
		try:
			student = Student.objects.get(username=req.GET.get('name'))
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
			student.avatar = req.data['avatar']
			student.save()
			# serializer = StudentSerializer(instance=student,data=req.data)
			# if serializer.is_valid():
			# 	serializer.save()
			return Response({'isSuccess':True})
			# return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
		except:
			return Response({'isSuccess':False})


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


# class GetStudent(APIView):
# 	def get(self,req,pk):
# 		user = Student.objects.get(id=pk)
# 		serializer = StudentSerializer(user)
# 		return Response(serializer.data)

class GetStudent(APIView):
	def get(self,req,pk):
		try:
			user = Student.objects.get(id=pk)
			serializer = StudentSerializer(user,many=False)
			print(serializer.data)
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

class ClassRoomBycode(APIView):
	def get(self,req):
		try:
			data = ClassRoom.objects.get(id = req.GET.get('id'))
			serializer = ClassRoomSerializer(data)
			return Response(serializer.data)
		except:
			return Response({'isExist':False})
	

class JoinClassRoom(APIView):
	def get(self,req):
		data = ClassRoomStudent.objects.all()
		serializer = ClassRoomStudentSerializer(data,many=True)
		return Response(serializer.data)
	def post(self,req):
		try:
			data = ClassRoom.objects.get(id = req.data['classroom'])
			serializer = ClassRoomSerializer(data)
			
			serializer = ClassRoomStudentSerializer(data=req.data)
			if serializer.is_valid():
				serializer.save()
				Response(serializer.data)
		except:
			return Response({'isExist':False})
		
		print(serializer.errors)
		return Response(serializer.errors)
	
class GetClassRoom(APIView):
	def get(self,req,pk):
		print(pk)

		try:
			classRoom = []
			clroom = ClassRoom.objects.filter(teacher=pk)
			# serializer = ClassRoomSerializer(clroom,many=True)
			for room in clroom:
				# clroom = ClassRoom.objects.get(id=room.classroom)
				serializer = ClassRoomSerializer(room)
				creator = Student.objects.get(id=room.teacher)
				creatorSerializer = StudentSerializer(creator)
				classRoom.append({"classrrom":serializer.data,"creator":creatorSerializer.data})
			data = ClassRoomStudent.objects.filter(student=pk)
			
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
class GetGroup(APIView):
	def get(self,req,pk):
		print(pk)

		try:
			clroom = GroupChat.objects.filter(teacher=pk)
			print(clroom)
			serializer = ClassRoomSerializer(clroom,many=True)
			
			return Response(serializer.data)
		except:
			return Response({"isExist":False})

class PostClassRoom(APIView):
	def get(self,req,pk):
		try:
			data = ClassRoomPost.objects.filter(classroom=pk)
			res = []
			for post in data:
				user = Student.objects.get(id=post.author)
				userserializer = StudentSerializer(user)
				serializer = ClassRoomPostSerializer(post)
				res.append({'post':serializer.data,'user':userserializer.data})
			return Response(res)
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

		msgs = Message.objects.filter(roomid__in=lists)
		msgs = msgs.order_by('-updated')
		gotFriend = []
		data=[]
		# print(MessageSerializer(msgs,many=True).data)
		for fr in msgs:
			ids = fr.sender if fr.sender !=pk else fr.receiver
			if ids not in gotFriend:
				user = Student.objects.get(id=ids)
				userser = StudentSerializer(user)
				messageser = MessageSerializer(fr)
				data.append({'user':userser.data,'msg':messageser.data})
				gotFriend.append(ids)

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

		msgs = Student.objects.filter(id__in=lists)
		serializer = StudentSerializer(msgs,many=True)
		
		return Response(serializer.data)
	def post(self,req,pk):
		user = Student.objects.get(id=pk)
		data = req.data['data']
		if user.friends == None or data[0] not in user.friends:
			print(user.friends)
			user.friends = user.friends + [data[0]] if user.friends  != None else  [data[0]]
			user.save()
		user2 = Student.objects.get(id=data[0])
		if user2.friends == None or pk not in user2.friends:
			user2.friends = user2.friends + [pk] if user2.friends  != None else  [pk]
			user2.save()
		serializer = StudentSerializer(user)
		serializer2 = StudentSerializer(user2)

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

class GroupMessageGet(APIView):
	def get(self,req,pk):
		res=[]
		data = Message.objects.filter(roomid = pk)
		for ds in data:
			user = Student.objects.get(id=ds.sender)
			seruser = StudentSerializer(user)
			serializer = MessageSerializer(ds)
			res.append({'user':seruser.data,'msg':serializer.data})
		
		return Response(res)
	def post(self,req,pk):
		serializer = MessageSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		return Response(serializer.errors)

class GroupMessageGet(APIView):
	def get(self,req,pk):
		data = Message.objects.filter(roomid = pk)
		res=[]
		for ds in data:
			user = Student.objects.get(id=ds.sender)
			userserializer = StudentSerializer(user)
			serializer = MessageSerializer(ds)
			res.append({'msg':serializer.data,'user':userserializer.data})
		return Response(res)
	def post(self,req,pk):
		serializer = MessageSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		return Response(serializer.errors)


class Group(APIView):
	def get(self,req,pk):
		res=[]
		usergroup = GroupUser.objects.filter(user=pk)
		for gr in usergroup:
			group = GroupChat.objects.get(id=gr.group)
			serailizer = GroupChatSerializer(group)
			msg = Message.objects.filter(roomid=group.idname)
			
			hasmsg = len(msg)>0 
			if hasmsg:
				msg = msg[len(msg)-1]
				msgserializer = MessageSerializer(msg) 
				res.append({'group':serailizer.data,'msg':msgserializer.data})	
			else:	
				res.append({'group':serailizer.data,'msg':0})		
		return Response(res)
	def post(self,req,pk):
		serializer = GroupChatSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
		else:
			return Response(serializer.errors)
		print('1 1 1 1')
		group = GroupChat.objects.get(idname=req.data['idname'])
		data = {
			'group':group.id,
			'user':pk
		}
		GUserialiser = GroupUserSerializer(data=data)
		if GUserialiser.is_valid():
			GUserialiser.save()
		else:
			Response(GUserialiser.errors)
		print('1 1 1 1')
		
		Response(serializer.data)
	def put(self,req,pk):
		group = GroupChat.objects.get(id=pk)
		serializer = GroupChatSerializer(instance=group,data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

class Online(APIView):
	def get(self,req,pk):
		data = Student.objects.get(id=pk)
		data.isOnline = not data.isOnline 
		data.save()
		serializer = StudentSerializer(data)
		return Response(serializer.data)
	
	def post(self,req,pk):
		data = Student.objects.get(id=pk)
		data.isOnline = req.data['status'] 
		data.save()
		serializer = StudentSerializer(data)
		return Response(serializer.data)

class JoinGroup(APIView):
	def get(self,req):
		data = GroupChat.objects.all()
		serializer = GroupChatSerializer(data,many=True)
		return Response(serializer.data)
	def post(self,req):
		
		try:
			data = GroupChat.objects.get(idname = req.data['group'])

			req.data['group'] = data.id
			groups = GroupUser.objects.filter(group = req.data['group'])
			for gr in groups:
				if gr.user == req.data['user']:
					return Response({'isIt':9})
			
		except:
			return Response({'isExist':False})
		
		serializer = GroupUserSerializer(data=req.data)
			
		if serializer.is_valid():
			serializer.save()
			Response(serializer.data)
		return Response(serializer.errors)
	

class ClassRoomSeen(APIView):
	def get(self,req,pk):
		data = ClassRoomPost.objects.get(id=pk)
		data.isSeen = data.isSeen + [int(req.GET.get('id'))] 
		data.save()
		serializer = ClassRoomPostSerializer(data)
		return Response(serializer.data)

class ChatSeen(APIView):
	def get(self,req,pk):
		print(req.GET.get('id'))
		res = []
		data = Message.objects.filter(roomid=pk)
		for ms in data:
			if not ms.isSeen and ms.receiver == int(req.GET.get('id')):
				res.append(ms.id)

		return Response(res)	
	def post(self,req,pk):
		data = Message.objects.get(id=pk)
		if int(req.GET.get('id')) == data.receiver:
			data.isSeen = True
			data.save()
		serializer = MessageSerializer(data)
		return Response(serializer.data)	

class Notification(APIView):
	def get(self,req,pk):
		data = ClassRoomStudent.objects.filter(student=pk)
		crpost = []
		for cr in data:
			post = ClassRoomPost.objects.filter(classroom=cr.classroom)
			for ps in post:
				if pk not in ps.isSeen:
					classroom = ClassRoom.objects.get(id = ps.classroom)
					serializer = ClassRoomSerializer(classroom)
					user = Student.objects.get(id=ps.author)
					userserializer = StudentSerializer(user)
					postserializer = ClassRoomPostSerializer(ps)
					crpost.append({'post':{'classroom':serializer.data,'post':postserializer.data,'user':userserializer.data}})
		chat = Message.objects.filter(receiver=pk)
		for ch in chat:
			if not ch.isSeen:
				sender = Student.objects.get(id=ch.sender)
				senderSer = StudentSerializer(sender)
				serializer = MessageSerializer(ch)
				crpost.append({'chat':{'chat':serializer.data,'user':senderSer.data}})
		return Response(crpost)


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
