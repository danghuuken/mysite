from django.shortcuts import render

def home(request):
	return render(request, "mysite/index.html", {})

def home_files(request, filename):
	return render(request, filename, {}, context_type="text/plain")