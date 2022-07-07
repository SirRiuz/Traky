


# Libs
import json
from serializer import BaseSerializer



class TradeinnSerializer(BaseSerializer):
    
    
    def __init__(self,**kwargs) -> None:
        self.__response = kwargs.get('response',[])
        self.__keyboard = kwargs.get('keyboard','')
    
        data = self.serializer()
        self.data = data
        self.provider_name = 'Tradeinn'
        self.size = len(data)
    
    def serializer(self) -> (list):
        
        data = []
        for item in self.__response['results'][0]['hits']:
            name = item['model']['spa'].lower()
            item_data = {
                'id':item['objectID'],
                'name':name,
                'preview':item['src_photo'],
                'price':int(
                    item['precio_str']['precio_43'].replace('COL$','')),
                'origin':item['link_product']
            }
            
            if name.find(self.__keyboard) > 0:
                data.append(item_data)

        return data
