from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import Post
from django.contrib.admin.models import LogEntry


def theory_page(request):
    """
    Theory page with blog items
    :param request: request
    :return: JSON with objects
    """
    try:
        query = Post.objects.filter(type=1).order_by('pk')
    except ValueError:
        query = []
    num = len(query)
    posts = []
    for obj in query:
        words = obj.text.split(' ')[:10]
        text = ""
        isFile = len(obj.doc.name) == 0
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
                'name_s': len(obj.doc.name),
                'size': size,
                'text': obj.text}
        posts.append(post)
    # page — section id. If 0 —> theory page, 1 —> practice page, 2 —> info page
    return render(request, 'main.html', {'posts': posts,
                                         'len': num,
                                         'page': 0,
                                         'actions': get_recent_actions()})


def get_recent_actions():
    """
    Returns all recent actions with database
    :return:
    """
    log = LogEntry.objects.all()
    log = [str(obj) for obj in log]
    info = []
    for rec in log:
        if "Added" in rec:
            info.append("Добавлена " + rec.split(sep='Added')[1][2:-2])
        if "Deleted" in rec:
            info.append("Удалена " + rec.split(sep='Deleted')[1][2:-2])
    return info


def practice_page(request):
    """
    practice page with blog items
    :param request: request
    :return: JSON with objects
    """
    try:
        query = Post.objects.filter(type=0).order_by('pk')
    except ValueError:
        query = []
    num = len(query)
    posts = []
    for obj in query:
        words = obj.text.split(' ')[:10]
        text = ""
        isFile = len(obj.doc.name) != 0
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
                'name_s': len(obj.doc.name),
                'size': size,
                'text': obj.text}
        posts.append(post)
    return render(request, 'main.html', {'posts': posts,
                                         'len': num,
                                         'page': 1,
                                         'actions': get_recent_actions()})


def info_page(request):
    """
    info page with blog items
    :param request: request
    :return: JSON with objects
    """
    try:
        query = Post.objects.filter(type=2).order_by('pk')
    except ValueError:
        query = []
    num = len(query)
    posts = []
    for obj in query:
        words = obj.text.split(' ')[:10]
        text = ""
        isFile = len(obj.doc.name) == 0
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
                'name_s': len(obj.doc.name),
                'size': size,
                'text': obj.text}
        posts.append(post)
    return render(request, 'main.html', {'posts': posts,
                                         'len': num,
                                         'page': 2,
                                         'actions': get_recent_actions()})
