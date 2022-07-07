



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
            **kwargs,
            body=BODY,
            url=PROVIDER_URL,
            payload=PAYLOAD_DIR,
            method='POST'
        )
        self.serailizer_class = MovistarSerializer


    def get_data(self) -> (dict):
        response_data = super().get_data()
        serialaizer = self.serailizer_class(
            response=response_data,
            keyboard=self.__keyboard
        )
        return serialaizer.data
        #print(json.dumps(serialaizer.data,indent=2))





#result = Movistar(keyboard='Samsung galaxy'.lower())

