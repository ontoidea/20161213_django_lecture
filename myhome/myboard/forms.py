from django.forms import ModelForm
from myboard.models import Article

class Form(ModelForm):
        class Meta:
            model = Article
            fields = ['name', 'title', 'contents']