import smtplib, socket, sys, getpass

def main():
    print
    
    try:
        smtpserver=smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print 'Connection to Gmail successefully'
        print 'Connected to Gmail'+'\n' 
        try:
           gmail_user=str(raw_input("Enter your Email: ")).lower().strip()
           gmail_pwd=getpass.getpass("Enter your email password: ").strip()
           smtpserver.login(gmail_user, gmail_pwd)
        except:
           print 'Authentication fail'+ '\n'
           smtpserver.close()
           getpass.getpass('Press ENTER to continue...')
           sys.exit(1)
         
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        print 'Connection to Gmail fail'
        print e 
        getpass.getpass('Press ENTER to continue...')
        sys.exit(1)
    while True:
        to=str(raw_input("Send mail to: ")).lower().strip()
        if to!='':
            break
        else:
            print 'This field can not be blank'
    sub=str(raw_input("Subject: "))
    body=str(raw_input("body of mail: "))
    print
    header='To: ' + to + '\n' + 'From: '+ gmail_user +'\n'+ 'Subject: ' + sub + '\n'
    print header
    msg=header+'\n'+body+'\n\n'
    try:
       smtpserver.sendmail(gmail_user, to, msg)
    except smtplib.SMTPException:
       print 'Gmail could not be sent' + '\n'
       smtpserver.close()
       getpass.getpass('Press ENTER to continue...')
       sys.exit(1)
    print 'Email sent succesfully'
    smtpserver.close()
    getpass.getpass('Press ENTER to continue...')
    sys.exit(1)







    print '\n'
    raw_input('pause program')
main()
