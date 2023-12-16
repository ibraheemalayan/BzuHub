from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')

def add_user(request):
    errors = User.objects.user_validator(request.POST, 1)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name = request.POST['first_name'],
                            last_name = request.POST['last_name'],
                            birthday = request.POST['birthday'],
                            email = request.POST['email'],
                            password = pw_hash
                            )
        request.session['first_name'] = request.POST['first_name']
        messages.success(request, 'Successfully registered!')
        return redirect('/success')

def render_success(request):
    try:
        request.session['first_name']
        return render(request, 'success.html')
    except:
        return redirect('/')

def log_out(request):
    if request.session['first_name']:
        del request.session['first_name']
    return redirect('/')

def log_in(request):
    errors = User.objects.user_validator(request.POST, 2)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.filter(email = request.POST['login_email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
                request.session['first_name'] = logged_user.first_name
                messages.success(request, 'Successfully logged in!')
                return redirect('/success')
            else:
                messages.error(request, 'Wrong Password! Try again')
        return redirect('/')

def delete_all(request):
    for user in User.objects.all():
        user.delete()
    return redirect('/')

