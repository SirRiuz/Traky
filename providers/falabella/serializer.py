

# Libs
from models import BaseProductModel
from .settings import MEDIA_URL
from serializer import BaseSerializer



class FalabellaSerializer(BaseSerializer):
    

    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
    
        
    class Model(BaseProductModel):
        id:str = 'productId'
        name:str = 'displayName'
        origin:str = 'url'
        price:float = 'prices:0:price:0'
        preview:str = f'{MEDIA_URL} + media:id'




