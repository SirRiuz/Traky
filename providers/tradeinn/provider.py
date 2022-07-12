


# Settings
from providers.tradeinn.serializer import TradeinnSerializer
from .settings import ( PROVIDER_URL
                       ,PAYLOAD_DIR,
                       BODY )


# Libs
from provider import BaseProvider



class Tradeinn(BaseProvider):

    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,body=BODY,url=PROVIDER_URL,
            payload=PAYLOAD_DIR,method='POST'
        )


    def get_data(self) -> (dict):
        response_data = super().get_data()
        data = response_data['results'][0]['hits']
        result = TradeinnSerializer(
            data=data,
            keyboard=self.__keyboard    
        ).serialize()
        
        
        return result
        # return serializer.data




Tradeinn(keyboard='redmi note'.lower()).get_data()


