from .models import categorys ,Post


def add_variable_to_context(request):
    return {
        'categorys_list': categorys.objects.all(),
        # 'like' : Post.objects.get(id=post_id).post.like_count()
        # 'like': Post.like_count(pk)
    }

