from channels.generic.websocket import AsyncWebsocketConsumer
import openai
import json
import os
import logging
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "global_chat"
        self.room_group_name = "chat_%s" % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response_type = await self.get_ai_response(message)
        print(f"📩 Message response_type: {response_type}")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': response_type
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({"message": message}))

    async def get_ai_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return "Error: " + str(e)

