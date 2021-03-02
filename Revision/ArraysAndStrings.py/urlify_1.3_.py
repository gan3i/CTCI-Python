
# 1. will we have spaces just enough to replace or there can be more spaces as well.


#common string manipulation ivolves modifying the strings from 
#the end so that we don't overwrite things
def urlify(s)->str:

    if s == None:
        return None

    length = len(s)

    # covert string to character array you would have 
    # to do the same with C# and Java
    # Since we are converting string to char array 
    # this doesn't qualify as in place 
    # we can do this inplace only if we receive the char array as input 
    # or we are programming in a language where strings are mutable
    s = list(s)

    #pointer which we replace the character to
    end = length-1
    #pointer which we replace the character from
    start = end
    #traverse from end until we hit the first character
    while not s[start] != ' ':
        start -= 1

    while start >= 0:

        # when you hit a space add %20 to the end of the string starting from end pointer
        if s[start] == ' ':
            s[end] = '0'
            s[end-1] = '2'
            s[end-2] = '%'
            end -= 3
        else:
            #else just move the character to end pointer
            s[end]=s[start]
            end -=1
        #either way we would have to decrement the start by one
        start -=1

    return ''.join(s)


s = ' bc  '
print(urlify(s)) 
        