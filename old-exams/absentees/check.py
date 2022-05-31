import sys
import hashlib
    
    
    
hash = hashlib.sha256()
with open('absentees.txt') as f:
    for line in f:
        hash.update(line.strip().encode('utf-8'))

actual = hash.hexdigest()
print(actual)
   