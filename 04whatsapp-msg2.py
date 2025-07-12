from twilio.rest import Client

# Twilio credentials
account_sid = input("Enter your Twilio Account SID: ")
auth_token = input("Enter your Twilio Auth Token: ")
client = Client(account_sid, auth_token)

# Send WhatsApp message
message = client.messages.create(
    body=input("Enter the message you want to send via WhatsApp: "),
    from_=input("Enter your Twilio number: "),  # Twilio sandbox number
    to=input("Enter the reciever's number (+91..): ")     # Your WhatsApp number
)

print(f"Message sent! SID: {message.sid}")

