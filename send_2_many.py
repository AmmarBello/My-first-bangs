import csv
#from Setting import SENDER_EMAIL, SENDER_PASSWORD
import smtplib, socket, sys, getpass
 

MASSAGE="""
{},


Assalam alaikum wa rahmatullah,
Kindly;
be reminded that Friday 7th April is the deadline to pay the reg. fee of N15,000
as confirmation of your attendence in the forthcoming workshop slated for 16th & 17th April.
Therefore consideration will only be given to those who make the payment before or on the specified date.

Wajazakumullah khairan


Account name: IET/DIN 
Account number 2002947064
Bank name: UBA

Respectfully,
Hamza Sani (DIN-IET)

"""
def main():
  print
  with open('Jlist.csv') as send_mail_file:
    csv_reader=csv.reader(send_mail_file, delimiter=',')
    next(csv_reader)
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
    try:
       for row in csv_reader:
          Name, Email=row
          msg=MASSAGE.format(Name)
          subject='Jaseer Auda workshop'
          #print('Send e-mail to: {}'.format(email))
          #print('E-mail content:')
          #print(msg)
          email_msg="Subject:{}\n\n{}".format(subject, msg)
          
          smtpserver.sendmail(gmail_user, Email, email_msg)
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
