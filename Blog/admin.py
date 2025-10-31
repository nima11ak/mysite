from django.contrib import admin
from Blog.models import post



# class PostAdmin(admin.ModelAdmin):
#     date_hierarchy = "created_date"
#     empty_value_display = '-'
#     # fields =('title',)
#     list_display = ('title','counted_views','status','published_date','created_date')
#     list_filter  =('status',)
#     search_fields =('title','content',)

class ContactAdmin(admin,ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('name','email','created_date') 
    list_filter  =('email',)
    search_fields =('name','message')

admin.site.register(Contact,ContactAdmin)

