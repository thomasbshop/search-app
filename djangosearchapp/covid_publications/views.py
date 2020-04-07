
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
	posts = Post.has_abstract.all()
	return render(request,
		'covid/publications/list.html',
		{'posts': posts})

def post_detail(request, post, study):
	post = get_object_or_404(Post, 
		slug=post,
		study=study, #authors
		)
	return render(request,
		'covid/publications/detail.html',
		{'post': post})