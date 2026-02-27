from django.shortcuts import render
from .models import ChatbotResponse   # Make sure this matches models.py

def chat(request):
    reply = ""

    if request.method == "POST":
        user_msg = request.POST.get("message").lower()
        responses = ChatbotResponse.objects.all()

        for r in responses:
            keywords = r.keywords.split(",")   # make sure field name matches models.py
            for k in keywords:
                if k.strip().lower() in user_msg:
                    reply = r.response
                    break
            if reply:
                break

        if reply == "":
            reply = "Sorry, I couldn't understand. Please contact admin."

    return render(request, "chatbot.html", {"reply": reply})