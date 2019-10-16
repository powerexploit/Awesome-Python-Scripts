# need to import the smtp lib
import smptplib


# TLS port = 587, normal_port=465
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
print("TYPE_SMTP_OBJ", type(smtp_obj))

smtp_obj.ehlo()

#starttls() puts smtp in TLS mode
smtp_obj.starttls()

smtp_obj.login('email_address', 'password')

sender_email_adress = 'abcd@efg.com'
list_of_reciever_addresses = ['email_1@xxxx.com', 'email_2@xxxx.com']

smtp_obj.sendemail(sender_email_address, list_of_reciever_addresses, 'Subject: the body of the message') 

#close the smtp obj when done
smtp_obj.quit()
