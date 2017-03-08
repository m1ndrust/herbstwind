#Description:

#    You are given an array (which will have a length of at least 5, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.



def outlier(integers):
    odd = []
    even = []
    given_list = integers
    for numb in integers:
        if ((numb % 2) == 0):
            even.append(numb)
        else:
            odd.append(numb)

    if len(even) > len(odd):
        bla= list(set(given_list)^set(even))
        for item in bla:
            return int(item)
    else:
        bla_odd= list(set(given_list)^set(odd))
        for item in bla_odd:
            return int(item)

list_int = [2,4,7,8]
print outlier(list_int)

#output '7'
