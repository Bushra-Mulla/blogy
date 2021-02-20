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


# def notArchivedReport(request):
#     reports = report.objects.filter(is_archived=False)
#     print(reports)
#     # return HttpResponseRedirect('/reports/', {'reports': reports})
