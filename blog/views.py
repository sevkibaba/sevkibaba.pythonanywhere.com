from django.shortcuts import render_to_response

from blog.models import post

def home(request):
    entries = post.objects.all().order_by('-timestamp')
    return render_to_response('index.html', {'posts' : entries})