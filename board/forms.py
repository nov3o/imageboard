from django import forms
from .models import Post

class PostForm(forms.ModelForm):																
	text = forms.CharField(label='Текст', widget=forms.Textarea, error_messages={'required': 'Текст обязателен'})
	title = forms.CharField(label='Заголовок', required=True, error_messages={'required': 'Заголовок обязателен'})

	class Meta:
		model = Post
		fields = ('author', 'title', 'text',)

class Reply(forms.ModelForm):																
	text = forms.CharField(label='Текст', widget=forms.Textarea, error_messages={'required': 'Текст обязателен'})

	class Meta:
		model = Post
		fields = ('author', 'text',)