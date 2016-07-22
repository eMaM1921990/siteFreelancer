from datetime import datetime
from django.contrib.gis.serializers.geojson import Serializer

__author__ = 'emam'
from utils import *
from models import *
import simplejson
from django.core import serializers




class AdminGridControl():

    #Handle niches action
    def delete_niches(self,request):
        try:
            record=TeensiesPosted.objects.get(id=int(request.POST['id']))
            record.status='in-active'
            record.save()
            #Add to delete posted
            deleted_record=TeensiesDeleted()
            deleted_record.teensie=record
            deleted_record.save()


            return responeJson(True,'Row deleted successfully')
        except Exception as e:
            return responeJson(False,str(e))

    def filter_niches(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=TeensiesPosted.objects.filter(date__year=year,date__month=month)
            return exequery
        except Exception as e:
            print str(e)
            return responeJson(False,str(e))


    #Handle Orders
    def filter_orders(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=TeensiesOrdered.objects.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None

    #Handle Pin
    def filter_pins(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=TeensiesFeatured.objects.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None

    #Handle Cancellation order
    def filter_cancellation(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=TeensiesCancelled.objects.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None

    #Handle trash
    def filter_trash(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=TeensiesDeleted.objects.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None

    #Handle Membership
    def filter_membership(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=Membership.objects.filter(~Q(membership_type__type="Bronze"))
            if request.GET['date']!=0:
               exequery=exequery.filter(date__year=year,date__month=month)
            if request.GET['type']!=0:
               exequery=exequery.filter(membership_type__type=request.GET['type'])
            return  exequery
        except Exception as e:
            return None



    #Handler silver
    def filter_silver(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=Membership.objects.filter(membership_type__type="Silver")
            if request.GET['date']!=0:
               exequery=exequery.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None

    #Handler Gold
    def filter_gold(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=Membership.objects.filter(membership_type__type="Gold")
            if request.GET['date']!=0:
               exequery=exequery.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None


    #Handle platinum
    def filter_platinum(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=Membership.objects.filter(membership_type__type="Platinum")
            if request.GET['date']!=0:
               exequery=exequery.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None

    #Handle reqyuest release
    def filter_requests(self,request):
        try:
            year=str(request.GET['date']).split('-')[1]
            month=str(request.GET['date']).split('-')[0]
            exequery=TeensiesOrdered.objects.filter(released="request")
            if request.GET['date']!=0:
               exequery=exequery.filter(date__year=year,date__month=month)
            return  exequery
        except Exception as e:
            return None




    #handle trash
    def restore_trash(self,request):
        message='Successfully restored selected rows ['
        try:
            dataJson=simplejson.JSONDecoder().decode(request.POST['ids'])
            for index in dataJson:
                #delete from trash
                TeensiesDeleted.objects.get(id=index['id']).delete()
                #restore in main
                record=TeensiesPosted.objects.get(id=int(index['id']))
                record.status='Active'
                record.save()
                message=message+str(record.id)
            message=message+']'
            return responeJson(True,message)
        except Exception as e:
            return responeJson(False,str(e))


    ##handle user
    def blacklist_user(self,request):
        return None







