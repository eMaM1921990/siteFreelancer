from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app_site.models import *



class UsersEnt(admin.ModelAdmin):
    list_display = ['username','first_name','facebook_id','email','password','account_type','city','country','language','address','state','zip_code']
    ordering = ['first_name']
    search_fields = ['first_name','username','email']


class PostedEnt(admin.ModelAdmin):
    list_display = ['teensie_name','status','timeframe','price','date','category','user','description','skills','ordered','rating','featured']
    ordering = ['teensie_name']
    search_fields = ['teensie_name','price','category']


class DisputeEnt(admin.ModelAdmin):
    list_display = ['user','payment','date','teensie','winner']
    ordering = ['teensie']
    search_fields = ['teensie_name']

class MessEnt(admin.ModelAdmin):
    list_display = ['from_user','to_user','message','date']
    ordering = ['from_user']
    search_fields = ['message','from_user','to_user']

class FeatEnt(admin.ModelAdmin):
    list_display = ['user','teensie','days','date']
    ordering = ['teensie']
    search_fields = ['teensie','user']

class OrdEnt(admin.ModelAdmin):
    list_display = ['user','teensie','released','review']
    ordering = ['teensie']
    search_fields = ['teensie','user']

class WithEnt(admin.ModelAdmin):
    list_display = ['user','email','amount','status','date']
    ordering = ['user']
    search_fields = ['email','user']

class MemEnt(admin.ModelAdmin):
    list_display = ['membership_type','user','date']
    ordering = ['user']
    search_fields = ['membership_type','user']

class ActEnt(admin.ModelAdmin):
    list_display = ['user','date']
    ordering = ['user']
    search_fields = ['user']


admin.site.register(Users, UsersEnt )
admin.site.register(Languages)
admin.site.register(AccountType)
admin.site.register(UsersActivity, ActEnt)
admin.site.register(MembershipType)
admin.site.register(Membership, MemEnt)
admin.site.register(Categories)
admin.site.register(TeensiesPosted, PostedEnt)
admin.site.register(Messages,MessEnt)
admin.site.register(Disputes, DisputeEnt)
admin.site.register(TeensiesOrdered, OrdEnt)
admin.site.register(TeensiesFeatured, FeatEnt)
admin.site.register(WithdrawalRequests, WithEnt)
admin.site.register(TeensiesCancelled)