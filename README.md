# BuildProject-Synthetic-Network-Monitoring-System

## Features
- Display network latency statistics in pinging Google.com, Cloudflare.com, and Yahoo.com
- Capture and store network latency results in time-series formats using Prometheus
- Visualize network latency trends in Grafana dashboards.

## Functionalities
- YAML Config File Parsing: Parse the configuration for pinging the servers.
- Ping Parsing: Transmit the data packets to servers in intervals, receive and parse the ping response, and extract latency statistics data.
- HTTP Server: Create an HTTP server to expose its endpoint for Prometheus, a time-series database server, from which to pull.
- Prometheus Python Client: Define metric and time-series data for the Prometheus server.
Prometheus Server: This is a time series database server that continuously pulls data from the HTTP server, stores it in a time series model, and allows for aggregated analysis and querying.
- Grafana: The visualization tool that pulls data from the Prometheus server, and creates industry-standard visualizations
