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
    
def get(mapa, key):
    
    """
    Recibe un mapa y una llave, y retorna el valor asociado a la llave.
    
    """
    index = mf.hash_value(mapa, key)
    table = mapa['table']['elements']
    while table[index] is not None:
        if table[index][0] == key:
            return table[index][1]
        index = (index + 1) % mapa['capacity']
    return None

def remove(mapa, key):
    """
    Recibe un mapa y una llave, y elimina la entrada asociada a la llave.
    
    """
    index = mf.hash_value(mapa, key)
    table = mapa['table']['elements']
    while table[index] is not None:
        if table[index][0] == key:
            table[index] = None
            mapa['table']['size'] -= 1
            return
        index = (index + 1) % mapa['capacity']