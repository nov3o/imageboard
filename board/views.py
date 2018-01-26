from django.utils import timezone
from .models import Thread, Post
from .forms import ThreadForm, PostForm
from django.shortcuts import render, redirect

def reply_format(reply, thread_number, post_number):
	lst = list(set(reply.split()))
	post_list = [
		str(post.count_number) for post in Post.objects.filter(thread_number=thread_number)
	]
	post_list.append(thread_number)
	lst = [i for i in lst if i in post_list]
	for count_number in lst:
		if count_number == str(thread_number):
			post = Thread.objects.get(count_number=int(thread_number))
		else:
			post = Post.objects.get(count_number=int(count_number))
		post.replies += str(post_number) + ' '
		post.save()

def post_list(request):
	if request.method == "POST":
		form = ThreadForm(request.POST, request.FILES)
		if form.is_valid():
			thread = form.save(commit=False)
			if thread.author == '':
				thread.author = 'Товарищ'
			thread.published_date = timezone.now()
			thread.last_publish = thread.published_date
			thread.count_number = get_max(Post.objects.all(), Thread.objects.all())
			thread.save()
			return redirect('thread_page', thread_number=thread.count_number)
	else:
		form = ThreadForm()

	thread_nodes = []
	for thread in Thread.objects.all().order_by('-last_publish'):
		posts = Post.objects.filter(thread_number=thread.count_number)
		if len(posts) > 5:
			showed_posts = posts[len(posts)-5:]
			missed = len(posts) - len(showed_posts)
		else:
			showed_posts = posts
			missed = 0
		thread_nodes.append([thread, showed_posts, missed])

	return render(request, 'board/post_list.html', 
		{'form': form, 'thread_nodes': thread_nodes}
	)


def thread_page(request, thread_number):
	posts = Post.objects.filter(thread_number=thread_number)
	post_nodes = []
	for i in posts:
		post_nodes.append([i, i.replies.split()])
	op = Thread.objects.get(count_number=thread_number)

	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			new_post = form.save(commit=False)
			if new_post.author == '':
				new_post.author = 'Товарищ'
			new_post.published_date = timezone.now() 
			new_post.thread_number = thread_number
			new_post.count_number = get_max(Post.objects.all(), Thread.objects.all())
			if new_post.replies:
				reply_format(new_post.replies, thread_number, new_post.count_number)
				new_post.replies = ''
			new_post.save()

			op.last_publish = new_post.published_date
			op.save(update_fields=["last_publish"])

			return redirect('thread_page', thread_number=thread_number)
	else:
		form = PostForm()

	return render(request, 'board/thread_page.html', 
		{'post_nodes': post_nodes, 'form': form, 'thread_number': thread_number, 'op': op}
	)


def get_max(posts, threads):
	lst = [i[len(i)-1].count_number for i in [posts, threads] if len(i) != 0]
	if lst == []:
		return 1
	else:
		return max(lst)+1