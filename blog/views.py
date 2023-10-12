from django.shortcuts import render
from . import models
from datetime import datetime


def postView(request):
    post_value = models.Post.objects.all()
    context = {
        'post_key': post_value,
    }
    template_name = 'post.html'
    return render(request, template_name, context)
