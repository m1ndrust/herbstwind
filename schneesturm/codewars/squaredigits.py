
#codewars // square every digit
#eg: 9119 == 811181

def square(num):
    num_to_string = str(num)
    squared =[]
    for i in num_to_string:
        squared.append(int(i) ** 2)

    s = ''.join(map(str,squared))
    print int(s)
    return int(s)


square(9119)
