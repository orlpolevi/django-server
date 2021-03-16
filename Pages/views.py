from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>WORKING ON TUTORING PROJECT</h1>")
	my_context = {
	"text1": "just for test",
	"text2": "context dictionary",
	"text3": 12345,
	"text4": ["random","words","that","has","no","meaning"]
	}
	return render(request, "home.html", my_context)


def match_student_to_totur_view(*args, **kwargs):
	return HttpResponse("<h1> page under construction - content will be added in the future </h1>")

def test_page_from_matan_view(request, *args, **kwargs):
	return render(request, "ManagerScreen.html", {})