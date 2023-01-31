from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

def profile(request):
    return render(request, 'profile/profile.html')

@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        user = UserSerializer.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def event_api(request, id):

    user = get_object_or_404(User, pk=id)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)