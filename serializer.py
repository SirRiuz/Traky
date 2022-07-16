

# Libs
from sekeer import Sekeer


class BaseSerializer:
        
    def __init__(self,**kwargs) -> (None):
        self.__model = kwargs.get('model')
        self.__keyboard = kwargs.get('keyboard','')
        self.data = kwargs.get('data',[])    
          
        
    def serialize(self) -> (list):
                
        if not self.data:
            return []
        
        data = []
        sekeer = Sekeer()
        
        for item in self.data:
            
            origin = sekeer.find(item,self.__model.origin)
            origin = origin.replace('->',':') if origin and type(origin) == str else None
            
            
            preview = sekeer.find(item,self.__model.preview)
            preview = preview.replace('->',':') if preview and type(preview) == str else None
            
            item_data = {
                'id':sekeer.find(item,self.__model.id),
                'name':sekeer.find(item,self.__model.name),
                'price':sekeer.find(item,self.__model.price),
                'origin':origin,
                'preview':preview,
                'free_shipping':sekeer.find(item,self.__model.free_shipping)
            }
            
            
            if type(item_data['price']) == str:
                item_data['price'] = int(
                    item_data['price'].replace('.','')
                )
            
            if item_data['name'] and item_data['price']:
                item_data['name'] = item_data['name'].lower()
                if item_data['name'].count(self.__keyboard) > 0:
                    data.append(item_data)
               
               
                
                
        return data

    
    
    
    