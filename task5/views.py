from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse

# Create your views here.



def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {'error'}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if username not in users and password == repeat_password and age >= 18:
                users.append(username)
                print(users)
                return HttpResponse(f'Приветствуем {username}')
            elif username in users:
                info['error'] = HttpResponse('Пользователь уже существует', status=400, reason='the user exists')
                print(info['error'])
                return HttpResponse('Пользователь уже существует', status=400, reason='the user exists')
            elif password != repeat_password:
                info['error'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
                print(info['error'])
                return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            elif age < 18:
                info['error'] = HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')
                print(info['error'])
                return HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')
    else:

        form = UserRegister()
        info['form'] = form
        return render(request, 'fifth_task/registration_page.html', context = info)

def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username not in users and password == repeat_password and age >= 18:
            users.append(username)
            print(users)
            return HttpResponse(f'Приветствуем {username}')
        elif username in users:
            info['error'] = HttpResponse('Пользователь уже существует', status=400, reason='the user exists')
            return HttpResponse('Пользователь уже существует', status=400, reason='the user exists')
        elif password != repeat_password:
            info['error'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
        elif age < 18:
            info['error'] = HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')
            return HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')

    context = {'info': info}
    return render(request, 'fifth_task/registration_page.html', context)

