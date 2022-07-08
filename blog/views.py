from django.shortcuts import render
from blog.models import post


def home(request):
    entries = post.objects.all().order_by('-timestamp')
    return render(request, 'index.html', {'posts': entries})
