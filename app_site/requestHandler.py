__author__ = 'emam'
from utils import *
from models import *
class AdminGridControl():

    #Handle niches action
    def delete_niches(self,request):
        try:
            record=TeensiesPosted.objects.get(id=int(request.POST['id']))
            record.delete()
            return responeJson(True,'Row deleted successfully')
        except Exception as e:
            return responeJson(False,str(e))


