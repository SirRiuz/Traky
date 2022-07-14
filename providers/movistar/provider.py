



# Settings
import json
from .settings import (BODY,PAYLOAD_DIR,PROVIDER_URL)

# Libs
from provider import BaseProvider


# Serializer
from .serializer import MovistarSerializer




class Movistar(BaseProvider):

        
    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,body=BODY,url=PROVIDER_URL,
            payload=PAYLOAD_DIR,method='POST'
        )


    def get_data(self) -> (dict):
        response_data = super().get_data()['searchResult']
        serialaizer = MovistarSerializer(
            data=response_data,
            keyboard=self.__keyboard
        ).serialize()
        
        return serialaizer







