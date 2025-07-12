import smtplib
from email.mime.text import MIMEText

sender_email = input("Enter your email: ")    # You have access to this
app_password = input("Enter your app password: ")  # You have access to this
receiver_email = input("Enter the receiver's email: ")  # You have access to this
subject = input("Enter the email subject: ")  # You have access to this
body = input("Enter the email body: ")  # You have access to this

message = MIMEText(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()

print("Email sent.")
