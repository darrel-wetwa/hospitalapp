from django.shortcuts import render,redirect
from hospitalapp.models import Member
from hospitalapp.models import Message
from hospitalapp.models import Users

# Create your views here.
def index(request):
    if request.method == 'POST':
        messages = Message(name =request.POST['name'],
                          email =request.POST['email'],
                          subject =request.POST['subject'],
                          message =request.POST['message'])
        messages.save()
        return redirect('/')
    else:
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

def detail(request):
    details = Message.objects.all()
    return render(request,'details.html',{'details':details})

def user(request):
    users = Users.objects.all()
    return render(request, 'details2.html', {'users':users})
