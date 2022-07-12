


# Libs
from models import BaseProductModel
from serializer import BaseSerializer






class TradeinnSerializer(BaseSerializer):
    
    def __init__(self,**kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
            
    class Model(BaseProductModel):
        id:str = 'objectID'
        name:str = 'model:spa'
        preview:str = 'src_photo'
        origin:str = 'link_product'
        price:float = 'precio_str:precio_43'




