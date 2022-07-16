



from models import BaseProductModel
from serializer import BaseSerializer


class LinioSerializer(BaseSerializer):
    
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            model=self.Model
        )
        
        
    
    class Model(BaseProductModel):
        
        id:str = 'sku'
        name:str = 'name'
        price:float = 'previousPrice'
        preview: str = 'image'
        origin: str = 'path'
        free_shipping:bool = 'hasFreeShipping'