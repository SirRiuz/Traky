

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


        open('data.json','w').write(json.dumps({
            'size':len(result_list),
            'items':result_list    
        },indent=2))
        # result_list = sorted(
        #     result_list,
        #     key=lambda k:k['price']
        # )
        # print(json.dumps({
        #         'size':len(result_list),
        #         'provider_list':provider_list,
        #         'data':result_list
        #     },indent=2))
        
        
        
        