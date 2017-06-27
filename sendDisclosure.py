import smtplib
import json
import time
import sys

##Configs
gmail_user = 'xxx@xxx.xxx'  
gmail_password = 'xxxxx' # You will need to generate a Google app password for this to work

GMAIL_USERNAME = 'xxxx@xxxx.xxx' #This is the alias your emails will be sent from, could be the same as gmail_user if you wish
email_subject = 'Responsible Security Disclosure'



def sendDisclosure(data):

    #Make connection to gmail server, once
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)

        print 'Connection to gmail successful!'
        
    except:  
        print 'Something went wrong when connecting to gmail...'

    data = json.loads(data)

    for site in data:
        insert_site = site['vulnerableSite']['url']

        emails = site['vulnerableSite']['emails']
        
        if type(emails) is unicode:
            emails = [emails]
            

        for email in emails:
            recipient = str(email)

            headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                                "subject: " + email_subject,
                                "to: " + recipient,
                                "mime-version: 1.0",
                                "content-type: text/html"])

            body_of_email = 'During the course of a security research project I was completing, your site ' + insert_site + \
                ' was discovered to have a serious security' \
                ' vulnerability present. The goal of this email is to responsibly disclose ' \
                'this issue to you so your technical team can mitigate the issue as soon as possible and minimize any impact.' \
                ' If you have an active bug bounty program you would like me to report additional details through please reply with contact information.' \
                ' Technical Details: The source code of your site is exposed at the root of your site at ' + insert_site + '/.git/'


            content = headers + "\r\n\r\n" + body_of_email

            try:  
                time.sleep(10) #Just so we dont freak Google out
                server.sendmail(GMAIL_USERNAME, recipient, content)
                

                print 'Email sent to: ' + recipient
            except:  
                print 'Something went wrong...' + str(sys.exc_info()[0])
    
    #Close the gmail sever connection
    server.close()