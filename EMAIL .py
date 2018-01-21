import timeit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def function1(num_mail):
    emails_done = 0
    for i in range(num_mail): 
        fromaddr = "fromaddress" #INSERT FROM ADDR(your email)
        toaddr = "Destination adress" #INSERT EMAIL TO SEND TO
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = ("INSERT SUBJECT" + str(emails_done)) #INSERT SUBJECT
         
        body ="INSERT MESSSAGE"
        msg.attach(MIMEText(body, 'plain'))
         
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "INSERT PASSWORD") #INSERT UR EMAIL PASSWORD
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        print(emails_done)
        emails_done = emails_done + 1
    server.quit()
def function2(num_mail):
    emails_done = 0
    fromaddr = "Your email" #insert your email
    toaddr = "destination adress" #insert adress to send to
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = ("SUBJECT" + str(emails_done))  #Insert subject
    with open('BeeMovieScript.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    body = data
    print(body)
    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Password") #insert password
    text = msg.as_string()
    for i in range(num_mail): 
        server.sendmail(fromaddr, toaddr, text)
        print(emails_done)
        emails_done = emails_done + 1
    server.quit()

#Function2 is faster than function1 as far as im aware
#CALL THE FUNCTIOn
