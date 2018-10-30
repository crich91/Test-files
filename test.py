from google.transit import gtfs_realtime_pb2
import requests
import time
import os
import sqlite3 as db
import datetime
import sys


'''
api_key = 'bf83cb9a7f437c52c034339b889bf6e1'

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('http://datamine.mta.info/mta_esi.php?key={}&feed_id=26'.format(api_key))
feed.ParseFromString(response.content)


from protobuf_to_dict import protobuf_to_dict
subway_feed = protobuf_to_dict(feed)
realtime_data = subway_feed['entity']

collected_times = []

def staion_time_lookup(train_data, station):
    for trains in train_data:
        if trains.get('trip_update', False) != False:
            unique_train_schedule = trains['trip_update']
            unique_arrival_times = unique_train_schedule['stop_time_update']
            for scheduled_arrivals in unique_arrival_times:
                if scheduled_arrivals.get('stop_id', False) == station:
                    time_data = scheduled_arrivals['arrival']
                    unique_time = time_data['time']
                    if unique_time != None:
                        collected_times.append(unique_time)
    print('Done')


staion_time_lookup(realtime_data, 'A06S')

collected_times.sort()
'''
current_time = int(time.time())
#nearest_arrival_time = collected_times[0]
#second_arrival_time = collected_times[1]
nearest_arrival_time = current_time + 360
second_arrival_time = current_time  + 420

seconds_until_train = int(((nearest_arrival_time - current_time)))
seconds_until_second_train = int(((second_arrival_time - current_time)))


while seconds_until_train > 0 :

    m, s = divmod(seconds_until_train, 60)
    sched_time = time.strftime("%I: %M %p", time.localtime(nearest_arrival_time))
    timetiltrain =  "The next A train will arrive in %02d Min %02d Sec at %s " % (m,s, sched_time) 
   # print(timetiltrain + "\r" , end="")

    m2 ,s2 = divmod(seconds_until_second_train, 60)
    second_sched_time = time.strftime("%I: %M %p", time.localtime(second_arrival_time))
    timetilsecondtrain = "The following A train will arrive in %02d Min %02d Sec at %s " % (m2,s2, second_sched_time)

    sys.stdout.write(timetiltrain)
    sys.stdout.write(timetilsecondtrain)
    sys.stdout.flush()
    
    time.sleep(1)

    seconds_until_train -= 1
    seconds_until_second_train -= 1

print("Train is here!")

#for times in collected_times:
#    print(times, '=' ,time.strftime("%I: %M %p", time.localtime(times)))











'''
conn = db.connect('Test.db')

c = conn.cursor()


def createTable():
    c.execute("CREATE TABLE TestTable( ID INT, Times VARCHAR(30))")

def DataEntry():
              c.execute("INSERT INTO TestTable VALUES(2, 15)")
              conn.commit()
              c.close()
              conn.close()

              
#createTable()
DataEntry()
'''
