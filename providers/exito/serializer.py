


# Libs
from models import BaseProductModel
from serializer import BaseSerializer



class ExitoSerializer(BaseSerializer):
    
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
        
    class Model(BaseProductModel):
        
        id:str = 'productId'
        name:str = 'productName'
        origin:str = 'link'
        
        price_discount:float = 'priceRange:sellingPrice:lowPrice'
        price:float = 'priceRange:listPrice:lowPrice'
        
        preview:str = 'items:0:images:0:imageUrl'


