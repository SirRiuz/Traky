



#Libs
import json
from provider import BaseProvider
from providers.exito.serializer import ExitoSerializer
from providers.exito.settings import PROVIDER_URL




class Exito(BaseProvider):
    
    
    def __init__(self, **kwargs) -> (None):
        self.__keyboard =kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='GET'
        )
        
    def get_data(self) -> (dict):
        response_data = super().get_data()
        data = json.loads(
            response_data['queryData'][0]['data']
        )['productSearch']['products']
        data = ExitoSerializer(
            data=data,
            keyboard=self.__keyboard
        ).serialize()        
        
        return data
        
        
        



