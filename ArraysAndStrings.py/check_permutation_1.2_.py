
# covert the string into char array and sort it join it and return the string
# same are the step in C# and java
def sort(s)->str:
    s = list(s)
    s.sort()
    return ''.join(s)

# come to an agremetn on input and output,
# what should be the output when strings are null or empty
# I am assuming I have to return False when strings are null or empty
def is_permutation(a,b)->bool:

    if a == None or b == None or len(a) ==0  or len(b) == 0 or len(a)!=len(b):
        return False
    
    # sort takes O(nlogn) time and comparison takes O(n), time complexity would be O(nlogn)
    # space complexity is dependent on the sort algorithm used, if it is inplace then constant time else linear time
    if sort(a) != sort(b):
        return False
    else:
        return True

# linear time and space
def is_permutation1(a,b)->bool:

    if a == None or b == None or len(a) ==0  or len(b) == 0 or len(a)!=len(b):
        return False
    # to keep track of number of occurences of the character in string
    # an array of integers of length 128 or 256 can also be used.
    hash_map = dict()

    for c in a:
        if c in hash_map:
            hash_map[c] +=1
        else:
            hash_map[c] = 1

    for c in b:
        if c not in hash_map:
            return False
        val = hash_map[c] -1
        # if value is negative then there is character which repeated more times than it is in string a
        if val < 0:
            return False

        hash_map[c] = val

    # if value is not zero then strings are miss mathcing.
    for value in hash_map.values():
        if value != 0:
            return False

    return True

a ='aabb'

b = 'bbaa'

print(is_permutation1(a,b))




