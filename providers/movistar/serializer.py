


# Libs
from .settings import ORIGIN_BASE_URL,PROVIDER_BASE_URL
from serializer import BaseSerializer



class MovistarSerializer(BaseSerializer):
    
    
    def __init__(self,**kwargs) -> None:
        self.__response = kwargs.get('response',[])
        self.__keyboard = kwargs.get('keyboard','')
    
        data = self.serializer()
        self.data = data
        self.provider_name = 'Movistar'
        self.size = len(data)
    
    def serializer(self) -> (list):
        
        data = []
        for item in self.__response['searchResult']:
            if item['offeringName'].lower().count(self.__keyboard) > 0:
                item_data = {
                    'id':item['offeringId'],
                    'name':item['offeringName'],
                    'preview':f"{PROVIDER_BASE_URL}{item['picUrl']}",
                    'price':item['monthlyFee'],
                    'origin':f"{ORIGIN_BASE_URL}{item['offeringId']}"
                }
                
                data.append(item_data)
        
        return data
                
        

