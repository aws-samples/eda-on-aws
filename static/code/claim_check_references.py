# Library to generate unique identifiers
import uuid

# Simulate the information store
full_storage: dict = dict()

# A function to store the information in a pending status and return a reference
def storage_first(object: dict):
    reference = uuid.uuid4().hex

    full_storage[reference] = ['PENDING', object]

    return reference

# A function to enrich the original message and status according to its reference
def enrich_later(reference: str, new_object: dict):
    try:
        full_storage[reference][1].update(new_object)
        full_storage[reference][0] = 'OK'
    except KeyError as ke:
        return False

    return True

# First object to be stored
object1 = {"name": "John"}

# Store the first object
ref1 = storage_first(object1)

# Watch the store with the first object in pending status
print(f'Store: {full_storage}')

# Store the second object
object2 = {"name": "Jane"}

# Intentionally we don't store the reference
storage_first(object2)
# Should be this way
# ref2 = storage_first(object2)

# Watch the store with two objects in pending status
print(f'Store: {full_storage}')

# Enrich only the first object as we have no reference for the second object
enrich_later(ref1, {"age": 30})

# Watch the store with two objects, the first in OK status and the second in pending status
print(f'Store: {full_storage}')
