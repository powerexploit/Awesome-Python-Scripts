# using python3.7
import hashlib
import json

def generateHash(data):
    blkSerial = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(blkSerial).hexdigest()

# tests
example = {
    'name' : 'Erick Silva',
    'event': 'Hacktoberfest',
    'year' : 2019
}

print( 'Example hash  : ', generateHash(example) )
# proving the property from equal hash to equal inputs
print( 'Example hash 2: ', generateHash(example) )