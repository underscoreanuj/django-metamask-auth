"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.shortcuts import render, redirect
from django.contrib import auth


## *** feel free to add these views in a separete views.py file

## metamask web3 auth specific views
## ------------------------------------------------------------
def login(request):
    if not request.user.is_authenticated:
        return render(request, 'metamask_web3_auth/login.html')
    else:
        return redirect('/home')


def auto_login(request):
    if not request.user.is_authenticated:
        return render(request, 'metamask_web3_auth/autologin.html')
    else:
        return redirect('/home')


def logout(request):
    auth.logout(request)
    return redirect('/home')
## ------------------------------------------------------------

def home(request):
    context = {
        'user': request.user,
    }

    return render(request, 'index.html', context=context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),

    ## web3 auth specific urls
    ## ------------------------------------------------------------
    re_path(r'^$', RedirectView.as_view(url='/login')),
    re_path(r'^login/', login, name='login'),
    re_path(r'^auto_login/', auto_login, name='autologin'),
    re_path(r'^logout/', logout, name='logout'),
    re_path(r'', include('metamask_web3_auth.urls')),
    ## ------------------------------------------------------------
]
