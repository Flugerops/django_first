from django.contrib import admin

from .models import Post, Comment, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin): ...


class CommentAdmin(admin.ModelAdmin): ...


class TagAdmin(admin.ModelAdmin): ...


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
