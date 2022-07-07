



import json
from providers.mac_center.settings import (PROVIDER_BASE_URL,
                                           PROVIDER_NAME)
from serializer import BaseSerializer



class CenterSerailizer(BaseSerializer):
    
    
    def __init__(self,**kwargs) -> None:
        self.____response = kwargs.get('response')
        self.__keyboard = kwargs.get('keyboard')
        super().__init__()
        
        data = self.serializer()
        self.data = data
        self.provider_name = PROVIDER_NAME
        self.size = len(data)

    
    
    def serializer(self) -> (list):
        
        data = []
        for item in self.____response:
            item_data = {
                'id':item['seoUrlSlugDerived'],
                'name':item['displayName'].lower(),
                'preview':f"{PROVIDER_BASE_URL}{item['primaryMediumImageURL']}",
                'origin':f"{PROVIDER_BASE_URL}{item['route']}"
            }

            if item['childSKUs'][0]['salePrice']:
                item_data['price'] = item['childSKUs'][0]['salePrice']
                
            else:
                item_data['price'] = item['listPrice']
            
            
            if item_data['name'].count(self.__keyboard) >= 1:
                data.append(item_data)
            

        return data