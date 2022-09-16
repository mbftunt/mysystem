from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUser
from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def users(request):
    list_user = MyUser.objects.all()
    return render(request, "users/list-user.html", dict(list_user=list_user, title="Danh sách người dùng 1"))
