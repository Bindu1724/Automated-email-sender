import smtplib

email = input("SENDER EMAIL: ")
reciever_email = input("RECIEVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587) #creates a connection to Gmail's SMTP server on port 587
server.starttls() #upgrades the connection to use encryption (TLS) for secure data transmission.

server.login(email, "fvlt kyzn mxjv hymq") #logs into the sender's email account using the email address and a password or app-specific key 

server.sendmail(email, reciever_email, text)

print("Email has been sent to " + reciever_email)
