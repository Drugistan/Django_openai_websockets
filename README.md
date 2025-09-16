# Django_openai_websockets



⚙️ Installation
Clone repo:
git clone https://github.com/your-username/ai-chat.git
cd ai-chat


Create virtual environment:
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Create superuser:
python manage.py createsuperuser


Visit in browser:
Chat UI: http://127.0.0.1:8000/chat/


🖥️ Frontend (Minimal Example)
Open chat/templates/chat.html in browser:
Type message → Sent via WebSocket (ws://127.0.0.1:8000/ws/chat/).
AI Response appears in real-time.


🔑 Environment Variables
Create .env file in root:
OPENAI_API_KEY=your_api_key_here
DEBUG=True

📌 Notes
For local dev, python manage.py runserver works (ASGI auto-handled).
For production, use Daphne or Uvicorn:
daphne -p 8000 ai_chat.asgi:application

🧑‍💻 Author
Ali Khan
Python/Django Developer • Building AI + WebSocket powered apps


