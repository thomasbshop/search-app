
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
	posts = Post.published.all()
	return render(request,
		'covid/publications/list.html',
		{'posts': posts})

def post_detail(request, year, month, post):
	post = get_object_or_404(Post, slug=post,
		publish__year=year, # title
		publish__month=month, #authors
		publish__day=day) #reference
	return render(request,
		'covid/publications/detail.html',
		{'post': post})