from django.http import HttpResponse


def login_redirect(request):
    return HttpResponse('<h1>Login redirect</h1>')
