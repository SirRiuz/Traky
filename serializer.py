

# Libs
import json



class BaseSerializer:
        
    def __init__(self,**kwargs) -> (None):
        self.__model = kwargs.get('model')
        self.__keyboard = kwargs.get('keyboard','')
        self.data = kwargs.get('data',[])    
          


    def __search_by_query(self,data,query) -> (dict):
        
        if not query:
            return None
        
        data = data
        query = query.replace(' ','')
        concat = ''
        
        # Condicionales
        if '+' in query:
            query_data = query.split('+')
            query = query_data[1]
            concat = query_data[0]
            
        
        for q in query.split(':'):
            if q.isnumeric():
                data = data[int(q)]
            else:
                data = data.get(q)
                           
                                
        return f'{concat}{data}'
        
        
        
    def serialize(self) -> (list):
                
        if not self.data:
            return []
        
        data = []
        for item in self.data:
            item_name = self.__search_by_query(
                item,self.__model.name
            ).lower()
            
            if item_name.count(self.__keyboard) > 0:
                data.append({
                    'id':self.__search_by_query(item,self.__model.id),
                    'name':self.__search_by_query(item,self.__model.name),
                    'preview':self.__search_by_query(item,self.__model.preview),
                    'pricing':{
                        'price':self.__search_by_query(item,self.__model.price),
                        'prece_whith_descount':self.__search_by_query(item,self.__model.price_discount)
                    },
                    'origin':self.__search_by_query(item,self.__model.origin),
                    'free_shipping':self.__search_by_query(item,self.__model.free_shipping)
                })
                
                
                
        return data

    
    
    
    