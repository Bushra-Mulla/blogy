from .models import *
from django.http import HttpResponse, HttpResponseRedirect


def add_variable_to_context(request):
    return {
        'testme': 'Hello world!'
    }


# def reports(request):
#     reports = report.objects.all().order_by('-id')
#     return {'reports': reports}


def countReports(request):
    countReports = report.objects.all().count()
    print(countReports)
    return {'countReports': countReports}


def countNotArchivedReport(request):
    countReports = report.objects.filter(is_archived=False).count()
    print(countReports)
    return {'countNotArchivedReport': countReports}


def countArchivedReport(request):
    countReports = report.objects.filter(is_archived=True).count()
    print(countReports)
    return {'countArchivedReport': countReports}


def getAllNotArchivedReport(request):
    reports = report.objects.filter(is_archived=False).select_related(
        'user_id__user_profile').all().order_by('-id')
    print(reports)
    return {'notArchivedReport': reports}


def getReports(report):
    return {'report': report}


def getAllArchivedReport(request):
    reports = report.objects.filter(is_archived=True).select_related(
        'user_id__user_profile').all().order_by('-id')
    print(reports)
    return {'archivedReport': reports}


def all(request):
    reports = report.objects.all().select_related(
        'user_id__user_profile').all().order_by('-id')
    return {'allReport': reports}

from .models import categorys

def add_variable_to_context(request):
    return {
        'categorys_list': categorys.objects.all()
    }




## publish

def countpost(request):
    countpost = Post.objects.filter(isPublish='published').count()
    return {'countpost': countpost}


def countrefused (request):
    countpost = Post.objects.filter(isPublish='refused').count()
    return {'countrefused': countpost}


def countnotPublished(request):
    countpost = Post.objects.filter(isPublish = 'notPublished').count()
    return {'countnotPublished': countpost}


# def getAllNotArchivedReport(request):
#     reports = report.objects.filter(is_archived=False).select_related(
#         'user_id__user_profile').all().order_by('-id')
#     return {'notArchivedReport': reports}


# def getReports(report):
#     return {'report': report}


# def getAllArchivedReport(request):
#     reports = report.objects.filter(is_archived=True).select_related(
#         'user_id__user_profile').all().order_by('-id')
#     print(reports)
#     return {'archivedReport': reports}


# def all(request):
#     reports = report.objects.all().select_related(
#         'user_id__user_profile').all().order_by('-id')
#     return {'allReport': reports}

# from .models import categorys

# def add_variable_to_context(request):
#     return {
#         'categorys_list': categorys.objects.all()
#     }
