from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    MAX_LEN = 100 
    # Postモデルの中身を条件を指定して取得する。
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    for post in posts:
        if len(post.text) > MAX_LEN:
            post.text = post.text[0:MAX_LEN] + "..."
    
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, pk):# pk: primary key
    post = get_object_or_404(Post, pk=pk)# レコードが見つからなかった場合, 404エラーを発生する？
    
    # print( Post._meta.get_fields() ) # カラム一覧を確認
    return render(request, 'blog/post_detail.html', {"post": post})


@login_required # ログインを強制する。
def post_new(request):
    if request.method == "POST":# フォーム情報を受信した場合
        form = PostForm(request.POST, request.FILES) # 通常のデータはこれだけで良い
        if form.is_valid():# 入力データが正しいかどうかをチェックする。
            print(request)
            post = Post()
            post.title  = request.POST["title"]
            post.text   = request.POST["text"]
            post.author = request.user
            post.published_date = timezone.now()
            if "image" in request.FILES:
                post.image  = request.FILES['image']
            post.save()                
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form}) # formクラスを直接渡せば良い。
