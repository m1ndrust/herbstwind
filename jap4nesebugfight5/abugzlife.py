import requests
import time
import dns.resolver
import subbrute
import sys



#BugBoobiez [working title]

#Main purpose: Automate as much as possible and have a directory of visited websites with notes

# 1.Subdomain scanner
# 2.Hostile Subdomain scanner
# 3.Directory Bruteforcer
# 4.Upload list of visited websites incl. notes and a visual indication when the site was last visited


#ASK THEM ABOUT THE FULL LIST AT DETECTIFY
#The original article states 17 services, we have now identified 100+ different ways that you can be vulnerable to a domain takeover


#(TODO: Dir Bruteforcer)
#TODO: Upload list in a table or something
#TODO: send found domains to email
#TODO: use wordlist
#TODO: different resolvers, different user-agent [blacklist avoidance]
#TODO: import subbrute.. and use a thread for each subbrute run on a company website
#TODO: Creates subdomain list, implement check if this file is present just use it, otherwise create it with another subbrute scan

#dictionary with Company:Magic_String is better

magic_strings = {'amazon':'NoSuchBucket', 'github':'There isn\'t a GitHub Pages site here',
                 'COMPANY':'there is no app configured at that hostname','COMPANY':'No Such Account','COMPANY':'Sorry, this shop is currently unavailable',
                 'COMPANY':'Sorry, this shop is currently unavailable','COMPANY':'There\'s nothing here','COMPANY':'The site you were looking for couldn\'t be found',
                 'COMPANY':'You\'re almost there...',
                }
                #Fastly
                #BlueDigital?
                #Microsoft Azure App Service 'Error 404 Web app not found'


def get_subdomains(company):

    subdomains = []
    start = time.time()
    print "[+]trying to find some subdomains for "+company
    print "[+]be patient and read something on [website] "
    print "[+]Started on " + time.strftime("%c") 

    with open(company+'.txt','w+') as text_file:
        for subdomain in subbrute.run(company):
            print subdomain[0]
            text_file.write(subdomain[0]+'\n')
            subdomains.append(subdomain[0])
        text_file.close()   
         
    end = time.time()

    hours,rem = divmod(end-start,3600)
    minutes,seconds = divmod(rem,60)
    print "[+]time taken --> {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

    return subdomains

def get_http_status(subdomainList):

    #subdomains=[]
    four0subdomains =[]
    
    with open(subdomainList, "r") as subwords:      #works with a textfile but not with a list!!!
        for subword in subwords:
            time.sleep(0.5)
            subdomain = "http://"+subword.strip()                           #use http and redirect the request in case its https
            try:
                r = requests.get(subdomain,verify=False, timeout=2)
                if r.status_code == 404:
                    four0subdomains.append(subdomain)
                else:   
                    print subdomain +" status_code: \033[1;35m[{}]\033[1;m".format(r.status_code)
                    #generate overview over all subdomains with their statuscodes like so: subdomain status
                    subdomains.append(subdomain)
            except:
                pass


            
    

    print "404 ->{}".format(four0subdomains)
    return four0subdomains    

def hostile_takeover(Four0subdomains):

    print "[+] Cross your fingers now!"
    for domain in Four0subdomains:
        try:
            
            print domain
            print "-------DNS INFO---------------------------------------------------------------------"
            print dns.resolver.query(domain, 'CNAME').response
            print "-------DNS INFO---------------------------------------------------------------------"
        except:
            pass
    
    #This is shit because we have to make an EXTRA request(We already make a request in get_subdomains(). Change it
    for domain in Four0subdomains:
        response = requests.get(domain)
        if magic_strings['amazon'] in response.content:     # Loop through the magic_strings
            print "The string [{0}] was found on subdomain [{1}].Try to claim it from {2} and get some internet points.".format(magic_strings['amazon'],domain,magic_strings.keys()[0])


def main():

    if len(sys.argv) != 2:
        print "[help] python bugboobiez.py subdomainlist.txt"
        exit()


    print "######www.convuleted-wiring.net########"
    print "\033[1;32m[!] Remember kids! Keep your wordlists up-2-date.\033[1;m"
    
    if ".txt" in sys.argv[1]:
        status_list = get_http_status(sys.argv[1])
        hostile_takeover(status_list)
        exit()
    else:                       #make it more explicit e.g. sjkldhfsdf should be rejected. Deal with real URL
        subdomain_list = get_subdomains(sys.argv[1])
        status_list = get_http_status(subdomain_list)
        hostile_takeover(status_list)
        exit()


        

if __name__ == "__main__":
        main()




