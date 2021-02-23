from .models import categorys
from .models import *
from django.http import HttpResponse, HttpResponseRedirect


def add_variable_to_context(request):
    return {
        'testme': 'Hello world!'
    }


# def reports(request):
#     reports = report.objects.all().order_by('-id')
#     return {'reports': reports}

def totalAnnouncement(request):
    notPublishedPosts = Post.objects.filter(isPublish='notPublished').count()
    reports = report.objects.filter(is_archived=False).count()
    totel = notPublishedPosts + reports
    # print(totel)
    return {'totalAnnouncement': totel}


def countNotPublishedPosts(request):
    count = Post.objects.filter(isPublish='notPublished').count()
    # print(countNotPublishedPosts)
    return {'countNotPublishedPosts': count}


def countReports(request):
    countReports = report.objects.all().count()
    # print(countReports)
    return {'countReports': countReports}


def countNotArchivedReport(request):
    countReports = report.objects.filter(is_archived=False).count()
    # print(countReports)
    return {'countNotArchivedReport': countReports}


def countArchivedReport(request):
    countReports = report.objects.filter(is_archived=True).count()
    # print(countReports)
    return {'countArchivedReport': countReports}


def getAllNotArchivedReport(request):
    reports = report.objects.filter(is_archived=False).select_related(
        'user_id__user_profile').all().order_by('-id')
    # print(reports)
    return {'notArchivedReport': reports}


def getReports(report):
    return {'report': report}


def getAllArchivedReport(request):
    reports = report.objects.filter(is_archived=True).select_related(
        'user_id__user_profile').all().order_by('-id')
    # print(reports)
    return {'archivedReport': reports}


def all(request):
    reports = report.objects.all().select_related(
        'user_id__user_profile').all().order_by('-id')
    return {'allReport': reports}


def add_variable_to_context(request):
    return {
        'categorys_list': categorys.objects.all()
    }
