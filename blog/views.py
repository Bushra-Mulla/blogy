from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    last_twenty = Post.objects.filter(
        isPublish='published').select_related('author__user_profile').order_by('-id')[:20]
    return render(request, 'index.html', {'posts': last_twenty})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username, 'id ', user.id)
            # HttpResponse('<h1>Success</h1>')
            # return HttpResponseRedirect('')
            return HttpResponseRedirect('/profile/create')
        else:
            print('try again')
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/show.html', {'post': post})


@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'post_img', 'category_id']
    success_url = 'user/posts/'

    def form_valid(self, form, *kwargs):
        self.object = form.save(commit=False)
        # get one field
        print('fhgbjlkm;,', self.object.title)
        print('----------form----------;,', form)
        print('selffffffffffff;,', self.request.POST)
        self.object.author_id = self.request.user.id
        self.object.save()
        # if self.request.POST['submit'] == 'cancel':
        #     # if self.request.GET.get('NameOfYourButton') == 'YourValue':
        #     print('self.request.POST', self.request.POST)
        # if self.request.method == 'GET':
        # return HttpResponse('llllllll?;')
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&", self.request.method)
        return HttpResponseRedirect('/user/posts/')
        # return "True"

    def draft(self):
        # result = super(CreateView, self).is_valid()
        # print('aaaaaaaaaaaaaa', form_valid())
        print("request method ***********", result)
        if self.request.method == 'GET':
            return HttpResponse('hhhhhhhhhhhh;')
        return HttpResponse('ghkjl;')

    # def draft(self):
        # print('fhgbjlkm;,', self.object.title)
    #     print('----------form----------;,', form)
    #     print('selffffffffffff;,', self.request.POST)
    #     self.object.author_id = self.request.user.id
    #     self.object.save()
    #     if self.request.POST['submit'] == 'cancel':
    #         # if self.request.GET.get('NameOfYourButton') == 'YourValue':
    #         print('self.request.POST', self.request.POST)
    #     return HttpResponseRedirect('/user/posts/')
    #     # self.object = form.save(commit=False)
    #     # if self.object.title is not '':
    #     #     print('*********************')
    #     return HttpResponse('draft')
    # def post(self, form):
    #     if form.form_invalid():
    #         if self.request.POST['cancel']:
    #             # url = self.get_success_url()
    #             return HttpResponse("url")
    #         else:
    #             return HttpResponseRedirect('/user/posts/')
    #     else:
    #         print("yeas")
    #         if self.request.POST['cancel']:
    #             # url = self.get_success_url()
    #             return HttpResponse("url")
    #         else:
    #             return HttpResponseRedirect('/user/posts/')


@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'post_img', 'category_id']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/post/' + str(self.object.pk))
        
@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = '/'


def post_draft(request):
    # if request.method == POST: title', 'content', 'post_img', 'category_id
    title = request.POST.get('title')
    # href="{% url 'post_draft'%}"
    # if title == '':
    # if request.form.is_valid():
    #     print("title")
    # else:
    #     print('error')
    # return HttpResponse('<h1>Draft</h1>', title)
    # print('null')

    # if request
    return HttpResponse(title)


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    post = Post.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'post': post})


def category_view(request, category_name):
    categorys_post = categorys.objects.get(category_name=category_name)
    post = Post.objects.filter(
        category_id=categorys_post, isPublish='published').order_by('-id')
    return render(request, 'category/category.html', {'category_name': category_name, 'posts': post, 'category_info': categorys_post})


def userPostsList(request):
    current_user = request.user
    posts = Post.objects.filter(author=current_user.id).order_by('-id')
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def userPublishedPostsList(request):
    current_user = request.user
    posts = Post.objects.filter(isPublish="published", author=current_user.id)
    # print(current_user.id)
    # print(current_user.username)
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def userNotPublishedPostsList(request):
    current_user = request.user
    posts = Post.objects.filter(
        isPublish="notPublished", author=current_user.id)
    # print(current_user.username)
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def userRefusedPostsList(request):
    current_user = request.user
    posts = Post.objects.filter(isPublish="refused", author=current_user.id)
    # print(current_user.id)
    # print(current_user.username)
    print(posts)
    return render(request, 'userPostsList.html', {'posts': posts})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class categoryCreate(CreateView):
    # print('create new category')
    model = categorys
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')

@method_decorator(login_required, name='dispatch')
class ProfileCreate(CreateView):
    model = user_profile
    fields = ['about_me', 'position', 'profile_picture']
    success_url = '/profile'

    def form_valid(self, form, *kwargs):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        return HttpResponseRedirect('/profile')
        
        
def profile(request):
    # current_user = request.user.id
    # posts = user_profile.objects.filter(id=current_user)
    posts = Post.objects.filter(author=request.user)
    userInfo = user_profile.objects.filter(user=request.user)
    return render(request, 'user/profile.html', {
        'post': posts,
        'userInfo': userInfo,
    })


class ProfileUpdate(UpdateView):
    model = user_profile
    fields = ['about_me', 'position', 'profile_picture']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/profile/')


def reports(request):
    # reports = report.objects.all().order_by('-id')
    return render(request, 'report/report_list.html', {"reports": allReports()})


def allReports():
    reports = report.objects.all().select_related(
        'user_id__user_profile').all().order_by('-id')
    return reports


class reportCreate(CreateView):
    model = report
    # fields = '__all__'
    fields = ['title', 'message']
    success_url = '/'

    def form_valid(self, form, *kwargs):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        # get post instance by id
        post = Post.objects.get(id=self.kwargs['post_id'])
        # print(post)
        self.object.Post_id = post
        self.object.save()
        return HttpResponseRedirect('/post/'+str(post.id))


def reportDetails(request, report_id):
    report_details = report.objects.get(
        id=report_id)
    print(report_details.title)
    return render(request, 'report/report_list.html', {'reports': allReports(), 'report_details': report_details})


def archiveReport(request, report_id):
    reportDetails = report.objects.get(
        id=report_id)
    reportDetails.is_archived = True
    reportDetails.save()
    print(reportDetails.is_archived)
    return HttpResponseRedirect('/reports/', {'reports': allReports()})

# Query: Retrive number of not archived reports , make it a badge for admin anounncemnt


def notArchivedReport(request):
    reports = report.objects.filter(is_archived=False).select_related(
        'user_id__user_profile').all()
    print(reports)
    return render(request, 'report/report_list.html', {'reports': reports})


def archivedReport(request):
    reports = report.objects.filter(is_archived=True)
    print(reports)
    return render(request, 'report/report_list.html', {'reports': reports})


def published(request):
    notPublished = Post.objects.filter(isPublish='notPublished')

    # notPublished.published_update()
    return render(request, 'post/publish_manage.html', {'notPublished': notPublished})


def all_post():
    all_Post = Post.objects.all().select_related(
        'author__user_profile').all()
    return Post


def post_details(request, post_id):
    post_details = post.objects.get(
        id=post_id)
    return render(request, 'post/publish_manage.html', {'post_details': post_details})


def likeview(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        profile = User.objects.get(username=user)

        if profile in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

    # return HttpResponse(status=204)
    post.save()

    return HttpResponseRedirect('/post/'+post_id, {'profile': profile})


def likes_list(request):
    user = request.user
    likes_post = Post.objects.filter(likes=user).all()
    return render(request, 'profile/like_list.html', {'posts': likes_post})


def search(request):
    if request.method == 'GET':
        search = request.GET.get('q')
        if search:
            result = Post.objects.filter(Q(title__icontains=search))
            return render(request, "search.html", {"posts": result})

    else:
        return render(request, "base.html", {})
