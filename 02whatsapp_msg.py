import pywhatkit as kit

number=input("Enter the phone number with country code (e.g., +91..): ")
msg=input("Enter the message you want to send: ")
kit.sendwhatmsg_instantly(number, msg, tab_close=True, close_time=3)

