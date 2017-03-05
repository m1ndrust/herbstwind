import re

#only accept 4 or 6 digit long pins
#return True if found
#else return False

def validate_pin(pin):
    if re.search(r"^\b\d{4}\b|^\b\d{6}\b", pin):
        print pin
        return True
    else:
        print "Wroooong."
        return False





validate_pin("123465")





