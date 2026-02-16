from django.http import JsonResponse
import json

def save_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Save to database
        print(data)

        return JsonResponse({"status": "success"})
