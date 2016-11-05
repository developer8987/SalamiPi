import Adafruit_DHT  
import os
from time import sleep
from datetime import datetime

hSwitchOn = "/home/pi/Desktop/echo-master/On.sh 24"
hSwitchOff = "/home/pi/Desktop/echo-master/Off.sh 24"

dhSwitchOn = "/home/pi/Desktop/echo-master/On.sh 18"
dhSwitchOff = "/home/pi/Desktop/echo-master/Off.sh 18"


Max = "Cool"

while Max == "Cool" :
    Hu, Te = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

    if Te > 0:
        Te = Te * 8/5 +32
    
    print str(datetime.now())
    print ""
    print "---HU: " + str(Hu) + " %"  
    print "---TE: " + str(Te) + " F"
    print ""

    
    
    if Hu > 3000:
        print "SKIP-READING SPIKE"
        print ""

        
        
    elif Hu >= 81 and Hu < 3000:
        os.system(dhSwitchOn)
        print ""
        print "ON-DE-ON-Turning ON DEhumidifier"
        print ""
        sleep (2)
        os.system(hSwitchOff)
        print ""
        print "OFF-H-OFF-Turning OFF Humidifier"
        print ""
        #sleep (10)
        #os.system(dhSwitchOff)
        #print "Turning OFF Humidifier"

    elif Hu < 81 and Hu > 73:
        os.system(dhSwitchOff)
        print ""
        print "OFF-DE-OFF-Turning OFF DEhumidifier"
        print ""
        sleep(2)
        os.system(hSwitchOff)
        print ""
        print "OFF-H-OFF-Turning OFF Humidifer"
        print ""

    elif Hu <= 73 and Hu > 0:
        os.system(dhSwitchOff)
        print ""
        print "OFF-DE-OFF-Turning OFF DEhumidifier"
        print ""
        sleep (2)
        os.system(hSwitchOn)
        print ""
        print "ON-H-ON-Turning ON Humidifier"
        print ""
 
    else:
        print "SKIP- READING FAILED"
        os.system(hSwitchOff)
        sleep (5)
        os.system(dhSwitchOff)
        #print "OFF-OFF-Turning OFF DEhumidifier"
        print ""
    sleep(30)
    
