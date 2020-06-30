from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import Post


def theory_page(request):
    """
    Theory page with blog items
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
        isFile = obj.doc is not None
        for word in words:
            text += " " + word
        try:
            size = round(obj.doc.size / 1024, 1)
        except:
            size = 0
            isFile = False
        post = {'title': obj.title,
                'short': text + "...",
                'date': str(obj.published).split('+')[0],
                'isFile': isFile,
                'file': obj.doc,
                'size': size}
        posts.append(post)
    # page — section id. If 0 —> theory page, 1 —> practice page, 2 —> info page
    return render(request, 'main.html', {'posts': posts,
                                         'len': num,
                                         'page': 0})


def practice_page(request):
    """
    practice page with blog items
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
        isFile = obj.doc is not None
        for word in words:
            text += " " + word
        try:
            size = round(obj.doc.size / 1024, 1)
        except:
            size = 0
            isFile = False
        post = {'title': obj.title,
                'short': text + "...",
                'date': str(obj.published).split('+')[0],
                'isFile': isFile,
                'file': obj.doc,
                'size': size}
        posts.append(post)
    return render(request, 'main.html', {'posts': posts,
                                         'len': num,
                                         'page': 1})


def info_page(request):
    """
    info page with blog items
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
        isFile = obj.doc is not None
        for word in words:
            text += " " + word
        try:
            size = round(obj.doc.size / 1024, 1)
        except:
            size = 0
            isFile = False
        post = {'title': obj.title,
                'short': text + "...",
                'date': str(obj.published).split('+')[0],
                'isFile': isFile,
                'file': obj.doc,
                'size': size}
        posts.append(post)
    return render(request, 'main.html', {'posts': posts,
                                         'len': num,
                                         'page': 2})
