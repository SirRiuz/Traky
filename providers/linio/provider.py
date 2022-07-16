


# Libs
from provider import BaseProvider
from providers.linio.serializer import LinioSerializer
from providers.linio.settings import PAYLOAD_DIR,BODY,PROVIDER_URL



class Linio(BaseProvider):


    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            payload=PAYLOAD_DIR,
            url=PROVIDER_URL,
            method='POST',
            body=BODY
        )

    
    def get_data(self) -> (dict):
        print('Get daa')
        response_data = super().get_data()
        data = response_data.get('searchResult',[])
        if data:
            data = data['original']['products']
        
        serielizer = LinioSerializer(
            data=data,
            keyboard=self.__keyboard
        ).serialize()
        
        return serielizer

  
  
  