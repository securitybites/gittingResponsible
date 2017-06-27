#!/usr/bin/python

import whoisLookup
import sendDisclosure
import json


#Get list of email addresses with associated urls to send to
print "Gathering whois info for reporting"
contact_info = whoisLookup.findAddressesToEmail()
print contact_info
print "Finished gathering contact info"

# Send the emails to the domain owners
print "Sending emails"
sendDisclosure.sendDisclosure(contact_info)
print "Disclosure has been completed"

