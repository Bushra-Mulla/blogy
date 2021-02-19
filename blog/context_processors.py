from .models import categorys


def add_variable_to_context(request):
    return {
        'categorys_list': categorys.objects.all()
    }
