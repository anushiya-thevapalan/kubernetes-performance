import json
#import objectpath
def get_container_uptime(filename, size):
    with open(filename) as datafile:
        data = json.load(datafile)

    file = open("container_uptime_"+size+".csv", "w+")

    header = ["pod_id", "cluster_name", "container_name", "instance_id", "startTime","endTime","doubleValue"]
    file.write(",".join(string for string in header))
    file.write("\n")
    required_pod_id = "190b2fae-d2d1-11e9-a58a-42010a8000c0"

    time_series = data.get("timeSeries")
    for metrics in time_series:
        resource = metrics.get("resource")
        # print(metrics.get("resource").get("labels").get("pod_id"))
        pod_id = resource.get("labels").get("pod_id")
        if (pod_id==required_pod_id):
            cluster_name = resource.get("labels").get("cluster_name")
            container_name = resource.get("labels").get("container_name")
            instance_id = resource.get("labels").get("instance_id")

            points = metrics.get("points")
            for point in points:
                startTime = point.get("interval").get("startTime")
                endTime = point.get("interval").get("endTime")
                doubleValue = point.get("value").get("doubleValue")
                data = [pod_id,cluster_name,container_name, instance_id, str(startTime), str(endTime), str(doubleValue)]
                data = ",".join(string for string in data)
                file.write(data)
                file.write("\n")
    file.close()

# Testing purpose
#filename = "/home/anushiyat/Documents/wso2/project/server-architecture-performance/container_uptime.json"
#get_container_uptime(filename,"1")
