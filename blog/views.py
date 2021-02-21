from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy ,reverse
from django.contrib.auth.decorators import login_required


def home(request):
    last_twenty= Post.objects.filter(
        isPublish='published').select_related('author__user_profile').order_by('-id')[:20]
    return render(request, 'index.html', {'posts': last_twenty})
   

# def logIn(request):
#     if request.method == 'POST':
#         # if post, then authenticate (user submitted username and password)
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     # return HttpResponse('<h1>Success</h1>')
#                     print(user.id)
#                     return HttpResponseRedirect('/')
#                 else:
#                     HttpResponse('<h1>Try Again</h1>')

#                     # print("The account has been disabled.")
#             else:
#                 print("The username and/or password is incorrect.")
#     else:
#         form = LoginForm()
#     return render(request, 'logIn.html', {'form': form})

# def logIn(request):
#     return render(request, 'logIn.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username, 'id ', user.id)
            # HttpResponse('<h1>Success</h1>')
            # return HttpResponseRedirect('')
            return HttpResponseRedirect('/', user.id)
        else:
            print('try again')
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/show.html', {'post': post})


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


def category_view(request, category_name):
    categorys_post = categorys.objects.get(category_name=category_name)
    post = Post.objects.filter(category_id=categorys_post)
    return render(request, 'category/category.html', {'category_name': category_name, 'posts': post , 'category_info':categorys_post})
 

def published(request):
    notPublished = Post.objects.filter(isPublish='notPublished')
    return render(request, 'post/publish_manage.html', {'notPublished': notPublished})
# Query to


def userPostsList(request):
    current_user = request.user
    posts = Post.objects.all().order_by('-id')
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def userPublishedPostsList(request):
    current_user = request.user
    posts = Post.objects.filter(isPublish="published")
    # print(current_user.id)
    # print(current_user.username)
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def userNotPublishedPostsList(request):
    current_user = request.user
    posts = Post.objects.filter(isPublish="notPublished")
    # print(current_user.username)
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def userRefusedPostsList(request):
    current_user = request.user
    posts = Post.objects.filter(isPublish="refused")
    # print(current_user.id)
    # print(current_user.username)
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class categoryCreate(CreateView):
    print('create new category')
    model = categorys
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')


def category_view(request, category_name):
    categorys_post = categorys.objects.get(category_name=category_name)
    post = Post.objects.filter(
        category_id=categorys_post, isPublish='published').order_by('-id')
    return render(request, 'category/category.html', {'category_name': category_name, 'posts': post, 'category_info': categorys_post})


def published(request):
    notPublished = Post.objects.filter(isPublish='notPublished')
    publishe ='' 
    # notPublished.published_update()
    return render(request, 'post/publish_manage.html', {'notPublished': notPublished, 'publishe': publishe})

def update_publish_state(request, state):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.isPublish.update(isPublish=state)
    return HttpResponse(status=204)


# def likeviewf(request,pk):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     #  post.refresh_from_db()
#     # return HttpResponseRedirect(reverse('blog-post-show', args=[str(pk)]))
#     return HttpResponse(status=204)


# like_unlike_post
@login_required
def likeview(request):
    user=request.user
    print(user)
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post=Post.objects.get(id=post_id)
        profile = User.objects.get(username=user)

        if profile in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        
    # return HttpResponseRedirect('/')

    return HttpResponseRedirect('/post/'+post_id)
