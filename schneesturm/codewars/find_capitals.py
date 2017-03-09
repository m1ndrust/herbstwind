#Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.


def capitals(word):

    #[ouput_expression() for(set of values to iterate) if(conditional filtering) ]

    return [pos for pos,char in enumerate(word) if char.isupper()]








