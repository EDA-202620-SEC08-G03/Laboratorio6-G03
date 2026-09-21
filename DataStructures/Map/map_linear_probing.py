import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.Map import map_separate_chaining as sp
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
    
    