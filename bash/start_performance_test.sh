#!/bin/bash

backend_host_ip=35.193.107.31

run_time_length_seconds=900
#warm_up_time_seconds=300 # check for min vs sec
warm_up_time_minutes=5
actual_run_time_seconds=600

jmeter_jtl_location=/home/kubernetes-performance/results/jtls
jmeter_jmx_file_root=/home/kubernetes-performance/jmx

#jmeter_jtl_location=/home/anushiyat/jtls
#jmeter_jmx_file_root=/home/anushiyat/Documents/wso2/project/server-architecture-performance/jmx

jmeter_jtl_splitter_jar_file=/home/kubernetes-performance/jar/jtl-splitter-0.3.1-SNAPSHOT.jar

#new ADD
jmeter_performance_report_python_file=/home/kubernetes-performance/python/performance-report.py
jmeter_performance_report_output_file=/home/kubernetes-performance/results/results.csv

server_performance_report_generation_python_file=/home/kubernetes-performance/python/collect-metrics.py

rm -r ${jmeter_jtl_location}/

mkdir -p ${jmeter_jtl_location}/

concurrent_users=(1 10 50 100 500)
heap_sizes=(100m)
message_sizes=(521 100003)
garbage_collectors=(UseParallelGC)
use_case=prime
param_name=number
request_timeout=50000

for size in ${message_sizes[@]}
do
	start_time=$(date +%Y-%m-%dT%H:%M:%S.%N)
	echo "start time : "${start_time}
	for heap in ${heap_sizes[@]}
	do
		for u in ${concurrent_users[@]}
	    	do
				for gc in ${garbage_collectors[@]}
				do
					total_users=$(($u))

					jtl_report_location=${jmeter_jtl_location}/${use_case}/${heap}_Heap_${total_users}_Users_${gc}_collector_${size}_size
					
					echo "Report location is ${jtl_report_location}"

					mkdir -p $jtl_report_location

					echo "starting jmeter"

					jmeter  -Jgroup1.host=${backend_host_ip}  -Jgroup1.port=80 -Jgroup1.threads=$u -Jgroup1.seconds=${run_time_length_seconds} -Jgroup1.data=${message} -Jgroup1.endpoint=${use_case} -Jgroup1.param=${param_name} -Jgroup1.timeout=${request_timeout} -n -t ${jmeter_jmx_file_root}/jmeter.jmx -l ${jtl_report_location}/results.jtl


					jtl_file=${jtl_report_location}/results.jtl

					echo "Splitting JTL"

					java -jar ${jmeter_jtl_splitter_jar_file} -f $jtl_file -t ${warm_up_time_minutes}

					jtl_file_measurement_for_this=${jtl_report_location}/results-measurement.jtl

					echo "Adding data to CSV file"

					python ${jmeter_performance_report_python_file} ${jmeter_performance_report_output_file} ${jtl_file_measurement_for_this} ${actual_run_time_seconds} ${use_case} ${heap} ${u} ${gc} ${size} 

				done
		done
	done
	end_time=$(date +%Y-%m-%dT%H:%M:%S.%N)
	echo "end time : "${end_time}
	
	echo "sleeping for 6 minutes"
	sleep 6m

	echo "Collecting server metrics"

	python ${server_performance_report_generation_python_file} ${start_time} ${end_time} ${size}
done
				
			
