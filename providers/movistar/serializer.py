


# Libs
from models import BaseProductModel
from .settings import ORIGIN_BASE_URL,PROVIDER_BASE_URL
from serializer import BaseSerializer




class MovistarSerializer(BaseSerializer):
    

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
        
        
    class Model(BaseProductModel):
        id:str = 'offeringId'
        name:str = 'offeringName'
        preview:str = f'{PROVIDER_BASE_URL} + :picUrl'
        origin:str = f'{ORIGIN_BASE_URL} + :offeringId'
        price:float = 'monthlyFee'




