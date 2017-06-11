# A simple stopwatch progrm.

import time

#Display the program's instructions.
 
print"""Press ENTER to begin. Afterwards, press ENTER  to "click" the stopwatch.
Press Ctrl-C to quit.
 """
raw_input()  #press Enter to begin
print'Started.'
startTime=time.time() #get first lap's start time
lastTime=startTime
lapNum=1
#start tracking the lap times.
try:
    while True:
       raw_input()
       lapTime=round(time.time()-lastTime, 2)
       totalTime=round(time.time()-startTime, 2)
       print'Lap #%s: %s (%s)'%(lapNum,totalTime, lapTime)
       lapNum+=1
       lastTime=time.time()
except KeyboardInterrupt:
    print"Done"
