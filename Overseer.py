import pyping 
import os
import platform

## Send Email function
def send_mail(hostname):
  import smtplib
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("youremail@gmail","password")

  msg = hostname + " is down"
  server.sendmail("from", "to", msg)
  server.quit()
 
  
  
###ping server

def isUp(hostname):
    

    giveFeedback = True
    
    if platform.system()== "Windows":
        response = os.system("ping " +  hostname + " -n 1")
        
    else:
        response = os.system("ping -c 1" + hostname)
       
    
    isUpBool = False
    if response == 0:
        if giveFeedback:
            print hostname, 'is up!'
        isUpBool = True
    else:
        if giveFeedback:
            print hostname, 'is down!'
            send_mail(hostname)

    return isUpBool

print (isUp("host1"))
print (isUp("Ip Address"))
print (isUp("host 2"))
print (isUp("Ip address"))
raw_input()



