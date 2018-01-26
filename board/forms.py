from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):																
	text = forms.CharField(label='Текст', widget=forms.Textarea, error_messages={'required': 'Текст обязателен'})
	title = forms.CharField(label='Заголовок', required=False)
	image = forms.ImageField(
		label='Пикча', 
		error_messages={
			'invalid_image': 'Файл не является изображением или поврежден',
			'required': 'Пикча обязательна'
		}
	)

	class Meta:
		model = Thread
		fields = ('author', 'title', 'text', 'image')

class PostForm(forms.ModelForm):																
	text = forms.CharField(label='Текст', widget=forms.Textarea, error_messages={'required': 'Текст обязателен'})
	image = forms.ImageField(
		label='Пикча', 
		error_messages={
			'invalid_image': 'Файл не является изображением или поврежден',
		},
		required=False
	)
	replies = forms.CharField(
		label='', 
		required=False, 
		widget=forms.Textarea(attrs={'style':'display: none;'})
	)

	class Meta:
		model = Post
		fields = ('author', 'text', 'image', 'replies')