from django.shortcuts import render,redirect
from hospitalapp.models import Member
from hospitalapp.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')


def login(request):
    return render(request, 'LOG IN.html')

def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        member.save()
        return redirect('/register')

    else:
        return render(request, 'register.html')

def upload(request):
    return render(request, 'upload.html')

def contact(request):
    if request.method == 'POST':
        contact = Contact(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'])
        contact.save()
        return redirect('')

    else:
        return render(request, 'index.html')