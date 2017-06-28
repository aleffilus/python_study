from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "22222"
# Your Auth Token from twilio.com/console
auth_token  = "2222"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+22222", 
    from_="+22222",
    body="Hello from Python!")

print(message.sid)
