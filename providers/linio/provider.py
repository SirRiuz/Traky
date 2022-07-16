


# Libs
import json
from textwrap import indent
from provider import BaseProvider
from providers.linio.serializer import LinioSerializer
from providers.linio.settings import PAYLOAD_DIR



class Linio(BaseProvider):


    def __init__(self,**kwargs) -> (None):
        self.__keyboard = kwargs.get('keyboard','')
        super().__init__(
            **kwargs,
            payload=PAYLOAD_DIR,
            url='https://api.linio.com/mapi/search',
            method='POST',
            body='''
            {
  "q": "query_keyboard",
  "searchResults": false,
  "sortBy": "relevance",
  "page": 1
}
            '''
        )

    
    def get_data(self) -> (dict):
        print('Get daa')
        response_data = super().get_data()
        data = response_data.get('searchResult',[]) #['searchResult']['original']
        if data:
            data = data['original']['products']
        
        serielizer = LinioSerializer(
            data=data,
            keyboard=self.__keyboard
        ).serialize()
        
        return serielizer
        #open('data.json','w').write(json.dumps(serielizer,indent=2))
        
        

#Linio(keyboard='xbox series x').get_data()
        


  