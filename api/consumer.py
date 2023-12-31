import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message
from .serializer import MessageSerializer
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
		message = event['message']
  
		self.send(text_data=json.dumps({
			'type': 'chat',
			'msg':message
		}))