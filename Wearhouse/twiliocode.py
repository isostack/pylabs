import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

TWILIO_SID = TOKENS["twilio.com sid"]
TWILIO_AUTH = TOKENS["twilio.com auth"]

client = Client(TWILIO_SID, TWILIO_AUTH)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)
