


import json
from .settings import MEDIA_URL
from serializer import BaseSerializer


class FalabellaSerializer(BaseSerializer):
    
    
    def __init__(self,**kwargs) -> (None):
        self.__response = kwargs.get('response')
        self.__keyboard = kwargs.get('keyboard','')
        
        
        data = self.serializer()
        
        self.provider_name = 'Falabella'
        self.data = data
        self.size = len(data)
    
    
    def __get_price(self,data) -> (str):
        
        if len(data) > 1:
            return data[1]['price'][0]
        
        return data[0]['price'][0]
    
    
    def serializer(self) -> (None):
                
        data = []
        if not self.__response['data'].get('results'):
            return []
        
        for item in self.__response['data']['results']:
            item_data = {
                'id':item['productId'],
                'name':item['displayName'].lower(),
                'preview':f"{MEDIA_URL}{item['media']['id']}",
                'price':int(
                    self.__get_price(item['prices']).replace('.','')
                ),
                'origin':item['url']
            }
            
            if item_data['name'].count(self.__keyboard) >= 1:
                data.append(item_data)
                
                
        return data




