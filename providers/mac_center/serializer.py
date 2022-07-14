



# Libs
from models import BaseProductModel
from providers.mac_center.settings import (PROVIDER_BASE_URL)
from serializer import BaseSerializer



class CenterSerailizer(BaseSerializer):
    

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
        
    class Model(BaseProductModel):
        id:str = 'seoUrlSlugDerived'
        name:str = 'displayName'
        preview:str = f'{PROVIDER_BASE_URL} + :primaryMediumImageURL'
        origin:str = f'{PROVIDER_BASE_URL} + :route'
        price:float = 'childSKUs:0:salePrice > childSKUs:0:listPrice'




