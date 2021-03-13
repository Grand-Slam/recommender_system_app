# form을  이용해 입력공간 만들기
from django import forms
from .models import Blog

# 모델을 기반으로한 입력 공간 만들기
# Blog 모델 중에서 title과 body를 입력받을 수 있는 공간을 만들겠다는 의미
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']