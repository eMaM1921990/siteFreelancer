"""siteFreelancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include,patterns


# Uncomment the next two lines to enable the admin:
import app_site
from app_site.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', app_site.views.appHome, name='home'),
    url(r'^index/', app_site.views.index, name='index'),
    url(r'^register/', app_site.views.register, name='register'),
    url(r'^login/', app_site.views.login, name='login'),
    url(r'^facebook_login/', app_site.views.facebook_login, name='facebook_login'),
    url(r'^dashboard/', app_site.views.dashboard, name='dashboard'),

    url(r'^logout/', app_site.views.logout, name='logout'),

    url(r'^profile/', app_site.views.profile, name='profile'),

    url(r'^u/(?P<username>[0-9a-zA-Z]+)/', app_site.views.user_page, name='user_page'),

    url(r'^myMessages/', app_site.views.my_messages, name='my_messages'),
    url(r'^myTeensies/', app_site.views.my_teensies, name='my_teensies'),
    url(r'^accountSettings/', app_site.views.accountSettings, name='accountSettings'),
    url(r'^membershipSettings/', app_site.views.membershipSettings, name='membershipSettings'),
    url(r'^profileSettings/', app_site.views.profileSettings, name='profileSettings'),


    url(r'^balance/', app_site.views.balance, name='balance'),
    url(r'^withdrawal/', app_site.views.withdrawal, name='withdrawal'),

    url(r'^uploadImage/', app_site.views.uploadImage, name='uploadImage'),
    url(r'^uploadCover/', app_site.views.uploadCover, name='uploadCover'),

    url(r'^uploadCover/', app_site.views.uploadCover, name='uploadCover'),

    url(r'^feedback/', app_site.views.feedback, name='feedback'),

    url(r'^cancel/(?P<user_id>[0-9]+)/(?P<teensie_id>[0-9]+)/', app_site.views.cancel, name='cancel'),


    url(r'^confirmedDispute/(?P<user_id>[0-9]+)/(?P<teensie_id>[0-9]+)/', app_site.views.confirmedDispute, name='confirmedDispute'),

    url(r'^releasePayment/(?P<user_id>[0-9]+)/(?P<teensie_id>[0-9]+)/',app_site.views.releasePayment, name='releasePayment'),

    url(r'^giveFeedback/(?P<user_id>[0-9]+)/(?P<teensie_id>[0-9]+)/', app_site.views.giveFeedback, name='giveFeedback'),


    url(r'^confirmedFeature/(?P<user_id>[0-9]+)/(?P<teensie_id>[0-9]+)/(?P<days>[0-9]+)/', app_site.views.confirmedFeature, name='confirmedFeature'),

    url(r'^confirmedCancelled/(?P<user_id>[0-9]+)/(?P<teensie_id>[0-9]+)/', app_site.views.confirmedCancelled, name='confirmedCancelled'),



    url(r'^placedOrder/(?P<user_id>[0-9]+)/(?P<teensie_id>[0-9]+)/', app_site.views.placed, name='placed'),

    url(r'^raise/', app_site.views.raiseDispute, name='raiseDispute'),

    url(r'^editTeensie/(?P<teensie_id>[0-9]+)/', app_site.views.edit_teensie, name='edit_teensie'),
    url(r'^deleteTeensie/(?P<teensie_id>[0-9]+)/', app_site.views.delete_teensie, name='delete_teensie'),

    url(r'^7-Day/(?P<teensie_id>[0-9]+)/', app_site.views.day7, name='day7'),
    url(r'^14-Days/(?P<teensie_id>[0-9]+)/', app_site.views.day14, name='day14'),
    url(r'^21-Days/(?P<teensie_id>[0-9]+)/', app_site.views.day21, name='day21'),
    url(r'^30-Days/(?P<teensie_id>[0-9]+)/', app_site.views.day30, name='day30'),

    url(r'^admin/releaseRequests/', app_site.views.releaseAdmin, name='releaseAdmin'),
    url(r'^admin/withdrawalRequests/', app_site.views.witgdrawalAdmin, name='witgdrawalAdmin'),
    url(r'^admin/resolved/', app_site.views.resolved, name='resolved'),
    url(r'^admin/allDisputes/', app_site.views.allDisputes, name='allDisputes'),
    url(r'^admin/chatHistory/', app_site.views.chatHistory, name='chatHistory'),
    url(r'^admin/allMembers/', app_site.views.allMembers, name='allMembers'),
    url(r'^admin/silver/', app_site.views.silverMembers, name='silverMembers'),
    url(r'^admin/gold/', app_site.views.goldMembers, name='goldMembers'),
    url(r'^admin/platinum/', app_site.views.platinumMembers, name='platinumMembers'),

    url(r'^admin/languages/', app_site.views.languages, name='languages'),
    url(r'^admin/categories/', app_site.views.categories, name='categories'),
    url(r'^admin/pages/', app_site.views.pages, name='pages'),
    url(r'^admin/users/', app_site.views.users, name='users'),
    url(r'^admin/clients/', app_site.views.clients, name='clients'),
    url(r'^admin/vas/', app_site.views.vas, name='vas'),
    url(r'^admin/blacklist/', app_site.views.blacklist, name='blacklist'),

    url(r'^admin/trash/', app_site.views.trash, name='trash'),
    url(r'^admin/cancellations/', app_site.views.cancelAdmin, name='cancelAdmin'),
    url(r'^admin/pins/', app_site.views.pins, name='pins'),
    url(r'^admin/niches/', app_site.views.niches, name='niches'),
    url(r'^admin/orders/', app_site.views.ordersAdmin, name='ordersAdmin'),

    url(r'^admin/', app_site.views.admin, name='admin'),

    url(r'^feature/', app_site.views.feature, name='feature'),

    url(r'^dispute/(?P<teensie_id>[0-9]+)/', app_site.views.dispute, name='dispute'),

    url(r'^orders/', app_site.views.orders, name='orders'),

    url(r'^postTeensie/', app_site.views.postTeensie, name='postTeensie'),
    url(r'^teensie/(?P<teensie_id>[0-9]+)/', app_site.views.teensie, name='teensie'),

    url(r'^forgot/', app_site.views.forgot, name='forgot'),

    url(r'^placeOrder/(?P<teensie_id>[0-9]+)/', app_site.views.place_order, name='place_order'),

    url(r'^membership/', app_site.views.membership, name='membership'),
    url(r'^bronze/', app_site.views.bronze, name='bronze'),
    url(r'^gold/', app_site.views.gold, name='gold'),
    url(r'^silver/', app_site.views.silver, name='silver'),
    url(r'^platinum/', app_site.views.platinum, name='platinum'),

    url(r'^edit_description/', app_site.views.edit_description, name='edit_description'),
    url(r'^edit_skills/', app_site.views.edit_skills, name='edit_skills'),

    url(r'^results/', app_site.views.results, name='results'),

    url(r'^sendMessage/', app_site.views.sendMessage, name='sendMessage'),

    url(r'^myContacts/', app_site.views.my_contacts, name='my_contacts'),

    url(r'^chat/', app_site.views.chat, name='chat'),




    # Grid Control
    url(r'^delete_niches/', app_site.views.deleteNiches, name='deleteNiches'),
    url(r'^restore_niches/', app_site.views.restoreNiches, name='restoreNiches'),
    url(r'^blacklist_user/', app_site.views.blacklistUser, name='blacklistUser'),
    url(r'^restore_user/', app_site.views.restoreUser, name='restoreUser'),

    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin2/', include(admin.site.urls)),
)