import sys
import os.path
import csv
from jtl_stats import *

def getIfHasAttribute(dictionary, key):
    if(key in list(dictionary.keys())):
        return dictionary[key]
    else:
        return "NA"


output_csv_file = sys.argv[1]

jtl_file_measurement_for_this= sys.argv[2]
run_time_seconds= sys.argv[3]
use_case= sys.argv[4]
heap= sys.argv[5]
u= sys.argv[6]
gc= sys.argv[7]
size= sys.argv[8]

csv_file_records = []
basic_headers = ['use case', 'heap', 'concurrency', 'garbage collector', 'workload']
basic_values = [use_case, heap, u, gc, size]

jtl_headers=['average_latency', 'min_latency', 'max_latency', 'percentile_10', 'percentile_20',
             'percentile_50', 'percentile_90', 'percentile_99', 'percentile_999', 'percentile_9999', 'percentile_99999', 'percentile_999999', 'percentile_9999999', 'throughput']
jtl_values=[]

if os.path.isfile(jtl_file_measurement_for_this):
    latency = getLatencyList(jtl_file_measurement_for_this)
    jtl_values.append(getAverageLatency(latency))
    jtl_values.append(min(latency))
    jtl_values.append(max(latency))

    jtl_values.append(get_percentile(latency, 10))
    jtl_values.append(get_percentile(latency, 20))
    jtl_values.append(get_percentile(latency, 50))
    jtl_values.append(get_percentile(latency, 90))
    jtl_values.append(get_percentile(latency, 99))
    jtl_values.append(get_percentile(latency, 99.9))
    jtl_values.append(get_percentile(latency, 99.99))
    jtl_values.append(get_percentile(latency, 99.999))
    jtl_values.append(get_percentile(latency, 99.9999))
    jtl_values.append(get_percentile(latency, 99.99999))

    jtl_values.append(len(latency)/int(run_time_seconds))

if not os.path.isfile(output_csv_file):
    with open(output_csv_file, "a+") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        headers = basic_headers+ jtl_headers
        writer.writerow(headers)

with open(output_csv_file, "a+") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    values =  basic_values + jtl_values 
    writer.writerow(values)







