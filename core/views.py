from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import Post


def main_page(request):
    """
    Main page with blog items
    :param request: request
    :return: JSON with objects
    """
    try:
        query = Post.objects.all()
    except ValueError:
        query = []
    num = len(query)
    posts = []
    for obj in query:
        words = obj.text.split(' ')[:10]
        text = ""
        for word in words:
            text += " " + word
        post = {'title': obj.title,
                'short': text + "...",
                'date': str(obj.published).split('+')[0]}
        posts.append(post)
    return render(request, 'main.html', {'posts': posts,
                                         'len': num})

