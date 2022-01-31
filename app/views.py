from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TableAllSerializer
from .models import *

#Get Data
@api_view(['GET'])
def All_TableList(request):
    alltablelist = TableAll.objects.all()  
    serializer = TableAllSerializer(alltablelist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
def ShowLoginPage(request):
	# return render(request, "login.html")
	return render(request, "page-login.html")

def doLogin(request):
	if request.method!="POST":
		return HttpResponse("<h2>Method Not Allowed</h2>")
	else:
		user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
		if user!=None:
			login(request,user)
			if user.user_type == "1":
				return HttpResponseRedirect("admin_home")
			elif user.user_type == "2":
				return HttpResponseRedirect(reverse("bkk1_home"))
			elif user.user_type == "3":
				return HttpResponseRedirect(reverse("skw1_home"))
			elif user.user_type == "8":
				return HttpResponseRedirect(reverse("act1_home"))
			elif user.user_type == "9":
				return HttpResponseRedirect(reverse("vip1_home"))
			else:
				return HttpResponse("Student login"+str(user.user_type))
		else:
			messages.error(request,"Invalid Login Details")
			return HttpResponseRedirect("/")


def logout_user(request):
		logout(request)
		return HttpResponseRedirect("/")