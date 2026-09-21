import map_functions as mf
import random

def new_map (num_elements, load_factor, prime=109345121):
    
    capacidad = mf.next_prime(num_elements / load_factor)
    lista_elementos = []
    
    i = 0
    while i < capacidad:
        lista_elementos.append({
            "key": None,
            "value": None
        })
    
    mapa = {
        'prime': prime,
        'capacity': capacidad,
        'scale': random.randint(1, prime - 1),
        'shift': random.randint(0, prime - 1),
        'table': {
            'size': 0,
            'elements': lista_elementos
        },
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0     
    }
    
    return mapa
    
def size (my_map):
    
    tamaño = my_map["size"]
    
    return tamaño
    
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