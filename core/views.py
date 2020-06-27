from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import Post


def theory_page(request):
    """
    Main page with blog items
    :param request: request
    :return: JSON with objects
    """
    try:
        query = Post.objects.filter(type=1)
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


def practice_page(request):
    """
    Main page with blog items
    :param request: request
    :return: JSON with objects
    """
    try:
        query = Post.objects.filter(type=0)
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


def info_page(request):
    """
    Main page with blog items
    :param request: request
    :return: JSON with objects
    """
    try:
        query = Post.objects.filter(type=2)
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
