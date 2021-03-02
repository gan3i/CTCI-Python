
# ascii or unicode is a important question, basic ascii or extended ascii.


def has_duplicates(s):


    # come to agreement with input and output before starting to code
    # I am assuming null or an empty string doesn't have duplicates
    if s == None or len(s)==0:
        return False

    #ask for case sensitive comparison
    s = s.lower()


    # this would be 256 for extended ascii
    # 65- 90 for capital alphabets, 
    # 97-122 for lower case letters 
    char_set = [False for _ in range(128)] 

    # you can iterate through string character by character in python and c++
    # but in C# or java you would have to covert string to char array first
    for c in s:
        if char_set[ord(c)] == True:
            return True
        else:
            char_set[ord(c)] = True

    return False



# assumming that string will only have ascii_letters 
def has_duplicates1(s):

    if s == None or len(s)==0:
        return False

    checker = 0

    for c in s:
        if c.islower():
            val = ord(c) - ord('a')
        else:
            val = ord(c) - ord('A')

        #left shift 1 by val times and then do an and with checker 
        # if the result is true then there is a duplicate.
        if ((checker & (1 << val)) > 0):
            return True
        else:
            #left shift 1 by val times and do an or with checker
            # this make sure that there is 1 at the position c.
            checker = (checker | ( 1 << val))

    return False
    
import string
print(has_duplicates1(string.ascii_letters))




