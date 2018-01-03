from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):																
	text = forms.CharField(label='Текст', widget=forms.Textarea, error_messages={'required': 'Текст обязателен'})
	title = forms.CharField(label='Заголовок', required=False)

	class Meta:
		model = Thread
		fields = ('author', 'title', 'text',)

class PostForm(forms.ModelForm):																
	text = forms.CharField(label='Текст', widget=forms.Textarea, error_messages={'required': 'Текст обязателен'})

	class Meta:
		model = Post
		fields = ('author', 'text',)