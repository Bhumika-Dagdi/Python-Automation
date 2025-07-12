from twilio.rest import Client

# Twilio credentials (get these from your Twilio console)
account_sid = input("Enter your Twilio Account SID: ")
auth_token = input("Enter your Twilio Auth Token: ")
client = Client(account_sid, auth_token)

# Your Twilio number and destination number
twilio_number = input("Enter Twilio phone number: ")   # your Twilio phone number
to_number = input("Enter the registed number on which you want to make call (+91...): ")      # your phone number (include country code)

# Send SMS
message = client.messages.create(
    body=input("Enter the message you want to send via WhatsApp: "),
    from_=twilio_number,
    to=to_number
)

print(f"Message sent! SID: {message.sid}")
