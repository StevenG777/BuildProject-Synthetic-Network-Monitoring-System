# BuildProject-Synthetic-Network-Monitoring-System

## Features
- Display network latency statistics in pinging Google.com, Cloudflare.com, and Yahoo.com
- Capture and store network latency results in time-series formats using Prometheus
- Visualize network latency trends in Grafana dashboards.

## Functionalities
- **Ping Config File Parser**: Parse the YAML configuration file for pinging the servers.
- **Ping Parser**: Transmit the data packets to servers in intervals, receive and parse the ping response, and extract latency statistics data.
- **HTTP Server**: Create an HTTP server to expose its endpoint for Prometheus, a time-series database server, from which to pull.
- **Prometheus Python Client**: Define metric and time-series data for the Prometheus server.
- **Prometheus Server**: This is a time series database server that continuously pulls data from the HTTP server, stores it in a time series model, and allows for aggregated analysis and querying.
- **Prometheus Config File**: Modify the config file to include the source target information for the Prometheus server to pull from.
- **Grafana**: The visualization tool that pulls data from the Prometheus server and provides an industry-standard dashboard.
- *Future Development*:
  - *Host each component in AWS EC2*
  - *Monitor other PING metrics*
  - *Monitor other Network metrics*

## Tech Stack
- Python
- Prometheus Python Client
- Prometheus
- Grafana

## How to Start the Application
- For PING Parser:
  - Navigate to the directory of ping_parser.py, run `Python ping_parser.py`
  - The program will run indefinitely to collect ping results
  - The HTTP server will run on port 8000

 - For Prometheus:
   - Install the Prometheus
   - Extract the Prometheus package: `tar xvfz prometheus-*.tar.gz`
   - Start the server:
     1. Navigate to the directory: `cd prometheus-*`
     2. Start the server: `./prometheus --config.file=prometheus.yml`
     3. The server will run on port 9090
   - Access the GUI:
     1.  Open your web browser
     2.  Go to `http://localhost:9090/`
   
- For Grafana:
  - Install the Grafana
  - Extract the Grafana package: `tar xvfz grafana-*.tar.gz`
  - Start the server:
    1. Navigate to the directory: `cd grafana-*`
    2. Start the server: `./bin/grafana server`
    3. The server will run on port 3000
  - Access the GUI:
    1. Open your web browser
    2. Go to `http://localhost:3000/`

## Final Result
Grafana Dashboard:

