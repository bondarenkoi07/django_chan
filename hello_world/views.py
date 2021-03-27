from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotModified
from django.shortcuts import render

from hello_world.form import CommentForm, ThreadForm
from hello_world.models import *


def index(request):
    units = Unit.objects.all().order_by("name")
    return render(request, "base.html", context={"units": units})


def unit(request, _unit):
    unit_obj = Unit.objects.get(name=_unit)
    threads = Thread.objects.filter(unit=unit_obj.id).order_by("priority")
    thread_form = ThreadForm
    units = Unit.objects.all().order_by("name")
    data = {"threads": threads, "form": thread_form, 'units': units}
    return render(request, "unit_template.html", context=data)


def thread(request, _unit, _thread):
    comment = Comment.objects
    thread_list = comment.filter(thread=_thread).order_by("id")
    thread_name = Thread.objects.get(id=_thread)
    form = CommentForm
    units = Unit.objects.all().order_by("name")
    data = {"form": form, "thread": thread_list, "thread_info": {"data": thread_name, "unit": _unit}, "units":units}

    return render(request, "thread_template.html", context=data)


def createComment(request, _unit, _thread):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = Thread.objects.get(id=_thread)
            try:
                mime_type = re.search(r"(.*)/(.*)", request.FILES['media'].content_type)
                comment.media_type = mime_type[1]
            except KeyError:
                comment.media_type = ''
            finally:
                comment.save()
            if 'comments' not in request.session.keys():
                request.session["comments"] = [comment.id]
            else:
                comments_id = request.session["comments"]
                comments_id.append(comment.id)
                request.session["comments"] = comments_id
    return HttpResponseRedirect(f"/{_unit}/{_thread}")


def deleteComment(request, _unit, _thread):
    if request.method == "GET":
        comment_id = request.GET.get("id")
        Comment.objects.filter(id=comment_id).delete()
    return HttpResponseRedirect(f"/{_unit}/{_thread}")


def updateComment(request, _thread, _unit, id):
    if request.method == "POST":
        comment = request.POST.get("text")
        Comment.objects.filter(id=id).update(text=comment)
        return HttpResponseRedirect(f"/{_unit}/{_thread}")
    else:
        return HttpResponseRedirect("/")


def createThread(request, _unit):
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            newThread = form.save(commit=False)
            newThread.date = timezone.now()
            newThread.unit = Unit.objects.get(name=_unit)
            try:
                mime_type = re.search(r"(.*)/(.*)", request.FILES['media'].content_type)
                newThread.media_type = mime_type[1]
            except KeyError:
                newThread.media_type = ''
            finally:
                newThread.save()
            return HttpResponseRedirect(f"/{_unit}/{newThread.id}")
        else:
            return HttpResponseNotModified("<h2>wrong data</h2>")
    else:
        return HttpResponseNotModified("<h2>Empty thread</h2>")


def createUser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        committed_password = request.POST.get("committed_password")
        if password == committed_password and committed_password is not None:
            user = User.objects.create_user(name=name, password=password)
            user.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/?error=wrong_password')
    else:
        return HttpResponseRedirect('/')
