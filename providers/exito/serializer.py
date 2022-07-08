


# Libs
import json
from serializer import BaseSerializer



class ExitoSerializer(BaseSerializer):
    
    
    def __init__(self,**kwargs) -> None:
        self.__response = kwargs.get('response',[])
        self.__keyboard = kwargs.get('keyboard','')
    
        data = self.serializer()
        self.data = data
        self.provider_name = 'Exito'
        self.size = len(data)
    
    def serializer(self) -> (list):
        
        
        if not self.__response:
            return []
        
        data = []
        for item in self.__response['productSearch']['products']:
            item_data = {
                'id':item['productId'],
                'name':item['productName'].lower(),
                'origin':item['link'],
                'price':item['priceRange']['sellingPrice']['lowPrice'],
                'preview':item['items'][0]['images'][0]['imageUrl']
            }
            
            if item_data['name'].count(self.__keyboard) > 0:
                data.append(item_data)
            
            
        return data





