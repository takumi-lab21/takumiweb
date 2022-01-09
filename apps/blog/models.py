from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

# データベースのデータ定義を行う
# TODO: 画像を扱えるようにする。
# 参考: 
# https://hisafi.hatenablog.com/entry/2017/07/09/212430
# https://docs.djangoproject.com/ja/4.0/ref/models/fields/#model-field-types

class Post(models.Model):
    # NOTE: ForeignKey
    # 外部キーにより1:多の製薬を与える。
    # 親テーブルに対応する(idの)レコードが存在する場合にのみこのテーブルにデータを追加できる。
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)# 長さが制限されたテキスト
    text = models.TextField()# 長さの制限がないテキスト
    image = models.ImageField(upload_to="images/blog/", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    # NOTE: ForeignKey
    # 外部キーにより1:多の製薬を与える。
    # 親テーブルに対応する(idの)レコードが存在する場合にのみこのテーブルにデータを追加できる。
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField() # 長さの制限がないテキスト
    author = models.CharField(max_length=200)# こちらのテーブルでは、authorは、ただのテキスト
    approved_comment = models.BooleanField(default=False) # 認証済みのコメントであるかどうか
