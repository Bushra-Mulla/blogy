from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home (request):
    last_twenty = Post.objects.all().order_by('-id')[:20]
    # last_twenty=Post.objects.all()
    return render(request, 'index.html', {'posts':last_twenty})


def logIn(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('<h1>Success</h1>')
                    print(user.id)
                    return HttpResponseRedirect('/')
                else:
                    HttpResponse('<h1>Try Again</h1>')

                    # print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
    return render(request, 'logIn.html', {'form': form})

# def logIn(request):
#     return render(request, 'logIn.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            # HttpResponse('<h1>Success</h1>')
            # return HttpResponseRedirect('')
            return HttpResponse('<h1>Success</h1>')
        else:
            print('try again')
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'post_img', 'category_id', 'author']
    success_url = '/'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')

class PostUpdate(UpdateView):
  model = Post
  fields = ['title', 'content', 'post_img', 'category_id', 'author']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/post/' + str(self.object.pk))