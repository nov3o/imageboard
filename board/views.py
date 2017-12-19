from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect

def post_list(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			thread = form.save(commit=False)
			thread.published_date = timezone.now()
			thread.save()
			thread.thrd = thread.id
			thread.save(update_fields=['thrd'])
			return redirect('thread_page', thrd=thread.thrd)
	else:
		form = PostForm()

	posts = Post.objects.all()
	thrd_list = list(set([i.thrd for i in posts]))
	last_pk_list = []
	for i in thrd_list:
		post_in_thread = Post.objects.filter(thrd=i)
		last_pk_list.append(post_in_thread[len(post_in_thread)-1].pk)
	sorted_thrd = []
	for i in range(len(thrd_list)):
		sorted_thrd.append(thrd_list[last_pk_list.index(max(last_pk_list))])
		last_pk_list[last_pk_list.index(max(last_pk_list))] = 0
	posts = []
	for i in sorted_thrd:
		posts.append(Post.objects.filter(thrd=i))
	return render(request, 'board/post_list.html', {'posts': posts, 'form': form})

def thread_page(request, thrd):
	posts = Post.objects.filter(thrd=thrd)

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.published_date = timezone.now()
			new_post.save()
			new_post.thrd = thrd
			new_post.save(update_fields=['thrd'])
			return redirect('thread_page', thrd=thrd)
	else:
		form = PostForm()

	return render(request, 'board/thread_page.html', {'posts': posts, 'form': form, 'thrd': thrd})