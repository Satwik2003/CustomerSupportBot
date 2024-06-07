from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

def chat(request):
    return render(request, 'chatbot/chat.html')

def rasa_webhook(request):
    if request.method == 'POST':
        user_message = json.loads(request.body).get('message')
        response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": "user", "message": user_message})
        response_data = response.json()
        return JsonResponse(response_data, safe=False)


# Create your views here.
