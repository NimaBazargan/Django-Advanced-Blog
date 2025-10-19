from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .tasks import sendEmail
import requests

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")

# def test(request):
#     if cache.get("test_delay_api") is None:
#         response = requests.get("https://1a34f124-a5f8-4d60-82c1-6aa0b3748eaa.mock.pstmn.io/test/delay/5")
#         cache.set('test_delay_api',response.json(),60)
#     return JsonResponse(cache.get("test_delay_api"))

@cache_page(60)
def test(request):
    response = requests.get("https://1a34f124-a5f8-4d60-82c1-6aa0b3748eaa.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())