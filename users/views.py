from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UploadForm
import os
from .models import User

import logging #파이썬 로깅 모듈 임포트

#settings.py 파일에서 설정된 로거를 취득함
logger = logging.getLogger('mylogger')

def my_view(request, arg1, arg2):
    #view logic
    if bad_mogo:
        logger.error('Something went worng!')  # ERROR 레벨의 로그 레코드를 생성함

def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			print("Complete")
			login(request, user)
		else:
			print("Fail")
	else:
		return render(request, "users/login.html")


def logout_view(request):
	authenticate.logout(request)
	return redirect("user:login")


def signup_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		name = request.POST["name"]
		user_id = request.POST["user_id"]

		user = User.objects.create_user(username, password, name)
		user.name = name
		user_id = user_id
		user.save()
		return redirect("user:login")
	return render(request, "users/signup.html")


def return_user(request):
	return request.user.id


def index(request):
	return render(request, "users/index.html")

def image_list(request):
	return render(request, "users/list.html", {})

def upload_image(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('user:image_list')
	else:
		form = UploadForm()
	return render(request, "users/upload.html", {'form': form})
