# importing the requests library
import time, re, sys
import requests, schedule

# importing the URL % encoding library
import urllib
# importing datetime to get the timestamp
import datetime
from container_cpu_usage_time import *
from container_cpu_utilization_stats import *
from container_memory_bytes_total_stats import *
from container_memory_bytes_used_stats import *
from container_memory_page_fault_count_stats import *
from container_uptime_stats import *

start_time = sys.argv[1]
end_time = sys.argv[2]
size = sys.argv[3]


def query_metrics(start_time, end_time, size):
    try:
        # python 2
        # start_time = urllib.quote(start_time, safe='')
        # python3
        start_time = urllib.parse.quote(start_time, safe='')

        end_time = urllib.parse.quote(end_time, safe='')
        filenames = []

        container_metrics_list = ["container/cpu/usage_time", "container/cpu/utilization", "container/memory/bytes_total",
                        "container/memory/bytes_used", "container/memory/page_fault_count", "container/uptime"]
        headers = {
            'Authorization': 'Bearer ya29.Glt-B90SSdzGrloQmUYE5g2nlrM-WQ0H0oW2x5d2_m0A9v6BbN_kxpaZ-2dLM8d19qSQF1egzBgPrITOkpBr3eJ-jTPKHSqRhR-PfIPji5Xvb1WEN6qxUUmpitO7'}

        for metrics in container_metrics_list:
            # file = open(str(time.time()), "a")
            filename = metrics.replace("/", "_")+"_"+size+".json"
            filenames.append(filename)

            file = open(filename, "w+")

            URL = "https://monitoring.googleapis.com/v3/projects/auto-scaling-springboot/timeSeries?filter=metric.type%20%3D%20%22container.googleapis.com%2F"+urllib.parse.quote(metrics, safe='')+"%22%20&interval.endTime=" + end_time + "Z&interval.startTime=" + start_time + "Z&key=AIzaSyDz_HsXVzYERtbBHH1jVOP1JsiIiTIjL9I"
            response = requests.get(url=URL, headers=headers)

            data = response.text

            file.write(data)
            file.close()

        get_container_cpu_usage(filename=filenames[0], size=size)
        get_container_cpu_utilization(filename=filenames[1], size=size)
        get_container_memory_bytes_total(filename=filenames[2], size=size)
        get_container_memory_bytes_used(filename=filenames[3], size=size)
        get_container_memory_page_fault_count(filename=filenames[4], size=size)
        get_container_uptime(filename=filenames[5], size=size)


    except Exception as e:
        print(e)

#start_time = '2019-09-09T04:42:45.615723941'
#end_time = '2019-09-09T04:42:45.615723941'
#size = "521"
# schedule.every(1).minute.do(query_metrics(start_time, end_time))
query_metrics(start_time, end_time, size)

# while True:
#    schedule.run_pending()
#    #print("waiting")
#    time.sleep(1)
