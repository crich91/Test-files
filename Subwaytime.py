from google.transit import gtfs_realtime_pb2
import requests
import time
import os
import sqlite3 as db
import datetime
import sys
import win32
import win32file
import win32con
import pywintypes
from asciimatics.effects import Cycle, Stars, Matrix, BannerText
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from protobuf_to_dict import protobuf_to_dict
import os.path
from pathlib import Path



def demo(screen):
     
            timeslist = staion_time_lookup('A06S')
            train_text_to_display1 = calc_sched_time(timeslist, 0)
            train_text_to_display2 = calc_sched_time(timeslist, 1)

            
            #TestText = int(time.time()) + 3505
            effects = [
                Cycle(
                    screen,
                    FigletText("Next A Train: ", font='small'), int(screen.height / 2 - 8 )),
                Cycle(
                    screen,
                    FigletText(str(train_text_to_display1), font='small'), int(screen.height / 2 - 3)),
                Cycle(
                    screen,
                    FigletText("Following A Train: ", font='small'), int(screen.height / 2 + 2 )),
                Cycle(
                    screen,
                    FigletText(str(train_text_to_display2), font='small'), int(screen.height / 2 +8))
            ]

            screen.play([Scene(effects, 800)])
            f.write("Finished at: " + str(time.time()) + "\n")
            f.close()
 
    



def staion_time_lookup(station):
    api_key = 'bf83cb9a7f437c52c034339b889bf6e1'


    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key={}&feed_id=26'.format(api_key))
    feed.ParseFromString(response.content)

    f.write("Ping API: " + str(time.time()) + "\n")
    
    subway_feed = protobuf_to_dict(feed)
    train_data = subway_feed['entity']

    collected_times = []

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
    collected_times.sort()
    return collected_times

def calc_sched_time(collected_times, trainindex):
    current_time = int(time.time())
    nearest_arrival_time = collected_times[trainindex]
   
    #nearest_arrival_time = current_time + 360
   

    seconds_until_train = int(((nearest_arrival_time - current_time)))
    m, s = divmod(seconds_until_train, 60)
    sched_time = time.strftime("%I: %M %p", time.localtime(nearest_arrival_time))
    timetiltrain =  "The next A train will arrive in %02d Min %02d Sec at %s " % (m,s, sched_time) 

   
    return sched_time

def seconds_until_train(collected_times):
    current_time = int(time.time())
    nearest_arrival_time = collected_times[0]
    seconds_until_train = int(((nearest_arrival_time - current_time)))
    return seconds_until_train

#------------main------------
#staion_time_lookup('A06S')

#calc_sched_time(staion_time_lookup('A06S'))

while True:
     datafolder = "C:/Users/christopher.rich/Desktop/Python/Subwaylog.txt"

     filetoopen = datafolder
     f = open(filetoopen, "a")
     currenttime = int(time.time())
     f.write("\nstarted at: " + str(currenttime) +  "\n")



     Screen.wrapper(demo)
    











