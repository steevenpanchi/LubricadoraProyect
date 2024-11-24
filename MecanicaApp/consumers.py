import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'room1'
        self.room_group_name = f'chat_{self.room_name}'

        # Unirse a la sala de chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Dejar la sala de chat
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recibir mensaje desde el WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']

        # Enviar el mensaje a la sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender
            }
        )

    # Recibir mensaje de la sala de chat
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
