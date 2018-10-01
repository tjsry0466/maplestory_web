from django_summernote import fields as summer_fields
from django import forms

from .models import Board, Comment

class BoardForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs=
    {
        'placeholder': '제목을 입력해주세요',
        'class': 'input_title'
        }))
# <!-- <input class="input_title" data-val="true" data-val-length="글 제목은 2자 이상, 200자 이하여야 합니다." data-val-length-max="200" data-val-length-min="2" data-val-required="글 제목이 입력되지 않았습니다." id="title" name="title" placeholder="게시물 제목을 입력하세요." type="text" value="" /> -->
    class Meta:
        model = Board
        fields = ('title', 'content')
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('author', 'board',)

