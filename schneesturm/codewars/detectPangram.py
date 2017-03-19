#A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.


import string
def is_pangram(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"

    new_s = ''.join([i for i in s if not i.isdigit()])
    lowerString = new_s.lower()
    joinString = lowerString.replace(' ','').replace(',','').replace('!','').replace('.','')




    if set(alphabet).issubset(joinString):
        print "wow"
        return True
    else:
        return False



