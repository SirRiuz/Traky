

# Libs
import json


class BaseConsumer:

    provider_list = []
    
    def search(self,keyboard:str) -> (list):
        print('Search :',keyboard)
        
        result_list = []
        provider_list = []
        
        for provider_class in self.provider_list:
            provider_object = provider_class(keyboard=keyboard)
            result_list += provider_object.get_data()

        result_list = sorted(
            result_list,
            key=lambda k:k['price']
        )
        print(json.dumps({
                'size':len(result_list),
                'provider_list':provider_list,
                'data':result_list
            },indent=2))
        