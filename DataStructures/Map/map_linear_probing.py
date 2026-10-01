import random
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_separate_chaining as sp
from DataStructures.List import array_list as al

def new_map (num_elements, load_factor, prime=109345121):
    
    capacidad = mf.next_prime(num_elements / load_factor)
    lista_elementos = []
    
    i = 0
    while i < capacidad:
        lista_elementos.append({
            "key": None,
            "value": None
        })
        i+=1
    
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
    index = hash_value(mapa, key)
    table = mapa["table"]["elements"]
    steps=0
    while table[index] is not None and steps < mapa["capacity"]:
        entry = table[index]
        if entry["key"] == key:
            return entry["value"]
        index = (index + 1) % mapa["capacity"]
        steps += 1

    return None

def remove(mapa, key):
    """
    Recibe un mapa y una llave, y elimina la entrada asociada a la llave.
    
    """
    index = hash_value(mapa, key)
    table = mapa['table']['elements']
    while table[index] is not None:
        if table[index]["key"] == key:
            table[index] = None
            mapa['size'] -= 1
            return
        index = (index + 1) % mapa['capacity']
        
def find_slot(map,key,hash_value):
    first_avail = None
    found = False
    ocupied = False
    i=0
    while i<(map["capacity"]) and not found:
        if is_available(map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(map["table"], hash_value)
            if get_key(entry) is None:
               found = True
        elif default_compare(key,al.get_element(map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
        hash_value = (hash_value + 1) % map["capacity"]
        i+=1
    return ocupied, first_avail

def get_key(entry):
    if entry is None:
        return None
    return entry.get("key", None)



def is_available(table, pos):

   entry = al.get_element(table, pos)
   if get_key(entry) is None or get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == get_key(entry):
      return 0
   elif key > get_key(entry):
      return 1
   return -1
def put(map, key, value):
    pos = hash_value(map, key)
    occupied, first_avail = find_slot(map, key, pos)

    if occupied:
        entry = al.get_element(map["table"], first_avail)
        entry["value"] = value
        al.change_info(map["table"], first_avail, entry)
    else:
        new_entry = {"key": key, "value": value}
        al.change_info(map["table"], first_avail, new_entry)
        map["size"] += 1


def is_empty(map):
    return map["size"] == 0


def key_set(map):
    keys = al.new_list()
    for i in range(map["capacity"]):
        entry = al.get_element(map["table"], i)
        if entry is not None and entry["key"] is not None and entry["key"] != "__EMPTY__":
            al.add_last(keys, entry["key"])
    return keys


def value_set(map):
    values = al.new_list()
    for i in range(map["capacity"]):
        entry = al.get_element(map["table"], i)
        if entry is not None and entry["key"] is not None and entry["key"] != "__EMPTY__":
            al.add_last(values, entry["value"])
    return values


def hash_value(table, key):

    h = hash(key)
    a = table['scale']
    b = table['shift']
    p = table['prime']
    m = table['capacity']
    value = int((abs(h*a + b) % p) % m)
    return value

def contains(map, key):
    index = hash_value(map, key)
    table = map["table"]["elements"]
    steps = 0

    while table[index] is not None and steps < map["capacity"]:
        entry = table[index]
        if entry["key"] == key:
            return True
        index = (index + 1) % map["capacity"]
        steps += 1

    return False

def rehash(map):
    old_table = map["table"]["elements"]
    old_capacity = map["capacity"]

    new_capacity = mf.next_prime(old_capacity * 2)
    mapa= new_map(new_capacity, map["limit_factor"], map["prime"])

    for entry in old_table:
        if entry is not None and entry["key"] is not None and entry["key"] != "__EMPTY__":
            put(mapa, entry["key"], entry["value"])

    return mapa
