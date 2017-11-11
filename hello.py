    import logging
import requests
from flask import Flask
from flask_ask import Ask, statement, context

app = Flask(__name__)
ask = Ask(app, '/')
log = logging.getLogger('flask_ask').setLevel(logging.DEBUG)

def get_alexa_location():
    URL =  "https://api.amazonalexa.com/v1/devices/{}/settings" \
           "/address".format(context.System.device.deviceId)
    TOKEN =  context.System.user.permissions.consentToken
    HEADER = {'Accept': 'application/json',
             'Authorization': 'Bearer {}'.format(TOKEN)}
    r = requests.get(URL, headers=HEADER)
    if r.status_code == 200:
        return(r.json())


@ask.launch
def launch():
    return start()

@ask.intent("WhatIsMyLocation")
def start():
    location = get_alexa_location()
    print( location );
    return statement( location[ "postalCode" ] );
    # city = "Your City is {}! ".format(location["city"].encode("utf-8"))    
    # address = "Your address is {}! ".format(location["addressLine1"].encode("utf-8")) 
    # speech = city + address   
    # return statement(speech)

if __name__ == '__main__':
    app.run(debug=True)