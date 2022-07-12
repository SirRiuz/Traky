


# libs
from consumer import BaseConsumer


# Providers
from providers.movistar.provider import Movistar
from providers.falabella.provider import Falabella
from providers.mac_center.provider import MacCenter
from providers.tradeinn.provider import Tradeinn
from providers.exito.provider import Exito
from providers.mercadolibre.provider import MercadoLibre




class SmartPhoneConsumer(BaseConsumer):
    
    provider_list = [
        Falabella,
        Movistar,
        MacCenter,
        Tradeinn,
        MercadoLibre,
        Exito
    ]

    
    
    