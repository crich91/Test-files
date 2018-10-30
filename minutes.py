import datetime
import time

seconds = 240

#secondsdelta =str(datetime.timedelta(seconds = seconds))

#print(secondsdelta)

while seconds > 0 :

    m, s = divmod(seconds, 60)
    timetiltrain =  "%02d Min %02d Sec" % (m,s) 
    print(timetiltrain + "\r" , end="")
    time.sleep(1)

    seconds -= 1 

print ("done") 
