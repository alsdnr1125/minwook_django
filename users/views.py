from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from .models import User


# Create your views here.
def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(username=username, password=password)
		if user is not None:
			print("Complete")
			login(request, user)
		else:
			print("Fail")
	return render(request, "users/login.html")


def logout_view(request):
	logout(request)
	return redirect("user:login")


def signup_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		firstname = request.POST["firstname"]
		lastname = request.POST["lastname"]
		email = request.POST["email"]
		user_id = request.POST["user_id"]

		user = User.objects.create_user(username, email, password)
		user.last_name = lastname
		user.first_name = firstname
		user.user_id = user_id
		user.save()

		# os.mkdir(f"mysite/media/{username}")
		return redirect("user:login")

	return render(request, "users/signup.html")


def return_user(request):
	return request.user.id


def index(request):
	return render(request, "users/index.html", {})