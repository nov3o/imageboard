from django.shortcuts import render
from django.utils import timezone
from .models import Thread, Post
from .forms import ThreadForm, PostForm
from django.shortcuts import render, redirect

def post_list(request):
	if request.method == "POST":
		form = ThreadForm(request.POST)
		if form.is_valid():
			thread = form.save(commit=False)
			if thread.author == '':
				thread.author = 'Товарищ'
			thread.published_date = timezone.now()
			thread.save()
			return redirect('thread_page', thread_id=thread.id)
	else:
		form = ThreadForm()

	#threads = Thread.objects.all()
	#posts = Post.objects.all()
	pairs = [ [thread, Post.objects.filter(thread_id=thread.id)] for thread in Thread.objects.all() ] 
	# pairs is list of [ op-post, [post-in-thread-except-of-op-post-list] ]
	#later change all() to ord_by('last_pub') 
	"""
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
	"""
	return render(request, 'board/post_list.html', {'form': form, 'pairs': pairs}) 
	#I'll extend QuerySet later

def thread_page(request, thread_id):
	posts = Post.objects.filter(thread_id=thread_id)

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			#Добавить изменение last_pub
			new_post = form.save(commit=False)
			if new_post.author == '':
				new_post.author = 'Товарищ'
			new_post.published_date = timezone.now()
			new_post.thread_id = thread_id
			new_post.save()
			return redirect('thread_page', thread_id=thread_id)
	else:
		form = PostForm()

	return render(request, 'board/thread_page.html', 
		{'posts': posts, 'form': form, 'thread_id': thread_id}
	)