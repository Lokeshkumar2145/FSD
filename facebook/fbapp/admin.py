from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(feeds)
admin.site.register(like_msg)


class MemberAdmin(admin.ModelAdmin):
  list_display = ("user", "feed_id", "date_cmt",)
  
admin.site.register(comment, MemberAdmin)