from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-pk')
	return render(request, 'board/post_list.html', {'posts': posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		post = form.save(commit=False)
		post.published_date = timezone.now()
		post.save()
	else:
		form = PostForm()
	return render(request, 'board/post_new.html', {'form': form})

def post_page(request):
	return