

# Libs
from models import BaseProductModel
from serializer import BaseSerializer



class MeliSerializer(BaseSerializer):
    
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
        
        
    class Model(BaseProductModel):
        id:str = 'id'
        name:str = 'title'
        preview:str = 'pictures:stack:retina'
        price:float = 'price:amount'
        price_discount:float = 'price:original_price'
        origin:str = 'permalink'
        
        
