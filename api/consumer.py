import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message
from .serializer import MessageSerializer
from .models import Student
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


class ChatConsumer(WebsocketConsumer):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.room_name = None

	def connect(self):
		# Access the room name from the URL path
		self.room_name = self.scope['url_route']['kwargs']['rm']
		self.room_group_name = f"chat_{self.room_name}"

		# Add the consumer to the group based on the dynamic room name
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
		)

		self.accept()

		self.send(text_data=json.dumps({
			'type': 'connection_established',
			'message': 'you are now connected!',
		}))
		
	def receive(self,text_data):
		
		text_data_json = json.loads(text_data)
		print(text_data)
		
		data = {
                    'body': text_data_json['body'],
                    'sender': text_data_json['sender'],
                    'receiver': text_data_json['receiver'],
                    'roomid': text_data_json['roomid']
                }
		print(data)
		receiver = Student.objects.get(id=text_data_json['receiver'])
		sender = Student.objects.get(id=text_data_json['sender'])
		send_notification(receiver.token,sender.name,text_data_json['body'])
		message = data
		serializer = MessageSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
		else:
			print('serializer:',serializer.errors)

		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type':'chat_message',
				'message':message
			}
		)
		
		# print('Message: ',message)

		# self.send(text_data=json.dumps({
		# 	'type': 'chat',
		# 	'message':message
		# }))
	def chat_message(self,event):
		send_notification('cFp7R6seSNuAql8TAOG5Lg:APA91bEfA3Pgf027q-lX_lFXIHRx9Z9pThKb-WkS7hLlWx3w0kQeb0yasL36zrsR4Z_NDPCW6CHl9oV0Rs-XP_e9nXaNLNJjVhE1v-OTuTbAeRG9cI3_6M5ees-_lW1bW_b4mdLjNG5W','EduFlex','the myghty')
		message = event['message']
  
		self.send(text_data=json.dumps({
			'type': 'chat',
			'msg':message
		}))

class GroupConsumer(WebsocketConsumer):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.room_name = None

	def connect(self):
		# Access the room name from the URL path
		self.room_name = self.scope['url_route']['kwargs']['rm']
		self.room_group_name = f"chat_{self.room_name}"

		# Add the consumer to the group based on the dynamic room name
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
		)

		self.accept()

		self.send(text_data=json.dumps({
			'type': 'connection_established',
			'message': 'you are now connected!',
		}))
		
	def receive(self,text_data):
		
		text_data_json = json.loads(text_data)
		print(text_data)
		
		data = {
                    'body': text_data_json['msg']['body'],
                    'sender': text_data_json['msg']['sender'],
                    'receiver': 0,
                    'roomid': text_data_json['msg']['roomid']
                }
		print(data)
		# receiver = Student.objects.get(id=text_data_json['receiver'])
		# sender = Student.objects.get(id=text_data_json['sender'])
		# send_notification(receiver.token,sender.name,text_data_json['body'])

		message = text_data_json

		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type':'chat_message',
				'message':message
			}
		)
		serializer = MessageSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			print(serializer.data)
		else:
			print('serializer:',serializer.errors)

		# async_to_sync(self.channel_layer.group_send)(
		# 	self.room_group_name,
		# 	{
		# 		'type':'chat_message',
		# 		'message':message
		# 	}
		# )
		
		# print('Message: ',message)

		# self.send(text_data=json.dumps({
		# 	'type': 'chat',
		# 	'message':message
		# }))
	def chat_message(self,event):
		send_notification('cFp7R6seSNuAql8TAOG5Lg:APA91bEfA3Pgf027q-lX_lFXIHRx9Z9pThKb-WkS7hLlWx3w0kQeb0yasL36zrsR4Z_NDPCW6CHl9oV0Rs-XP_e9nXaNLNJjVhE1v-OTuTbAeRG9cI3_6M5ees-_lW1bW_b4mdLjNG5W','EduFlex','the myghty')
		message = event['message']
  
		self.send(text_data=json.dumps({
			'type': 'chat',
			'msg':message
		}))