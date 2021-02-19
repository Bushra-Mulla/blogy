from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    # last_twenty = Post.objects.all().order_by('-id')[:20]
    last_twenty = Post.objects.filter(isPublish=True).order_by('-id')[:20]

    related = Post.objects.select_related('author').all()
    # last_twenty=Post.objects.all()
    return render(request, 'index.html', {'posts': last_twenty, 'related': related})


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
    # print('create new category')
    model = categorys
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')


def reports(request):
    # reports = report.objects.all().order_by('-id')
    return render(request, 'report/report_list.html', {'reports': allReports()})


def allReports():
    reports = report.objects.all().order_by('-id')
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
        return HttpResponseRedirect('/')


def reportDetails(request, report_id):
    report_details = report.objects.get(id=report_id)
    print(report_details.title)
    return render(request, 'report/report_list.html', {'reports': allReports(), 'report_details': report_details})


def archiveReport(request, report_id):
    reportDetails = report.objects.get(id=report_id)
    reportDetails.is_archived = True
    reportDetails.save()
    print(reportDetails.is_archived)
    return HttpResponseRedirect('/reports/', {'reports': allReports()})

# Query: Retrive number of not archived reports , make it a badge for admin anounncemnt


def countNotArchivedReport():
    countReports = report.objects.filter(is_archived=False).count()
    print(countReports)
    return countReports
