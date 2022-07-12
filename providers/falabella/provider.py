


# Libs
from providers.falabella.settings import PROVIDER_URL
from .serializer import FalabellaSerializer
from provider import BaseProvider



class Falabella(BaseProvider):


    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='GET'
        )

    
    def get_data(self) -> (dict):
        response_data = super().get_data()
        data = response_data['data'].get('results',[])      
        serializer = FalabellaSerializer(
            data=data,
            keyboard=self.__keyboard
        ).serialize()
        
        return serializer




