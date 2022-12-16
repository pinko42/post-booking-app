# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC77d1d056f4f305423bc5b493d472a92a"
auth_token = "d4647c572c16070cfbff506ddfaa80df"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+15044146871",
  to="+971522662935"
)

print(message.sid)