import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *
import RPi.GPIO as GPIO;
import time;

def mess(st):
	message = str(sys.argv[1:]).translate(None,'[],\'')

	number = "****"
	message = "Temp is " + st 
	
	if __name__ == "__main__":    
	    username = "*******"
	    passwd = "*****"
	
	    message = "+".join(message.split(' '))
	
	 #logging into the sms site
	    url ='http://site24.way2sms.com/Login1.action?'
	    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
	
	 #For cookies
	
	    cj= cookielib.CookieJar()
	    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	    
	 #Adding header details
	    #opener.addheaders=[('User-Agent','Chromium Version 60.0.3112.89')]
	    try:
	        usock =opener.open(url, data)
	    except IOError:
	        print "error"
	        #return()
	
	    jession_id =str(cj).split('~')[1].split(' ')[0]
	    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
	    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
	    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	    try:
	        sms_sent_page = opener.open(send_sms_url,send_sms_data)
	    except IOError:
	        print "error"
	        #return()
	
	    print "success" 
    #return ()

NG = 6
EG = 7
SG = 8
WG = 9

NA = 10
EA = 12
SA = 13
WA = 16

NR = 17
ER = 18
SR = 19
WR = 20

GPIO.setmode(GPIO.BCM);

GPIO.setup(NG,GPIO.OUT);
GPIO.setup(EG,GPIO.OUT);
GPIO.setup(SG,GPIO.OUT);
GPIO.setup(WG,GPIO.OUT);

GPIO.setup(NA,GPIO.OUT);
GPIO.setup(EA,GPIO.OUT);
GPIO.setup(SA,GPIO.OUT);
GPIO.setup(WA,GPIO.OUT);

GPIO.setup(NR,GPIO.OUT);
GPIO.setup(ER,GPIO.OUT);
GPIO.setup(SR,GPIO.OUT);
GPIO.setup(WR,GPIO.OUT);


def glow(GPIO_PIN, status):
    GPIO.output(GPIO_PIN, status);

def alloff(status):
        x = [6,7,8,9,10,12,13,16,17,18,19,20]
	for i in x:   
        	glow(i,False);

import time
import urllib2
import json
f=urllib2.urlopen('http://api.wunderground.com/api/49f71f00a1cffba7/conditions/q/CA/kothrud.json')
json_string=f.read()
parsed_json=json.loads(json_string)
v=parsed_json["current_observation"]["temp_c"]
print v
alloff(True);
if v<15:
    alloff(True);
    time.sleep(2);
    glow(7,True);
    mess('Low Temperature');
    time.sleep(5)
    GPIO.cleanup()
    time.sleep(1)
else:
    alloff(True);
    time.sleep(2);
    glow(18,True);
    mess('High Temperature');
    time.sleep(5)
    GPIO.cleanup()
    time.sleep(1)