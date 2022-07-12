


# Libs
from provider import BaseProvider
from providers.mercadolibre.serializer import MeliSerializer
from .settings import PROVIDER_URL,PAYLOAD_DIR



class MercadoLibre(BaseProvider):
    

    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='GET',payload=PAYLOAD_DIR
        )

    
    def get_data(self) -> (dict):
        response_data = super().get_data()
        response_data = response_data['results']
        
        data = MeliSerializer(
            data=response_data,
            keyboard=self.__keyboard
        ).serialize()
        
        
        return data
    
    
    
    