from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserDetailForm
from .models import UserProfile, UserDetail


# Create your views here.
pnumber = 1
def home(request):
    return render(request, "authentication/index.html")
def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        pnumber = float(request.POST['pnumber'])

        user = User.objects.create_user(username=username, email=email, password=pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()

        profile = UserProfile(user=user, phone_number=pnumber)
        profile.save()


        messages.success(request, "account has been successfully created")

        return redirect('signin')



    return render(request, "authentication/signup.html")
    
def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Bad credentials!")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully!")
    return redirect('home')
#creating new stuff
def profile(request):
    form = UserAddressForm()  # Create an instance of the form class

    context = {
        'form': form  # Add the form to the rendering context
    }

    return render(request, 'authentication/profile.html', context)


def add_details(request):
    user = request.user
    try:
        user_detail = UserDetail.objects.get(user=user)
        form = UserDetailForm(request.POST or None, instance=user_detail)
    except UserDetail.DoesNotExist:
        form = UserDetailForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user_detail = form.save(commit=False)
            user_detail.user = user  # Associate with the current user
            user_detail.save()
            # Redirect to a success page or perform any other actions
            return redirect('home')
    else:  # GET request
        # Retrieve all users' details
        all_user_details = UserDetail.objects.all()

        context = {
            'form': form,
            'all_user_details': all_user_details
        }
        return render(request, 'authentication/add_details.html', context)