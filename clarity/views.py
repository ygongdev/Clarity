from django.shortcuts import render, redirect
from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm, InfoForm
from .models import Info
from django.db.models import Q
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
# Create your views here.

# add rows to resources
def add_info(request):
    categories = ['SoulShield', 'Dailies', 'Gold Making', 'Leveling Up', 'Equipment', 'Dungeons', 'Quest']
    if not request.user.is_authenticated():
        return render(request, 'clarity/unauthorized.html')
    else:
        if request.method == 'POST':
            form = InfoForm(request.POST)
            if form.is_valid():
                form.save()
                form = InfoForm()
                return render(request, 'clarity/add_info.html', {'form':form, 'categories': categories})
            else:
                context = {
                    "form": form,
                    "error_message": "Invalid field inputs",
                    "categories": categories
                }
                return render(request, 'clarity/add_info.html', context)
        else:
            form = InfoForm()
            return render(request, 'clarity/add_info.html', {'form':form, 'categories':categories })
        #return render(request, 'clarity/resources.html', {'form': form })

# delete rows base on index
def delete_info(request, info_id):
    info = Info.objects.filter(id=info_id)
    info.delete()
    info = Info.objects.all()

    return render(request, 'clarity/resources.html', {'info':info})


def index(request):
    if request.user.is_authenticated():
        return render(request, 'clarity/index.html')
    else:
        return render(request, 'clarity/base_visitor.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'clarity/index.html')
            else:
                return render(request, 'clarity/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'clarity/login.html', {'error_message': 'Invalid login'})
    return render(request, 'clarity/login.html')
# For when user logout
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'clarity/login.html', context)


# For registration purposes and etc
class UserFormView(View):
    form_class = UserForm
    template_name = 'clarity/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('clarity:index')

        return render(request, self.template_name, {'form': form})

def resources(request):
    error_message = "you're not authorized to access this page, please register or log in"

    if request.user.is_authenticated():
        info = Info.objects.all()
        categories = ['SoulShield', 'Dailies']
        return render(request, 'clarity/resources.html', {'info':info, 'categories':categories})
    else:
        context = {
            'error_message': error_message,
        }
        return render(request, 'clarity/unauthorized.html', context)

def profile(request):
    error_message = "you're not authorized to access this page, please register or log in"
    context = {
        'error_message': error_message,
    }
    if request.user.is_authenticated():
        return render(request, 'clarity/profile.html', context)
    else:
        return render(request, 'clarity/unauthorized.html', context)

def communication(request):
    if request.user.is_authenticated():
        return render(request, 'clarity/communication.html', {'template':'clarity/base.html'})
    else:
        return render(request, 'clarity/communication.html', {'template':'clarity/base_visitor.html'})