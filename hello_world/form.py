from django import forms

from hello_world.models import *


class ThreadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.fields['media'].required = False

    class Meta:
        model = Thread
        fields = ('name', 'text', 'media')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['media'].required = False

    class Meta:
        model = Comment
        fields = ('text', 'media')
        widgets = {
            'text': forms.Textarea(attrs={ 'rows': 7})
        }