import smtplib

email = input("SENDER EMAIL: ")
reciever_email = input("RECIEVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email, "fvlt kyzn mxjv hymq")

server.sendmail(email, reciever_email, text)

print("Email has been sent to " + reciever_email)