
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
	posts_list = Post.has_abstract.all()
	paginator = Paginator(posts_list, 10) # 10 posts in each page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)
	return render(request,
		'covid/publications/list.html',
		{'page': page,
		'posts': posts})


def post_detail(request, post, study):
	post = get_object_or_404(Post, 
		slug=post,
		study=study, #authors
		)
	return render(request,
		'covid/publications/detail.html',
		{'post': post})