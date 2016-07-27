from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# Create your views here.
from datetime import datetime
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from app_site.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
import random
from django.core.files.base import ContentFile
import os
import os.path
import re
import time
import datetime
import calendar
import json
from django.db.models import Q
import dateutil.parser
from utils import *
from models import *
import mailchimp
from requestHandler import *

def results(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if request.method == "POST":
            skills = request.POST["skills"]
            teensies = TeensiesPosted.objects.filter(skills__icontains=skills).order_by("-featured")
            return render(request, "searchResults.html", {"teensies": teensies})


def save_user_activity(request):
    user_activity = None
    try:
        user = Users.objects.get(pk=request.session['user_id'])
        user_activity = UsersActivity.objects.get(user=user)
    except ObjectDoesNotExist:
        pass

    if user_activity is not None:
        user_activity.date = time.strftime("%Y-%m-%d %H:%M:%S")

        user_activity.save();
    else:
        user_activity = UsersActivity(user=user, date=time.strftime("%Y-%m-%d %H:%M:%S"))
        user_activity.save();


def check(request):
    auth = None
    try:
        auth = request.session['user_id']
    except KeyError:
        pass
    return auth


def users(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allUsers.html", {"user": user, "users":data ,"date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            if 'date'!='0':
                instance=AdminGridControl()
                data=instance.filter_users(request)
            return render(request, "allUsers.html", {"user": user, "users":data ,"date":dateList})


def witgdrawalAdmin(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "withdrawalRequests.html",
                      {"user": user, "withdrawals": WithdrawalRequests.objects.all()})


def releaseAdmin(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET and 'type' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesOrdered.objects.filter(released="request")
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "releaseRequests.html",
                          {"user": user, "withdrawals":data,"date":dateList })
        else:
            instance=AdminGridControl()
            user = Users.objects.get(pk=request.session["user_id"])
            data=instance.filter_requests(request)
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "releaseRequests.html",
                          {"user": user, "withdrawals":data,"date":dateList })


def pages(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        acc_type = AccountType.objects.get(type="Teenlancer")
        return render(request, "pages.html", {"user": user})


def allMembers(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            bronze_type = MembershipType.objects.get(type="Bronze")
            membership = Membership.objects.filter(~Q(membership_type=bronze_type))
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": "All","date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            instance=AdminGridControl()
            membership=instance.filter_membership(request)
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": "All","date":dateList})


def allDisputes(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "allDisputes.html", {"user": user, "disputes": Disputes.objects.all()})


def resolved(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "allDisputes.html",
                      {"user": user, "disputes": Disputes.objects.filter(winner__isnull=False)})


def chatHistory(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        messages = Messages.objects.all()
        dateList={}
        for i in membership:
            dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
        return render(request, "chatsHistory.html", {"user": user, "messages": messages,'date':dateList})


def silverMembers(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        if 'date' not in request.GET:
            silver = MembershipType.objects.get(type="Silver")
            membership = Membership.objects.filter(membership_type=silver)
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": silver.type,"date":dateList})
        else:
            instance=AdminGridControl()
            membership=instance.filter_silver(request)
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": membership.membership_type.type,"date":dateList})


def goldMembers(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        if 'date' not in request.GET:
            gold = MembershipType.objects.get(type="Gold")
            membership = Membership.objects.filter(membership_type=gold)
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": gold.type,"date":dateList})
        else:
            instance=AdminGridControl()
            membership=instance.filter_gold(request)
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": membership.membership_type.type,"date":dateList})


def platinumMembers(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        if 'date' not in request.GET:
            platinum = MembershipType.objects.get(type="Platinum")
            membership = Membership.objects.filter(membership_type=platinum)
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": platinum.type,'date':dateList})
        else:
            instance=AdminGridControl()
            membership=instance.filter_platinum(request)
            dateList={}
            for i in membership:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "allMembers.html", {"user": user, "members": membership, "type": membership.membership_type.type,"date":dateList})

def vas(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.filter(account_type__='Teenlancer')
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "vas.html", {"usetyper": user, "users": data,'date':dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.filter(account_type__='Teenlancer')
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            if 'date'!='0':
                instance=AdminGridControl()
                data=instance.filter_var(request)
            return render(request, "vas.html", {"usetyper": user, "users": data,'date':dateList})


def blacklist(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.filter(status='in-active')
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "black_listed.html", {"usetyper": user, "users": data,'date':dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.filter(status='in-active')
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            if 'date'!='0':
                instance=AdminGridControl()
                data=instance.filter_blackListed(request)
            return render(request, "black_listed.html", {"usetyper": user, "users": data,'date':dateList})


def clients(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.filter(account_type__type="Client")
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "clients.html", {"user": user, "users": data,"date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=Users.objects.filter(account_type__type="Client")
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')

            if 'date'!='0':
                instance=AdminGridControl()
                data=instance.filter_client(request)
            return render(request, "clients.html", {"user": user, "users":data,"date":dateList})



def pins(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesFeatured.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')

            return render(request, "pins.html", {"user": user, "niches": data,"date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesFeatured.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')

            if request.GET['date']!='0':
                instance=AdminGridControl()
                data=instance.filter_pins(request)

            return render(request, "pins.html", {"user": user, "niches": data,"date":dateList})



def trash(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesDeleted.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')

            return render(request, "trash.html", {"user": user, "niches": data,"date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesDeleted.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            if request.GET['date']!='0':
                instance=AdminGridControl()
                data=instance.filter_trash(request)
            return render(request, "trash.html", {"user": user, "niches": data,"date":dateList})



def languages(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "languages.html", {"user": user, "languages": Languages.objects.all()})


def categories(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "categories.html", {"user": user, "categories": Categories.objects.all()})


def cancelAdmin(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesCancelled.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')

            return render(request, "cancellations.html", {"user": user, "niches": data,"date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesCancelled.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')

            if request.GET['date']!='0':
                instance=AdminGridControl()
                data=instance.filter_cancellation(request)

            return render(request, "cancellations.html", {"user": user, "niches": data,"date":dateList})

def niches(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesPosted.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%m-%Y')]=i.date.strftime('%b %Y')
            return render(request, "niches.html", {"user": user, "niches":data,"date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesPosted.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%m-%Y')]=i.date.strftime('%b %Y')
            instance=AdminGridControl()
            if request.GET['date']!='0':
                data=instance.filter_niches(request)
            return render(request, "niches.html", {"user": user, "niches":data,"date":dateList})




def ordersAdmin(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if 'date' not in request.GET:
            user = Users.objects.get(pk=request.session["user_id"])
            orders=TeensiesOrdered.objects.all()
            dateList={}
            for i in orders:
                dateList[i.date.strftime('%b %Y')]=i.date.strftime('%b %Y')
            return render(request, "orders.html", {"user": user, "orders": orders,"date":dateList})
        else:
            user = Users.objects.get(pk=request.session["user_id"])
            data=TeensiesPosted.objects.all()
            dateList={}
            for i in data:
                dateList[i.date.strftime('%m-%Y')]=i.date.strftime('%b %Y')
            instance=AdminGridControl()
            if request.GET['date']!='0':
                data=instance.filter_orders(request)
            return render(request, "orders.html", {"user": user, "niches":data,"date":dateList})



def admin(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])

        yourdate = dateutil.parser.parse(time.strftime("%Y-%m-%d"))
        month = str(yourdate.month - 1)
        date1 = str(yourdate.year) + "-" + month + "-" + str(yourdate.day)
        if yourdate.day > 7:
            day = str(yourdate.day - 7)
            date2 = str(yourdate.year) + "-" + str(yourdate.month) + "-" + day
        else:
            month = str(yourdate.month - 1)
            day = str(yourdate.day + 24)
            date2 = str(yourdate.year) + "-" + month + "-" + day

        posted1 = TeensiesPosted.objects.filter(date__gte=date1)
        posted2 = TeensiesPosted.objects.filter(date__gte=date2)
        posted3 = TeensiesPosted.objects.filter(date__gte=time.strftime("%Y-%m-%d"))
        posted = [len(posted1), len(posted2), len(posted3)]

        ordered1 = TeensiesOrdered.objects.filter(date__gte=date1)
        ordered2 = TeensiesOrdered.objects.filter(date__gte=date2)
        ordered3 = TeensiesOrdered.objects.filter(date__gte=time.strftime("%Y-%m-%d"))
        ordered = [len(ordered1), len(ordered2), len(ordered3)]

        users1 = Users.objects.filter(date__gte=date1)
        users2 = Users.objects.filter(date__gte=date2)
        users3 = Users.objects.filter(date__gte=time.strftime("%Y-%m-%d"))
        users = [len(users1), len(users2), len(users3)]

        bronze_type = MembershipType.objects.get(type="Bronze")
        membership1 = Membership.objects.filter(~Q(membership_type=bronze_type) & Q(date__gte=date1))
        membership2 = Membership.objects.filter(~Q(membership_type=bronze_type) & Q(date__gte=date2))
        membership3 = Membership.objects.filter(
            ~Q(membership_type=bronze_type) & Q(date__gte=time.strftime("%Y-%m-%d")))
        mems = [len(membership1), len(membership2), len(membership3)]

        client_type = AccountType.objects.get(type="Client")
        teenlancer_type = AccountType.objects.get(type="Teenlancer")
        clients = Users.objects.filter(date__gte=date2, account_type=client_type)
        teens = Users.objects.filter(date__gte=date2, account_type=teenlancer_type)

        return render(request, "indexAdmin.html",
                      {"user": user, "posted": posted, "ordered": ordered, "users": users, "niches": posted2,
                       "clients": clients, "teens": teens, "orders": ordered2, "mems": mems})


def uploadImage(request):
    folder = '/home/drowerik3/mysite/media/images'  # request.path.replace("/", "_")
    uploaded_filename = request.FILES['image'].name
    BASE_PATH = '/'
    # create the folder if it doesn't exist.
    try:
        os.mkdir(os.path.join(BASE_PATH, folder))
    except:
        pass

    # save the uploaded file inside that folder.
    full_filename = os.path.join(BASE_PATH, folder, uploaded_filename)
    fout = open(full_filename, 'wb+')
    file_content = ContentFile(request.FILES['image'].read())

    try:
        # Iterate through the chunks.
        for chunk in file_content.chunks():
            fout.write(chunk)
        fout.close()
        user = Users.objects.get(pk=request.session["user_id"])
        user.image = full_filename[22:]
        user.save()
        return HttpResponseRedirect('/profile/')
    except:
        html = "<html><body>NOT SAVED</body></html>"
        return HttpResponse(html)


def day7(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "7-DayPlan.html", {"user": user, "teensie": teensie})


def day14(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "14-DayPlan.html", {"user": user, "teensie": teensie})


def day21(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "21-DayPlan.html", {"user": user, "teensie": teensie})


def day30(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "30-DayPlan.html", {"user": user, "teensie": teensie})


def feature(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if request.method == "POST":
            teensie = TeensiesPosted.objects.get(pk=request.POST["pk"])
            user = Users.objects.get(pk=request.session["user_id"])
            return render(request, "featuredPackages.html", {"user": user, "teensie": teensie})


def accountSettings(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        if request.method == "POST":
            type_flag = request.POST["type_flag"]
            pass_flag = request.POST["pass_flag"]
            email_flag = request.POST["email_flag"]
            error1 = ""

            if type_flag == "1":
                acc_type = None
                if request.POST['client'] == "1":
                    acc_type = AccountType.objects.get(type="Client")
                elif request.POST['teenlancer'] == "1":
                    acc_type = AccountType.objects.get(type="Teenlancer")
                user.account_type = acc_type

            if email_flag == "1":
                email = request.POST["current_email"]
                if user.email == email:
                    user.email = request.POST["new_email"]
                else:
                    error1 = "Wrong current email."

            if pass_flag == "1":
                password = request.POST["current_pass"]
                if password == user.password:
                    user.password = request.POST["new_pass"]
                else:
                    error1 = error1 + "Wrong current password"

            user.save()
            return render(request, "accountSetting.html", {"user": user, "error": error1})

        return render(request, "accountSetting.html", {"user": user})


def profileSettings(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        if request.method == "POST":
            full_name = request.POST["full_name"]
            username = request.POST["username"]
            title = request.POST["title"]
            address = request.POST["address"]
            city = request.POST["city"]
            country = request.POST["country"]
            _zip = request.POST["zip"]
            state = request.POST["state"]
            language = request.POST["language"]
            l = language.split(' ', 1)

            user.first_name = full_name
            user.username = username
            user.title = title
            user.address = address
            user.city = city
            user.country = country
            user.zip_code = _zip
            user.state = state
            lang = None
            try:
                lang = Languages.objects.get(language=l[0])
            except ObjectDoesNotExist:
                pass
            if lang:
                user.language = lang
            user.save()

        return render(request, "profileSetting.html", {"user": user, "langs": Languages.objects.all()})


def membershipSettings(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "membershipSetting.html", {"user": user})


def balance(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        working = 0.0
        available = 0.0
        pending = 0.0
        withdrawn = 0.0

        teensies_posted = TeensiesPosted.objects.filter(user=user)
        for teensie in teensies_posted:
            ordered = TeensiesOrdered.objects.filter(teensie=teensie)
            for order in ordered:
                if order.released == "":
                    working += teensie.price
                else:
                    available += teensie.price

        withdr = WithdrawalRequests.objects.filter(user=user)
        for w in withdr:
            if w.status == "Pending":
                pending += w.amount
            elif w.status == "Confirmed":
                withdrawn += w.amount

        bal = working + available + pending
        balance = [working, available, pending, withdrawn, bal]

        return render(request, "balance.html", {"user": user, "balance": balance})


def withdrawal(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])

        if request.method == "POST":
            amount = request.POST["amount"]
            email = request.POST["email"]
            date = time.strftime("%Y-%m-%d")
            withdraw = WithdrawalRequests(user=user, amount=amount, email=email, status="Pending", date=date)
            withdraw.save()
            return render(request, "withdrawal.html", {"user": user, "result": "Withdrawal request has been sent!"})

        return render(request, "withdrawal.html", {"user": user})


def place_order(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        user = Users.objects.get(pk=request.session["user_id"])
        deposit = teensie.price
        fee = (teensie.price * 2.90) / 100 + 0.37
        total = deposit + fee
        persent = total * 0.05
        total = total + persent
        payment = [round(deposit, 2), round(fee, 2), round(total, 2), round(persent, 2)]
        return render(request, "placeOrder.html", {"user": user, "teensie": teensie, "payment": payment})


def edit_teensie(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        user = Users.objects.get(pk=request.session["user_id"])
        if request.method == "POST":
            name = request.POST["name"]
            description = request.POST["description"]
            skills = request.POST["skills"]
            category = request.POST["category"]
            price = request.POST["price"]
            timeframe = request.POST["timeframe"]

            category_object = Categories.objects.get(category=category)

            teensie.teensie_name = name
            teensie.description = description
            teensie.skills = skills
            teensie.category = category_object
            teensie.price = price
            teensie.timeframe = timeframe
            teensie.save()
            return HttpResponseRedirect("/orders/")

        return render(request, "editTeensie.html",
                      {"user": user, "teensie": teensie, "categories": Categories.objects.all(), })


def delete_teensie(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        teensie.delete()
        return HttpResponseRedirect("/orders/")


def raiseDispute(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        if request.method == "POST":
            teensie = TeensiesPosted.objects.get(pk=request.POST.get('pk'))
            desc = request.POST.get('desc')
            user = Users.objects.get(pk=request.session["user_id"])
            disputes = Disputes.objects.filter(user=user, teensie=teensie)
            response_data = {}
            if len(disputes) != 0:
                response_data['result'] = "error"

                return HttpResponse(
                    json.dumps(response_data, default=date_handler),
                    content_type="application/json"
                )

            dispute = Disputes(user=user, teensie=teensie, description=desc, date=time.strftime("%Y-%m-%d"),
                               payment="No")
            dispute.save()

            response_data['result'] = "success"

            return HttpResponse(
                json.dumps(response_data, default=date_handler),
                content_type="application/json"
            )


def dispute(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, "raiseDispute.html", {"user": user, "teensie": teensie})


def confirmedDispute(request, user_id, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=user_id)
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        teensie.status = "Disputing"
        teensie.save()
        dispute = Disputes.objects.get(user=user, teensie=teensie)
        dispute.payment = "Yes"
        dispute.save()
        return HttpResponseRedirect("/orders/")


def confirmedCancelled(request, user_id, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=user_id)
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        cancelled = TeensiesCancelled(user=user, teensie=teensie, status="Pending", date=time.strftime("%Y-%m-%d"))
        cancelled.save()
        return HttpResponseRedirect("/orders/")


def confirmedFeature(request, user_id, teensie_id, days):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=user_id)
        teensie = TeensiesPosted.objects.get(pk=teensie_id)

        featured = TeensiesFeatured(user=user, teensie=teensie, date=time.strftime("%Y-%m-%d"), days=days)
        featured.save()

        return HttpResponseRedirect("/orders/")


def placed(request, user_id, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=user_id)
        teensie = TeensiesPosted.objects.get(pk=teensie_id)
        teensie.status = "Pending"
        teensie.save()
        ordered = TeensiesOrdered(user=user, teensie=teensie, date=time.strftime("%Y-%m-%d"))
        ordered.save()
        return HttpResponseRedirect("/orders/")


def orders(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        if user.account_type.type == "Client":
            teensies = TeensiesOrdered.objects.filter(user=user)
            return render(request, "ordersPlaced.html", {"user": user, "teensies": teensies})
        else:
            teensies = TeensiesPosted.objects.filter(user=user)
            for teensie in teensies:
                placed = TeensiesOrdered.objects.filter(teensie=teensie)
                teensie.ordered = len(placed)
                teensie.save()
            return render(request, "ordersReceived.html", {"user": user, "teensies": teensies})


def uploadCover(request):
    folder = '/home/drowerik3/mysite/media/images'  # request.path.replace("/", "_")
    uploaded_filename = request.FILES['cover'].name
    BASE_PATH = '/'
    # create the folder if it doesn't exist.
    try:
        os.mkdir(os.path.join(BASE_PATH, folder))
    except:
        pass

    # save the uploaded file inside that folder.
    full_filename = os.path.join(BASE_PATH, folder, uploaded_filename)
    fout = open(full_filename, 'wb+')
    file_content = ContentFile(request.FILES['cover'].read())

    try:
        # Iterate through the chunks.
        for chunk in file_content.chunks():
            fout.write(chunk)
        fout.close()
        user = Users.objects.get(pk=request.session["user_id"])
        user.cover = full_filename[22:]
        user.save()
        return HttpResponseRedirect('/profile/')
    except:
        html = "<html><body>NOT SAVED</body></html>"
        return HttpResponse(html)


def membership(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        membership = Membership.objects.get(user=user)
        save_user_activity(request)
        return render(request, 'plans.html', {"user_plan": membership.membership_type.type, "user": user})


def bronze(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        user = Users.objects.get(pk=request.session["user_id"])
        membership = Membership.objects.get(user=user)
        membership_type = MembershipType.objects.get(pk=1)
        membership.type = membership_type
        membership.save()

        return HttpResponseRedirect('/profile/')


def postTeensie(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        if request.method == "POST":
            name = request.POST["name"]
            description = request.POST["description"]
            skills = request.POST["skills"]
            category = request.POST["category"]
            price = request.POST["price"]
            timeframe = request.POST["timeframe"]

            user = Users.objects.get(pk=request.session["user_id"])
            category_object = Categories.objects.get(category=category)
            current_date = time.strftime("%Y-%m-%d")
            teensie_post = TeensiesPosted(description=description, skills=skills, price=price, timeframe=timeframe,
                                          teensie_name=name, date=current_date, status="Active")

            teensie_post.category = category_object
            teensie_post.user = user
            teensie_post.save()

            link = "/teensie/" + str(teensie_post.pk) + "/"
            return HttpResponseRedirect(link)
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, 'postTeensie.html', {"categories": Categories.objects.all(), "user": user})


def teensie(request, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie_posted = TeensiesPosted.objects.get(pk=teensie_id)
        l = re.compile("\s*,\s*").split(teensie_posted.skills)
        user = Users.objects.get(pk=request.session["user_id"])
        if teensie_posted.user == user:
            return render(request, 'teensie.html', {"teensie": teensie_posted, "skills": l, "user": user})
        else:
            return render(request, 'teensie.html',
                          {"teensie": teensie_posted, "skills": l, "user1": teensie_posted.user, "user": user})


def cancel(request, user_id, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        teensie = TeensiesOrdered.objects.get(pk=teensie_id)
        if int(user_id) == request.session[
            "user_id"] and teensie.teensie.status != "Delivered" and teensie.teensie.status != "Disputing:":
            user = Users.objects.get(pk=int(user_id))
            return render(request, "cancellationFee.html", {"user": user, "teensie": teensie})
        else:
            return HttpResponseRedirect("/orders/")


def silver(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        return render(request, 'silverPlan.html')


def gold(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        return render(request, 'goldPlan.html')


def chat(request):
    if request.method == "POST":

        user1 = request.POST.get('from')
        user2 = request.POST.get('to')

        user_from = Users.objects.get(pk=user1)
        user_to = Users.objects.get(username=user2)

        all_messages = Messages.objects.filter(
            Q(from_user=user_from, to_user=user_to) | Q(to_user=user_from, from_user=user_to))

        array = []

        for message in all_messages:
            response_data = {}
            if message.from_user == user_from:
                response_data['side'] = "right"
            else:
                response_data['side'] = "left"
            response_data['message'] = message.message
            response_data['date'] = message.date
            array.append(response_data)

        return HttpResponse(
            json.dumps(array, default=date_handler),
            content_type="application/json"
        )


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError


def platinum(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        return render(request, 'platinumPlan.html')


def sendMessage(request):
    if request.method == "POST":
        response_data = {}
        message = request.POST.get('message')
        user1 = request.POST.get('from')
        user2 = request.POST.get('to')

        user_from = Users.objects.get(pk=user1)
        user_to = Users.objects.get(username=user2)

        message_object = Messages(from_user=user_from, to_user=user_to, message=message,
                                  date=time.strftime("%Y-%m-%d %H:%M:%S"))
        message_object.save()

        response_data['date'] = message_object.date

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def forgot(request):
    if request.method == 'POST':
        email = request.POST['email']

        check_user_by_email = None

        try:
            check_user_by_email = Users.objects.get(email=email)
        except ObjectDoesNotExist:
            pass

        if check_user_by_email is None:
            return render(request, 'forgotPassword.html', {'error': 'No users with this email'})

        save_user_activity(request)

        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pw_length = 8
        mypw = ""

        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            mypw = mypw + alphabet[next_index]

        message = 'Your new password : ' + mypw
        to = email
        from_email = settings.EMAIL_HOST_USER

        try:
            send_mail("new pass", message, from_email, [to], fail_silently=False)

            check_user_by_email.password = mypw
            check_user_by_email.save()

            return render(request, 'forgotPassword.html', {'notification': 'Check your email for new password.'})

        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    return render(request, 'forgotPassword.html')


def edit_description(request):
    if request.method == 'POST':
        user = Users.objects.get(pk=request.POST['user_id'])
        user.description = request.POST['description']
        user.save()
        return HttpResponseRedirect('/profile/')


def edit_skills(request):
    if request.method == 'POST':
        user = Users.objects.get(pk=request.POST['user_id'])
        user.skills = request.POST['skills']
        user.save()
        return HttpResponseRedirect('/profile/')


def searchEqual(array, current):
    for item in array:
        if item == current:
            return 0
    return 1


def my_teensies(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        user = Users.objects.get(pk=request.session["user_id"])
        teensies = TeensiesPosted.objects.filter(user=user).order_by("-featured")
        return render(request, 'myTeensie.html', {"user": user, "teensies": teensies})


def my_messages(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        user = Users.objects.get(pk=request.session["user_id"])

        dialogs = Messages.objects.order_by('-date').filter(Q(from_user=user) | Q(to_user=user))
        users = []
        messages = []
        final_array = []

        for dialog in dialogs:
            if dialog.from_user == user:
                if searchEqual(users, dialog.to_user) == 1:
                    users.append(dialog.to_user)
            else:
                if searchEqual(users, dialog.from_user) == 1:
                    users.append(dialog.from_user)

        for u in users:
            message = Messages.objects.order_by('-date').filter(Q(from_user=u) | Q(to_user=u))[0]
            buff = [u.image, u.username, message.message, message.date]
            final_array.append(buff)

        if request.method == "POST":
            new_user = Users.objects.get(pk=request.POST["user_id"])
            return render(request, 'myMessages.html',
                          {"user": user, "users": final_array, "messages": messages, "new_user": new_user})

        return render(request, 'myMessages.html', {"user": user, "users": final_array, "messages": messages})


def my_contacts(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        user = Users.objects.get(pk=request.session["user_id"])

        dialogs = Messages.objects.order_by('-date').filter(Q(from_user=user) | Q(to_user=user))
        users = []

        for dialog in dialogs:
            if dialog.from_user == user:
                if searchEqual(users, dialog.to_user) == 1:
                    users.append(dialog.to_user)
            else:
                if searchEqual(users, dialog.from_user) == 1:
                    users.append(dialog.from_user)

        return render(request, 'myContacts.html', {"user": user, "users": users})


def profile(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        user = Users.objects.get(pk=request.session["user_id"])
        user_activity = UsersActivity.objects.get(user=user)
        membership = Membership.objects.get(user=user)
        teensies = TeensiesPosted.objects.filter(user=user)
        rating = 0.0
        count = 0
        for teensie in teensies:
            if teensie.rating :
                rating = (rating + teensie.rating)
                count += 1
        if count > 0:
            rating = rating / count
        if user.skills is not None:
            l = re.compile("\s*,\s*").split(user.skills)
            return render(request, 'profile.html', {"user": user, "skills": l, "value": user_activity.date,
                                                    "user_plan": membership.membership_type.type, "teensies": teensies,
                                                    "rating": rating, "reviews": count})
        else:
            return render(request, 'profile.html',
                          {"user": user, "value": user_activity.date, "user_plan": membership.membership_type.type,
                           "teensies": teensies, "rating": rating, "reviews": count})


def user_page(request, username):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        user = Users.objects.get(username=username)
        current_user = Users.objects.get(pk=request.session["user_id"])
        user_activity = UsersActivity.objects.get(user=user)
        membership = Membership.objects.get(user=user)
        teensies = TeensiesPosted.objects.filter(user=user)
        if user.skills is not None:
            l = re.compile("\s*,\s*").split(user.skills)
            return render(request, 'profile.html', {"user": user, "skills": l, "value": user_activity.date,
                                                    "user_plan": membership.membership_type.type, "teensies": teensies})
        else:
            return render(request, 'profile.html',
                          {"user": user, "value": user_activity.date, "user_plan": membership.membership_type.type,
                           "teensies": teensies})


def appHome(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/')
    else:
        save_user_activity(request)
        return HttpResponseRedirect('/dashboard/')


def index(request):
    auth = check(request)
    if auth:
        save_user_activity(request)
        user = Users.objects.get(pk=request.session["user_id"])
        return render(request, 'index.html', {"user": user})
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        check_user_by_email = None
        check_user_by_username = None

        try:
            check_user_by_email = Users.objects.get(email=email)
        except ObjectDoesNotExist:
            pass

        if check_user_by_email is not None:
            return render(request, 'register.html', {'error': 'This email is already used'})

        try:
            check_user_by_username = Users.objects.get(username=username)
        except ObjectDoesNotExist:
            pass

        if check_user_by_username is not None:
            return render(request, 'register.html', {'error': 'This username is already used'})

        acc_type = None
        if request.POST['client'] == "1":
            acc_type = AccountType.objects.get(type="Client")
        elif request.POST['teenlancer'] == "1":
            acc_type = AccountType.objects.get(type="Teenlancer")

        current_date = time.strftime("%Y-%m-%d")
        new_user = Users(username=username, email=email, account_type=acc_type, password=password, date=current_date)
        new_user.save()

        user_act = UsersActivity(user=new_user, date=time.strftime("%Y-%m-%d"))
        user_act.save()

        membership_type = MembershipType.objects.get(pk=1)
        membership = Membership(user=new_user, membership_type=membership_type, date=time.strftime("%Y-%m-%d"))
        membership.save()



        request.session['user_id'] = new_user.pk
        save_user_activity(request)
        #Add to Mail champ
        if new_user:
            try:
                api = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
                api.lists.subscribe(settings.MAILCHIMP_LIST_ID, {'email': new_user.email})

            except Exception as e:
                str(e)

        return HttpResponseRedirect('/dashboard/');

    return render(request, 'register.html')


def dashboard(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/');
    else:
        save_user_activity(request)
        user = Users.objects.get(pk=request.session["user_id"])
        teensies = TeensiesPosted.objects.filter(user=user).order_by("-featured")
        return render(request, 'dashboard.html', {"user": user, "teensies": teensies})


def releasePayment(request, user_id, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/');
    else:
        teensie = TeensiesOrdered.objects.get(pk=teensie_id)
        if int(user_id) == request.session["user_id"] and teensie.teensie.status != "Delivered":
            teensie.released = "request"
            teensie.teensie.status = "Delivered"
            teensie.teensie.save()
            teensie.save()
            return HttpResponseRedirect("/orders/");
        else:
            return HttpResponseRedirect("/orders/");


def giveFeedback(request, user_id, teensie_id):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/');
    else:
        teensie = TeensiesOrdered.objects.get(pk=teensie_id)
        if int(user_id) == request.session[
            "user_id"] and teensie.teensie.status == "Delivered" and teensie.review == "":
            user = Users.objects.get(pk=request.session["user_id"])
            return render(request, 'giveFeedback.html', {"user": user, "teensie": teensie})
        else:
            return HttpResponseRedirect("/orders/");


def feedback(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/');
    else:
        teensie = TeensiesOrdered.objects.get(pk=request.POST["pk"])
        if teensie.review == "":
            review = request.POST["review"]
            rating = request.POST["rating"]
            teensie.review = review
            teensie.teensie.rating += rating
            teensie.teensie.save()
            teensie.save()
        return HttpResponseRedirect("/orders/");


def logout(request):
    auth = check(request)
    if not auth:
        return HttpResponseRedirect('/login/');
    else:
        save_user_activity(request)
        try:
            del request.session['user_id']
        except KeyError:
            pass
        return render(request, 'logout.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = None

        try:
            user = Users.objects.get(email=email)
        except ObjectDoesNotExist:
            pass

        if user is not None and user.password == password:
            request.session['user_id'] = user.pk

            save_user_activity(request)

            return HttpResponseRedirect('/dashboard/')
        else:
            message = "Fuck you"
            return render(request, 'login.html')
    return render(request, 'login.html')


def facebook_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        facebook_id = request.POST['id']
        name = request.POST['name']
        user = None

        try:
            user = Users.objects.get(facebook_id=facebook_id)
        except ObjectDoesNotExist:
            pass

        if user is not None:
            request.session['user_id'] = user.pk
            save_user_activity(request)
            return HttpResponseRedirect('/dashboard/')
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            pw_length = 8
            username = ""

            for i in range(pw_length):
                next_index = random.randrange(len(alphabet))
                username = username + alphabet[next_index]
            current_date = time.strftime("%Y-%m-%d")
            acc_type = AccountType.objects.get(pk=1)
            new_user = Users(username=username, facebook_id=facebook_id, email=email, account_type=acc_type,
                             password=12345678, date=current_date)
            new_user.save()
            request.session['user_id'] = new_user.pk
            save_user_activity(request)
            return HttpResponseRedirect('/dashboard/')
    return render(request, 'login.html')

@csrf_exempt
def deleteNiches(request):
    if request.POST:
        instance=AdminGridControl()
        return HttpResponse(instance.delete_niches(request))


@csrf_exempt
def restoreNiches(request):
    if request.POST:
        instance=AdminGridControl()
        return HttpResponse(instance.restore_trash(request))
@csrf_exempt
def blacklistUser(request):
    if request.POST:
        instance=AdminGridControl()
        return HttpResponse(instance.blacklist_user(request))

@csrf_exempt
def restoreUser(request):
    if request.POST:
        instance=AdminGridControl()
        return HttpResponse(instance.restore_users(request))
