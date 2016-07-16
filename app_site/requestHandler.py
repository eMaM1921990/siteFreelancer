from datetime import datetime
from django.contrib.gis.serializers.geojson import Serializer

__author__ = 'emam'
from utils import *
from models import *
import simplejson
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
            print request.POST['date'].strftime('%Y')
            print request.POST['date'].strftime('%m')
            exequery=TeensiesPosted.objects.filter(date=datetime.date(request.POST['date'].strftime('%Y'),request.POST['date'].strftime('%m')))
            return Serializer.serialize('json',exequery)
        except Exception as e:
            return responeJson(False,str(e))


    #Handle Orders
    def filter_orders(self,request):
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







