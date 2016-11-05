import smtplib
import Adafruit_DHT

Hu, Te = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

Te = Te * 8/5 +32

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("therealwomprat@gmail.com", "MKnjbh12")




 
#msg = "HUMIDITY: " + str(Hu) + "  TEMP: " + str(Te)
msg = "Humidity " + str(Hu)[:6] + "  Temp " + str(Te)[:6]
print msg
server.sendmail("therealwomprat@gmail.com", "max8987@gmail.com", msg)
server.quit()
