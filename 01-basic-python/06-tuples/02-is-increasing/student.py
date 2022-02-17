# Write your code here
def is_increasing(ns):
    for x in range(len(ns)-1):
        if ns[x] > ns[x+1]:
            return False
    return True  