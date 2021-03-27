import os
import re

from django.db import models
from django.dispatch import receiver
from django.utils import timezone

THREAD_MAX_COUNT = 10


class Unit(models.Model):
    name = models.CharField(max_length=32)


class Thread(models.Model):
    name = models.CharField(max_length=128)
    text = models.CharField(max_length=1024)
    media = models.FileField(upload_to="", default='')
    date = models.DateTimeField(default=timezone.now)
    media_type = models.TextField(max_length="24", default='')
    unit = models.ForeignKey(Unit, models.CASCADE, default='')
    priority = models.SmallIntegerField(null=True)


# TODO: create OP field


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    thread = models.ForeignKey(Thread, models.CASCADE, default=0)
    media = models.FileField(upload_to="", default='')
    date = models.DateTimeField(default=timezone.now)
    media_type = models.TextField(max_length=24, default='')


class ExchangeWord(models.Model):
    pattern = models.CharField(max_length=256, null=True, default=0)
    replacer = models.CharField(max_length=256, null=True, default=0)


@receiver(models.signals.post_delete, sender=Comment)
def delete_comment_callback(sender, instance, **kwargs):
    if instance.media:
        if os.path.isfile(instance.media.path):
            os.remove(instance.media.path)


@receiver(models.signals.post_delete, sender=Thread)
def delete_thread_callback(sender, instance, **kwargs):
    if instance.media:
        if os.path.isfile(instance.media.path):
            os.remove(instance.media.path)


@receiver(models.signals.pre_save, sender=Thread)
def insert_thread_priority(sender, instance, **kwargs):
    num = sender.objects.filter(pk=instance.pk).count()
    if instance.unit and num == 0:
        max_prior = Thread.objects.filter(unit=instance.unit).aggregate(models.Max('priority'))['priority__max']

        if max_prior == THREAD_MAX_COUNT:
            Thread.objects.filter(priority=max_prior).delete()
        elif max_prior == 0 or max_prior is None:
            max_prior = 1
        else:
            max_prior += 1
        instance.priority = max_prior


@receiver(models.signals.pre_save, sender=Comment)
def update_thread_priority(sender, instance, **kwargs):
    replacers = ExchangeWord.objects.all()
    for replacer in replacers.iterator():
        pattern = re.compile(replacer.pattern)
        instance.text = re.sub(pattern, " " + replacer.replacer + " ", instance.text)

    _thread = instance.thread

    if _thread:
        if _thread.priority > 1:
            try:
                thread_list = list(Thread.objects.filter(unit=_thread.unit))
                prev_thread = next(item for item in thread_list if item.priority == _thread.priority - 1)
                prev_thread.priority = _thread.priority
                _thread.priority = _thread.priority - 1
                prev_thread.save()
                _thread.save()
            except TypeError:
                # TODO: create solutions to repair null priority fields during work
                print(_thread)
