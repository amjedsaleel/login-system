from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sessions.models import Session


# Create your views here.


def home(request):
    if request.session.has_key('sess_id'):
        cookie = Session.objects.get(session_key=request.COOKIES.get('sessionid'))
        data = cookie.get_decoded()
        if data.get('sess_id') != request.session['sess_id']:
            return redirect('login')
        return render(request, 'home.html')
    return redirect('login')


def login(request):

    if request.session.has_key('sess_id'):
        cookie = Session.objects.get(session_key=request.COOKIES.get('sessionid'))
        data = cookie.get_decoded()
        if data.get('sess_id') == request.session['sess_id']:
            return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            session_id = 'srid242nd2iy5tp7r8x1za1rt3pseudo'
            request.session['sess_id'] = session_id

            print('Logged')
            response = redirect('home')
            messages.success(request, 'You are successfully logged In')
            return response
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


def logout(request):
    request.session.flush()
    messages.info(request, 'You are successfully logged Out')
    return redirect('login')
