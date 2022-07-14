

# Libs
import json


class BaseConsumer:

    provider_list = []
    
    def search(self,keyboard:str) -> (list):
        print('\n\nSearch :',keyboard)
        
        result_list = []
        provider_list = []
        
        
        for provider_class in self.provider_list:
            provider_object = provider_class(keyboard=keyboard)
            result_list += provider_object.get_data()

        result_list = sorted(
            result_list,
            key=lambda k:k['price']
        )

        open('data.json','w').write(json.dumps(result_list,indent=2))
        
        
        