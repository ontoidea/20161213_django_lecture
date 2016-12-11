from django.shortcuts import render
from myboard.models import Article
from myboard.forms import *
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse


def list(request):
    myborad_list = Article.objects.all().order_by('-cdate')
    return render(request, 'myboard/list.html', {'list': myborad_list})

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            
        return HttpResponseRedirect(reverse('myboard:list'))
    else:
        form = Form()

    return render(request, 'myboard/write.html', {'form': form})

def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'myboard/view.html', {'article': article})