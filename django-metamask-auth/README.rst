=====
django-metamask-auth
=====

django-metamask-auth is a Django app that allows easy signup & login functionalities to you web-app using metamask.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "metamask_web3_auth" to your INSTALLED_APPS in setting.py like this::

    INSTALLED_APPS = [
        ...
        'metamask_web3_auth',
    ]

2. Add the following authentication backends to settings.py of your project::

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'metamask_web3_auth.backend.Web3Backend'
    ]

3. Make sure that your templates have the following configuration in your settings.py::
    TEMPLATES = [
        {
            ...
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
            ...
            ...
        },
    ]

4. Add to your settings.py the login redirect url and the default field to store metamask account address::
    
    LOGIN_REDIRECT_URL = '/home'
    WEB3AUTH_USER_ADDRESS_FIELD = 'username'

5. Specify the following views in your project::

    from django.contrib import admin
    from django.urls import path, include, re_path
    from django.views.generic import RedirectView
    from django.shortcuts import render, redirect
    from django.contrib import auth

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

6. Include the following urls in your application to render the following views::
    re_path(r'^$', RedirectView.as_view(url='/login')),
    re_path(r'^login/', login, name='login'),
    re_path(r'^auto_login/', auto_login, name='autologin'),
    re_path(r'^logout/', logout, name='logout'),
    re_path(r'', include('metamask_web3_auth.urls')),


7. Now, add the following templates to your templates directory (Note: you can modify these templates as per your needs)::
    https://gist.github.com/underscoreanuj/4b2ea64469595ce0b0266111653e97a0


8. Run ``python manage.py migrate``.



You're good to go, a new user can signup by specifying their ethereum address and unique email.
Once signed-up, a user can use their metamask extension to login