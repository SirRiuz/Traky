


# libs
from consumer import BaseConsumer


# Providers
from providers.movistar.provider import Movistar
from providers.falabella.provider import Falabella
from providers.mac_center.provider import CenterProvider
from providers.tradeinn.provider import Tradeinn




class SmartPhoneConsumer(BaseConsumer):
    
    provider_list = [
        Falabella,
        Movistar,
        CenterProvider,
        Tradeinn
    ]

    
    
    