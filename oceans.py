# Author: Tyler Smith, tylsmith@gmail.com, (805)444-4378
# Scrapes from IP address /monitor.htm, which is html that is updated by the sensors
# output is written to the same folder as the script

import urllib2
import re
from datetime import datetime
import time

ip_prefix="http://169.254.185."
url_suffix="/monitor.htm"

output_prefix="sensor"
output_extension=".txt"

time_interval = 10 #refresh rate in seconds

while True:
    for i in range(1,5):
        html = urllib2.urlopen(ip_prefix + str(i) + url_suffix).read()
        phs = re.findall("-?\d*\.\d* pH", html)
        temperatures = re.findall("-?\d*\.\d* .*C", html)
        phs = ["1", "1"]
        temperatures = ["2", "2"]
        for j in range(0, 2):
            if (2 * (i-1) + j + 1) == 6:
                continue
            output = str(datetime.now()) + "  " + phs[j] + "  " + temperatures[j] +"\n"
            f = open("sensor" + str((2 * (i-1)) + j + 1) + ".txt", "a")
            f.write(output)
            f.close()
            print("wrote:" + output)



    time.sleep(time_interval)
