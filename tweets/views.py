from django.shortcuts import render, redirect
from .models import post
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    posts = post.objects.all().order_by('-pk')
    if request.method == "POST":
        post_content = request.POST['tweet']
        author_ = request.user
        post_obj = post(author=author_, content=post_content)
        post_obj.save()
        return redirect('/home')
    else:
        return render(request, 'homepage.html', {'posts': posts})


def delete_post(request,id):
    post_=post.objects.filter(id=id)
    post_.delete()
    return redirect('/home')

