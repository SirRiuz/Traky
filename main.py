



import time
from consumers.smartphone import *

# #from providers.exito.provider import Exito

start = time.perf_counter()
SmartPhoneConsumer().search(keyboard='redmi note 9'.lower())
end = time.perf_counter()



print(end - start)



