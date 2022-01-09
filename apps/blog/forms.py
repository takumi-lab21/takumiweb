# このファイルには、各種フォームの定義を書く。
from PIL import Image
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:# 編集対象のモデルとフィールドを定義する。
        model = Post
        fields = ('title', 'text', 'image',)
        

