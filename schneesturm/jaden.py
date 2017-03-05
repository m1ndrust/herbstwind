
#Jaden casing strings
#m takes string and makes every word in the string starting with an upper case letter


def toJadenCase(string):
    word_list=string.split()
    jaden=[]
    for word in word_list:
        jaden.append(word[:1].upper() + word[1:])

    print " ".join(jaden)
    return  " ".join(jaden)







toJadenCase("hello i am jaden")
