import map_functions as mf
import random

def new_map (num_elements, load_factor, prime=109345121):
    
    mapa = {
        'prime': prime,
        'capacity': mf.next_prime(num_elements / load_factor),
        'scale': random.randint(1, prime - 1),
        'shift': random.randint(0, prime - 1),
        'table': {
            'size': 0,
            'elements': [
                
            ]
        },
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0     
    }
    
    for i in range(mapa['capacity']):
        diccionario = {
            ''
        }
    
    return mapa