from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import Student


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        context = {
            'students': students
        }
        return render(request, 'student.html', context)


class LendingWive(View):
    def get(self, request):
        return render(request, 'landing.html')


class UserRigisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password_1)
        user.set_password(password_1)
        user.save()
        return redirect("landing")


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password)
        if user:
            return redirect('landing')
        else:
            return render(request, 'user_note.html')
