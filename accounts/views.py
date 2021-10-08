from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    print(request.session['sess_id'])
    return render(request, 'home.html')


def login(request):
    try:
        sess_id = request.COOKIES.get('sess_id')
        if sess_id == request.session['sess_id']:
            return redirect('home')
    except KeyError:
        print('User is not logged In')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            session_id = 'srzd242nd2iy5tp7r8x1za1rt3psxwuo'
            request.session['sess_id'] = session_id

            print('Logged')
            response = redirect('home')
            response.set_cookie('sess_id', session_id)
            return response
    return render(request, 'accounts/login.html')
