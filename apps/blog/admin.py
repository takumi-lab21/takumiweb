from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post




# 管理画面の挙動を拡張する
class PostAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" style="width:100px;height:auto;">'.format(obj.image.url))
        else:
            return mark_safe('')
    list_display = list(admin.ModelAdmin.list_display)
    list_display.append("image_preview")
    
# 作成したモデルを登録する
myModels = [Post]
admin.site.register(myModels, PostAdmin)
