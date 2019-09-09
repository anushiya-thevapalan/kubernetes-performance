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
            'Authorization': 'Bearer ya29.Glt6BzCNGJU01jHiv7TucvD_QDcHR6d3RJza-hJPfzhtYPZDP0kHKYgMn9VihlLnghhcK4AL026yp0c3GbMk286p9zzvB0w2LUkBEnGiiX5EZ7O3inoOithwC-T9'}

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

        get_container_cpu_usage(filename=filenames[0])
        get_container_cpu_utilization(filename=filenames[1])
        get_container_memory_bytes_total(filename=filenames[2])
        get_container_memory_bytes_used(filename=filenames[3])
        get_container_memory_page_fault_count(filename=filenames[4])
        get_container_uptime(filename=filenames[5])


    except Exception as e:
        print(e)

# start_time = '2019-09-04T03:55:36.751947'
# end_time = '2019-09-04T04:00:10.560052'
# schedule.every(1).minute.do(query_metrics(start_time, end_time))
query_metrics(start_time, end_time, size)

# while True:
#    schedule.run_pending()
#    #print("waiting")
#    time.sleep(1)
