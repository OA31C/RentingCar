from django.shortcuts import redirect


def redirect_login(request):
    return redirect('login_url', permanent=True)
