import map_functions as mf
import random
from DataStructures.List import array_list as al
from DataStructures.Map import map_separate_chaining as sp
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
def find_slot(map,key,hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(map["table"], hash_value)
            if sp.get_key(entry) is None:
               found = True
      elif default_compare(key,sp.get_element(map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % map["capacity"]
   return ocupied, first_avail



def is_available(table, pos):

   entry = al.get_element(table, pos)
   if sp.get_key(entry) is None or sp.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == sp.get_key(entry):
      return 0
   elif key > sp.get_key(entry):
      return 1
   return -1

def put(map,key,value):
    hash_value=mf.hash_value(key)
    find_slot(map,key,hash_value)
    