from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404

def post_list(request):
	posts = Post.objects.all()
	thrd_list = list(set([i.thrd for i in posts]))
	last_pk_list = []
	for i in thrd_list:
		post_in_thread = Post.objects.filter(thrd=i)
		last_pk_list.append(post_in_thread[len(post_in_thread)-1].pk)
	sorted_thrd = []
	for i in range(len(thrd_list)):
		sorted_thrd.append(thrd_list[last_pk_list.index(max(last_pk_list))])
		last_pk_list[last_pk_list.index(max(last_pk_list))] = 0 #
	posts = []
	for i in sorted_thrd:
		posts.append(Post.objects.filter(thrd=i))
	return render(request, 'board/post_list.html', {'posts': posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		post = form.save(commit=False)
		post.published_date = timezone.now()
		post.save()
		post.thrd = post.id
		post.save(update_fields=['thrd'])
	else:
		form = PostForm()
	return render(request, 'board/post_new.html', {'form': form})

def post_page(request, pk):
	post = Post.objects.get(pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST)
		new_post = form.save(commit=False)
		new_post.published_date = timezone.now()
		new_post.save()
		new_post.thrd = post.pk
		new_post.save(update_fields=['thrd'])
	else:
		form = PostForm()

	return render(request, 'board/post_page.html', {'post': post, 'form': form})