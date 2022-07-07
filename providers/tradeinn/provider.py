



# Settings
import json

from providers.tradeinn.serializer import TradeinnSerializer
from .settings import (PROVIDER_URL,PAYLOAD_DIR,BODY)

# Libs
from provider import BaseProvider





class Tradeinn(BaseProvider):

    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            body=BODY,
            url=PROVIDER_URL,
            payload=PAYLOAD_DIR,
            method='POST'
        )
        self.serailizer_class = TradeinnSerializer


    def get_data(self) -> (dict):
        response_data = super().get_data()
        serializer = TradeinnSerializer(
            response=response_data,
            keyboard=self.__keyboard    
        )
        return serializer.data



