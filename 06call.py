from twilio.rest import Client

# Twilio credentials
account_sid = input("Enter your Twilio Account SID: ")  
auth_token = input("Enter your Twilio Auth Token: ")
twilio_number = input("Enter Twilio phone number: ")         # Twilio phone number
receiver_number = input("Enter receiver's number which is already registered in Twilio: ")     # Your phone number

# Initialize client
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    to=receiver_number,
    from_=twilio_number,
    url="http://demo.twilio.com/docs/voice.xml"  # Twilio provides XML for automated voice
)

print(f"Call initiated. SID: {call.sid}")
