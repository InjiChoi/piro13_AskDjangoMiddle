from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .forms import SignupForm

# Create your views here.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# 회원가입 첫번째 방법
'''def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) #로그인 처리
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form':form,
    })'''
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('profile')

# 회원가입 두번째 방법
signup = SignupView.as_view()