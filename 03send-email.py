import smtplib
from email.message import EmailMessage

# Email configuration
sender_email = input("Enter your email address: ")
receiver_email = input("Enter the receiver's email address: ")
app_password = input("Enter your app password: ")  # Use app-specific password here

# Email content
subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")

# Create the email
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Send the email using Gmail's SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
