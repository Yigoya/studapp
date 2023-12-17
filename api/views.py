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
		try:
			student = Student.objects.get(id=pk)
			serializer = StudentSerializer(student,many=False)
		
			return 

			(serializer.data)
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
		