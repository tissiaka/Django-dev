from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Explorer!")

# Create your views here.
