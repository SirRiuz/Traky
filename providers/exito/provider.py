


import json
from provider import BaseProvider
from providers.exito.settings import PROVIDER_URL


class Exito(BaseProvider):
    
    
    def __init__(self, **kwargs) -> None:
        super().__init__(
            **kwargs,
            url=PROVIDER_URL,
            method='GET'
        )
        
        
    def get_data(self) -> dict:
        response_data = super().get_data()
        open('data.json','w').write(
            json.dumps(response_data['queryData'][1]['data'].replace('\"',''),
            indent=2
        ))
        


Exito().get_data()

