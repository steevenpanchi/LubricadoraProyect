import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Aquí se puede definir el grupo o canal para cada conversación, si se necesita
        self.room_name = 'chat_room'  # O cualquier nombre dinámico basado en el contexto
        self.room_group_name = f'chat_{self.room_name}'

        # Unir el cliente al grupo de chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Aceptar la conexión WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Dejar el grupo de chat cuando el cliente se desconecte
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recibir mensaje desde WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Lógica para responder según la pregunta
        if 'hola' in message.lower():
            response_message = "¡Hola! ¿En qué puedo ayudarte hoy?"
        elif 'como estas' in message.lower():
            response_message = "Estoy bien, gracias por preguntar. ¿Y tú?"
        elif 'bien' in message.lower():
            response_message = "Me alegra saber eso"
        elif 'orden' in message.lower():
            response_message = "¿Sobre qué orden necesitas información?"
        else:
            response_message = f"Te he recibido el mensaje: '{message}', pero no entiendo la pregunta. ¿Puedes intentar otra vez?"

        # Enviar la respuesta al cliente
        await self.send(text_data=json.dumps({
            'message': response_message
        }))
