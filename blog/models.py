from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    # blog object라는 글이 만들어졌지만 이런 식으로 표현이 된다면 어떤 글인지 알아보기 힘듬 __str__ 함수를 사용하여 우리가 원하는 모양으로 바꿈
    def __str__(self):
        return self.title

    # 전체 본문 내용이 담긴 body 대신 100글자로 제한되어있는 summary로 담아 글자 수를 제한
    def summary(self):
        return self.body[:100]