from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    """Вью формы лоигига"""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # возвращает объект пользователя User, если он успешно аутентифицирован или None
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                # поле стандартное - активный пользовательи (не заблокирован)
                if user.is_active:
                    # авторизуем
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    """Рабочий стол после входа"""

    # передаем перменную что сказать где мы находитмся {'section': 'dashboard'}
    return render(request,'account/dashboard.html',{'section': 'dashboard'})