from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse('Home page')

def about_view(request):
    return HttpResponse('about page')

def contact_view(request):
    return HttpResponse('contact page')
