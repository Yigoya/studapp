from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class EntranceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceQuestion
        fields = '__all__'
        
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class ClassRoomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoomStudent
        fields = '__all__'

class ClassRoomPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoomPost
        fields = '__all__'

class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=GroupChat
        fields = '__all__'

class GroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=GroupUser
        fields = '__all__'