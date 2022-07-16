


# libs
from consumer import BaseConsumer


# Providers
from providers.linio.provider import Linio



class TestConsumer(BaseConsumer):
    
    provider_list = [
        Linio
    ]
