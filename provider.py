

# Libs
import json
from burpeer import parse_request
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings



class BaseProvider:
    
    def __init__(self,**kwargs) -> (None):
        self.payload = kwargs.get('payload','')
        
        self.__body = kwargs.get('body','')
        self.__method = kwargs.get('method','get')
        self.__url = kwargs.get('url','')
        self.__keyboard = kwargs.get('keyboard','')
    
    
    def __get_search_params(self) -> (str):
        return self.__url.replace('query_keyboard',self.__keyboard)

    
    def __get_params(self) -> (dict):
        return json.loads(
            self.__body.replace(
                'query_keyboard',
                self.__keyboard
            )
        )
    
    
    def __on_request(self) -> (dict):
        disable_warnings(InsecureRequestWarning)
        
        try:
            response = None            
            if self.__method == 'POST':
                request_data = parse_request(self.payload)
                headers = request_data[0]
                response = requests.post(
                    headers=headers,
                    timeout=5000,
                    url=self.__url,
                    json=self.__get_params(),
                    verify=False
                )
            
            if self.__method == 'GET':
                response = requests.get(
                    timeout=5000,
                    url=self.__get_search_params(),
                    verify=False
                )
            
            
            if response.ok:
                return json.loads(response.text)
        
        
        except Exception as e:
            print(e)
            return

    
    def get_data(self) -> (dict): 
        return self.__on_request()
    
    
    
    