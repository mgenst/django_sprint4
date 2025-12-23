from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'location', 'category', 'image')
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = self.fields['category'].queryset.filter(
            is_published=True
        )
        self.fields['location'].queryset = self.fields['location'].queryset.filter(
            is_published=True
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'text': 'Текст комментария',
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
            'email': 'Адрес электронной почты',
        }
        help_texts = {
            'username': 'Обязательное поле. Только буквы, цифры и символы @/./+/-/_.',
        }
