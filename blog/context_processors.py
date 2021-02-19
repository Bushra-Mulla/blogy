from .models import *

def add_variable_to_context(request):
    return {
        'testme': 'Hello world!'
    }


def reports(request):
    reports = report.objects.all().order_by('-id')
    return {'reports': reports}
