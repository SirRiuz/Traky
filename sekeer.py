


class Sekeer:
    
    
    CONCAT_OPERATOR = '+'
    QUERY_OPERATOR = ':'
    TRY_OPERATOR = '>'
    REPLACE_OPERATOR = '#'
    
    
    def __find(self,**kwargs) -> (str):
        data = kwargs.get('data')
        query = kwargs.get('query')
        
        try:
            for q in query.split(':'):
                if q.isnumeric():
                    data = data[int(q)]
                else:
                    if data:
                        data = data.get(q)
                        
            return data
        
        except:
            return
    
    
    def find(self,data:dict,query:str) -> (str):
        
        query = query.replace(' ','')
        
        if query.count(self.CONCAT_OPERATOR) > 0:
            """
              Se encarga de concatenar el valor
              de una query con un string.
                            
              Example:
                -> query:test + foo
                -> value foo
            """
            query_list = query.split(self.CONCAT_OPERATOR)
            query_result = ''
            
            for i in query_list:
                if i.count(self.QUERY_OPERATOR) > 0:
                    i = i
                    if i.startswith(':'):
                        i = i[1::]
                        
                    find_result = self.__find(
                        data=data,
                        query=i
                    )
                    if find_result:
                        query_result += find_result
                    
                    
                else:
                    query_result += i
            
            return query_result
        
        
        if query.count(self.TRY_OPERATOR) > 0:
            """
              Este operador se encarga de probar una lista querys 
              y solo retornara el  valor de una sola query si es 
              diferente de None , de lo contrario seguira probando
              con las demas hasta que la lista termine o 
              el valor sea diferente de None
            """
            query_list = query.split(self.TRY_OPERATOR)
            
            for q in query_list:
                find_result = self.__find(data=data,query=q)
                if find_result:
                    return find_result
                
                
        if query.count(self.REPLACE_OPERATOR) > 0:
            """
              Este operador se encarga de reemplazar un valor
              determinado con nada.
              
              Example:
                -> query:test#replace this
                -> "value query (replacedis)"#replace this
                -> value query
            """
            query_result = ''
            query_list = query.split(self.REPLACE_OPERATOR)
            replace = query_list[1]
            find_result = self.__find(
                data=data,
                query=query_list[0]
            )
            
            if find_result and type(find_result) == str:
                query_result = find_result.replace(replace,'')
            else:
                query_result = find_result
            
            return query_result        
        
        return self.__find(data=data,query=query)






