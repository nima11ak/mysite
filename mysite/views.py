from django.http import HttpResponse,JsonResponse

def Http_test(request):
    return HttpResponse('hello mother fucker')
def json_test(request):
    return JsonResponse({"name":'omid',"last name":'akbari'})