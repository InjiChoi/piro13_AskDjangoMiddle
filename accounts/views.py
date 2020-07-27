from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User

# Create your views here.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# 회원가입 첫번째 방법
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {
#         'form':form,
#     })

# 회원가입 두번째 방법
signup = CreateView.as_view(model=User, 
        template_name='accounts/signup.html',
        success_url = settings.LOGIN_URL,
        form_class=UserCreationForm)