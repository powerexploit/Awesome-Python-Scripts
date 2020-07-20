#import all the necessary libraries
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

#creating the object of class MIMEMultipart
message = MIMEMultipart("alternative")

#Body of message in HTML format
html = """\
<html>
  <body>
    <p>Some Text in HTML</p>
  </body>
</html>
"""

part2 = MIMEText(html, "html")

#attaching the html message to object
message.attach(part2)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

#Enter email and password
sender_email = "email@gmail.com"  # Enter your address
password = "passworddd"     


print("Starting")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    #Enter your CSV file here
    with open("testt.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        #Enter the attributes. Here we have attributes as serial name and email
        for serial,name,email in reader:

            #creating another MIMIMultipart object
            msg= MIMEMultipart("alternative")

            #Enter your subject here
            msg["Subject"] = "Enter your subject here"
            msg.attach(message)
            
            #Here we have different file for different serial number. Thus in each loop we are accessing new file
            filename = str(serial)+str(".pdf")  # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            msg.attach(part)

            #this tell the library that mark sender email as from and the email to which the mail has to sent is set to "to".
            msg["From"] = sender_email
            msg["To"] = email


            #Copying everything in msg object as string to text
            text = msg.as_string()
            
            #Finally sending mail.Phew!!!
            server.sendmail(sender_email, email, text)
            print(name)

            #deleting the msg object and part. This is necessary otherwise 
            # every file will get attach with previous file. 
            # Thus 1st recipient will receive one file and second will receive 2 and third three and so on.
            del msg
            del part
print("Done")
