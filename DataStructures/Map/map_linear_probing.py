import map_functions as mf

def new_map (num_elements, load_factor, prime=109345121):
    
    mapa = {
        'prime': prime,
        'capacity': mf.next_prime(num_elements / load_factor),
        'scale': ,
        'shift': 0,
        'table': {
            'size': 0,
            'elements': [
                
            ]
        }
    }