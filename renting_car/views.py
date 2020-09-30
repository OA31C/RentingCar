from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse


def redirect_login(request):
    return redirect('login_url', permanent=True)


def nav(request):
    return render(request, 'expanded_base.html')


def start(request):
    print()
    print()
    print()
    print()
    print()
    print()
    print('request')
    print(request)
    print()
    print()
    print()
    print()
    print()
    print()
    output = "<button><a href='/end?name=Max'>Click</button></a>"
    return HttpResponse(output)


def end(request):
    print()
    print()
    print()
    print()
    print()
    print('end request')
    print(request.GET['name'])
    print()
    print()
    print()
    print()
    return HttpResponse('<h1>End hello</h1>')
