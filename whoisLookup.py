#!/usr/bin/python

import whois
import time
import json

#Grab the vulnerable urls
def findAddressesToEmail():
    with open("files/urls.txt", "r") as ins:
        noContact = []
        data = []
        for line in ins:
            #Cleanup line ends
            line = line.rstrip('\n')
            ## For each url, lookup whois after waiting a few seconds
            time.sleep(5)
            w = whois.whois(line)
            
            if str(w.emails) != 'None':
                data.append({
                    'vulnerableSite': {
                        'url' : line,
                        'emails': w.emails
                    }
                })

            else:
                noContact.append(line)

        data_dump = json.dumps(data)

        #Print out list of sites without contact info
        print "These sites do not have contact info: " + str(noContact)

    return data_dump