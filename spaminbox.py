#!/bin/env/python

import smtplib
import optparse

def get_da_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-e", "--emailaddress", dest="email", help="The email adress you wish to send the spam from, you have to know the password for this address")
    parser.add_option("-t", "--to", dest="to", help="the email address you want to spam")
    parser.add_option("-p", "--password", dest="password", help="the password for the --emailaddress argument")
    parser.add_option("-u", "--username", dest="username", help="the username for the --emailaddress argument")
    parser.add_option("-m", "--message", dest="message", help="the message you want to spam, should be kinda short")
    (options, arguments) = parser.parse_args()
    return options


options = get_da_arguments()



server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(options.email, options.password)





try:
    for i in range (0,89):

        server.sendmail(options.email, options.to, options.message)
        print("Mail sent")
except KeyboardInterrupt:
    print("closing the program")
    server.quit()
