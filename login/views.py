from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def group_check(request):
	group_name = Group.objects.all().filter(
	    user=request.user)  # get logget user grouped name
	group_name = str(group_name[0])  # convert to string

	if "Student" == group_name:
		return redirect('http://127.0.0.1:8000/student/')
	elif "Teacher" == group_name:
		return redirect('http://127.0.0.1:8000/teacher/')


def logout_view(request):
	logout(request)
	return redirect('http://127.0.0.1:8000/')


class register_teacher(TemplateView):
  template_name = "register_attorney.html"


class register_student(TemplateView):
  template_name = "register_customer.html"


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register_student.html', {'form': form})


def signup(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			user.save()

			user_group = Group.objects.get(name='Student') 

			user.groups.add(user_group)

			#log the user in
			login(request, user)

			return redirect('home')

	else:

		form = UserCreationForm()

	return render(request, 'register_customer.html', {'form':form})