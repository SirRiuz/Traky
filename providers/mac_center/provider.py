

# Libs
from provider import BaseProvider
from providers.mac_center.serializer import CenterSerailizer
from providers.mac_center.settings import PROVIDER_URL



class MacCenter(BaseProvider):
    
    
    def __init__(self, **kwargs) -> None:
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            method='GET',
            url=PROVIDER_URL
        )
        
        
    def get_data(self) -> (dict):
        response_data = super().get_data()['items']
        data = CenterSerailizer(
            data=response_data,
            keyboard=self.__keyboard
        ).serialize()
        
        return data



