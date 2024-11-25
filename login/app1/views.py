from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        print(f"Username: {uname}")  # Check if the username is passed correctly

        if not uname:  # Check if username is empty
            messages.error(request, "Username is required")
            return render(request, 'signup.html')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')
        
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        messages.success(request, "User created successfully!")
        return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("incorrect username or password!")
    
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')  # Profile page
def roadmap(request):
    return render(request, 'roadmap.html')  # Profile page
def journey(request):
    return render(request, 'journey.html')  # Profile page
def motivation(request):
    return render(request, 'motivation.html')  # Profile page
def previous(request):
    return render(request, 'previous.html')  # Profile page
def friend(request):
    return render(request, 'friend.html')  # Profile page
def quiz(request):
    return render(request, 'quiz.html')  # Profile page
def setting(request):
    return render(request, 'setting.html')  # Profile page
def contact(request):
    return render(request, 'contact.html')  # Profile page
def ai(request):
    return render(request, 'ai.html')  # Profile page