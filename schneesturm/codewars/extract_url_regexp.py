import re
#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.



def domain_name(url):

    match = re.search('(?:http[s]{0,1}://){0,1}[w]{0,3}[\.]{0,1}(.*?)\.[a-z]{2,}', url)

    print match.group(1)
    return match.group(1)




domain_name("www.google.de")

