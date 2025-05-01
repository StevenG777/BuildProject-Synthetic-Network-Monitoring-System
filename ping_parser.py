# Fetch libraries
from prometheus_client import start_http_server, Gauge, Counter
import pingparsing
import yaml
import time

# Access configuration YAML file
file_path = '/Users/steveg/Documents/Coding & Development Related/Open Avenue/Build_Project3/Final_Project/'
file_name = 'config.yaml'
try:
    with open(file_path + file_name, 'r') as f:
        parsed_content = yaml.safe_load(f)
except Exception as e:
    print(f"ERROR happens! Details: {e}")
else:
    print("Parsed configuration file successfully!")

# Extract configuration parameters
servers = parsed_content['servers']
package_cnt = parsed_content['package_counts']
time_interval = parsed_content['time_interval']

# Start up the HTTP server to expose the metrics to Prometheus server.
start_http_server(8000)

# Define the Prometheus metrics
g_rtt = Gauge(name="round_trip_time_gauge", documentation="rtt metric", labelnames=["server", "stat"])

# Define ping sender(transmitter) & receiver(parser)
parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()

# 1. Ping the servers indefinitely until program is stopped
# 2. Pass the ping statistics to Prometheus
while True:
    # Iterate each server to ping
    for server in servers:
        # Configure the ping sender (transmitter)'s parameters
        transmitter.destination = server
        transmitter.count = 10

        # Ping (transmit) to servers and parse the response
        result = transmitter.ping()
        parsed_result = parser.parse(result).as_dict()

        # Define time series data and sync with Prometheus
        g_rtt.labels(server=server, stat='min').set(parsed_result['rtt_min'])
        g_rtt.labels(server=server, stat='avg').set(parsed_result['rtt_avg'])
        g_rtt.labels(server=server, stat='max').set(parsed_result['rtt_max'])
        g_rtt.labels(server=server, stat='mdev').set(parsed_result['rtt_mdev'])

    # Set a time interval after pinging all servers before the next round of pinging
    print("Pinged all servers successfully!")
    time.sleep(time_interval)
    print(f"Waited {time_interval} seconds")
    print()