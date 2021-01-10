from django.forms import ModelForm

from . models import Blog

class AddPostForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title','img','content')