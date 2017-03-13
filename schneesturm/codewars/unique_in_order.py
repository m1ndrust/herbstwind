
#Description:

#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.



#Optimal solution!
#from itertools import groupby
#
#def unique_in_order(iterable):
#    return [k for (k, _) in groupby(iterable)]


#My solution x_x
def unique_in_order(iterable):

    uniq = []
    if len(iterable) == 1:
            return list(iterable)


    for i in range(len(iterable)):
        if len(iterable) == 2:
            return list(set(iterable))
        elif iterable[i] != iterable[i-1]:
            uniq.append(iterable[i])


    return uniq

