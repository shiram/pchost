from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'pages/signin.html')

def register(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'pages/signup.html')